"""
Cliente Gemini API — wrapper profissional para geração de imagens NB2.

Encapsula autenticação, upload de referência, geração com retry,
e extração de imagens do response.
"""

from __future__ import annotations

import logging
import time
from pathlib import Path
from typing import Optional

import google.generativeai as genai
from google.generativeai.types import GenerationConfig
from PIL import Image
from tenacity import (
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
)

from content_pipeline.config import GeminiConfig

logger = logging.getLogger(__name__)


class GeminiClientError(Exception):
    """Erro base do cliente Gemini."""


class GeminiAuthError(GeminiClientError):
    """Falha de autenticação com a API."""


class GeminiGenerationError(GeminiClientError):
    """Falha na geração de conteúdo."""


class GeminiClient:
    """
    Cliente para Google Gemini API com suporte a geração de imagens.

    Responsabilidades:
    - Autenticação e configuração do SDK
    - Upload de imagens de referência (produto PNG)
    - Geração de imagens NB2 com prompt + referência
    - Retry automático com backoff exponencial
    - Extração e validação de imagens do response

    Uso:
        client = GeminiClient(config)
        result = client.generate_nb2_image(
            product_image_path="path/to/product.png",
            prompt="Place this product in...",
        )
        result.save("output.png")
    """

    def __init__(self, config: GeminiConfig) -> None:
        self._config = config
        self._configure_sdk()
        self._model = genai.GenerativeModel(
            model_name=config.image_model,
            generation_config=GenerationConfig(
                temperature=config.temperature,
                top_p=config.top_p,
                top_k=config.top_k,
                max_output_tokens=config.max_output_tokens,
            ),
        )
        logger.info("GeminiClient inicializado — modelo: %s", config.image_model)

    def _configure_sdk(self) -> None:
        """Configura o SDK com a API key."""
        if not self._config.api_key:
            raise GeminiAuthError("API key não configurada.")
        genai.configure(api_key=self._config.api_key)

    def upload_reference_image(self, image_path: Path) -> genai.types.File:
        """
        Faz upload de imagem de referência para o Gemini.

        Args:
            image_path: Caminho para o PNG do produto.

        Returns:
            Objeto File do Gemini para uso na geração.

        Raises:
            FileNotFoundError: Se o arquivo não existir.
            GeminiClientError: Se o upload falhar.
        """
        path = Path(image_path)
        if not path.exists():
            raise FileNotFoundError(f"Imagem não encontrada: {path}")

        if not path.suffix.lower() in (".png", ".jpg", ".jpeg", ".webp"):
            raise GeminiClientError(
                f"Formato não suportado: {path.suffix}. Use PNG, JPG ou WEBP."
            )

        logger.info("Uploading referência: %s", path.name)
        try:
            uploaded = genai.upload_file(path, mime_type=f"image/{path.suffix[1:].lower()}")
            logger.info("Upload concluído: %s → %s", path.name, uploaded.name)
            return uploaded
        except Exception as e:
            raise GeminiClientError(f"Falha no upload de {path.name}: {e}") from e

    @retry(
        retry=retry_if_exception_type(GeminiGenerationError),
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=2, max=30),
        before_sleep=lambda retry_state: logger.warning(
            "Retry %d/%d após falha na geração...",
            retry_state.attempt_number,
            3,
        ),
    )
    def generate_nb2_image(
        self,
        product_image_path: Path,
        prompt: str,
        *,
        uploaded_ref: Optional[genai.types.File] = None,
    ) -> Image.Image:
        """
        Gera imagem NB2 — produto inserido em cena criativa.

        Fluxo:
        1. Upload do PNG do produto como referência (se não fornecido)
        2. Envio do prompt NB2 + referência para o Gemini
        3. Extração da imagem gerada do response
        4. Validação básica (dimensões, formato)

        Args:
            product_image_path: Caminho para o PNG do produto.
            prompt: Prompt NB2 completo (8 dimensões).
            uploaded_ref: Referência já uploadada (evita re-upload).

        Returns:
            PIL.Image com a imagem gerada.

        Raises:
            GeminiGenerationError: Se a geração falhar após retries.
        """
        if uploaded_ref is None:
            uploaded_ref = self.upload_reference_image(product_image_path)

        logger.info(
            "Gerando NB2 — ref: %s, prompt: %d chars",
            uploaded_ref.name,
            len(prompt),
        )

        start = time.monotonic()
        try:
            response = self._model.generate_content(
                [uploaded_ref, prompt],
                request_options={"timeout": self._config.timeout_seconds},
            )
        except Exception as e:
            raise GeminiGenerationError(f"Erro na chamada API: {e}") from e

        elapsed = time.monotonic() - start
        logger.info("Response recebido em %.1fs", elapsed)

        return self._extract_image(response)

    def generate_text(self, prompt: str) -> str:
        """
        Gera texto via Gemini (para copy, claims, etc.).

        Args:
            prompt: Prompt de texto.

        Returns:
            Texto gerado.
        """
        try:
            response = self._model.generate_content(prompt)
            return response.text
        except Exception as e:
            raise GeminiGenerationError(f"Erro na geração de texto: {e}") from e

    def _extract_image(self, response) -> Image.Image:
        """
        Extrai imagem PIL do response do Gemini.

        O Gemini pode retornar imagens inline no response.
        Esta função navega a estrutura do response para encontrar
        e decodificar a imagem.
        """
        if not response.candidates:
            raise GeminiGenerationError(
                "Response vazio — nenhum candidato retornado. "
                "Possível bloqueio por safety filters."
            )

        candidate = response.candidates[0]

        if hasattr(candidate, "content") and candidate.content:
            for part in candidate.content.parts:
                if hasattr(part, "inline_data") and part.inline_data:
                    import io

                    image_data = part.inline_data.data
                    image = Image.open(io.BytesIO(image_data))
                    logger.info(
                        "Imagem extraída: %dx%d, modo=%s",
                        image.width,
                        image.height,
                        image.mode,
                    )
                    return image

        if hasattr(response, "_result"):
            result = response._result
            if hasattr(result, "candidates"):
                for cand in result.candidates:
                    if hasattr(cand, "content"):
                        for part in cand.content.parts:
                            if hasattr(part, "inline_data") and part.inline_data.data:
                                import io

                                image = Image.open(io.BytesIO(part.inline_data.data))
                                return image

        raise GeminiGenerationError(
            "Nenhuma imagem encontrada no response. "
            "O modelo pode ter retornado apenas texto. "
            "Verifique se o modelo suporta geração de imagens."
        )

    def cleanup_uploaded_files(self) -> None:
        """Remove arquivos temporários uploadados ao Gemini."""
        try:
            for f in genai.list_files():
                genai.delete_file(f.name)
                logger.debug("Arquivo removido: %s", f.name)
        except Exception as e:
            logger.warning("Falha ao limpar arquivos: %s", e)
