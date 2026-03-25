"""
NB2 Engine — motor de geração product-in-scene.

Orquestra o fluxo completo:
1. Carrega VDP → extrai prompt e metadados
2. Resolve caminho do PNG do produto
3. Chama Gemini API com referência + prompt
4. Valida resultado
5. Salva imagem com metadados

Suporta:
- Geração única ou em batch
- Múltiplas tentativas com variação de prompt
- Salvamento de intermediários para análise
"""

from __future__ import annotations

import json
import logging
import time
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

from PIL import Image

from content_pipeline.api.gemini_client import GeminiClient, GeminiGenerationError
from content_pipeline.config import PipelineConfig
from content_pipeline.nb2.prompt_builder import PromptBuilder
from content_pipeline.nb2.vdp_loader import VDPLoader, VDPSpec
from content_pipeline.output.manager import OutputManager

logger = logging.getLogger(__name__)


@dataclass
class GenerationResult:
    """Resultado de uma geração NB2."""

    vdp: VDPSpec
    image: Optional[Image.Image]
    output_path: Optional[Path]
    success: bool
    attempts: int
    elapsed_seconds: float
    error: Optional[str] = None
    metadata: dict = field(default_factory=dict)

    @property
    def summary(self) -> str:
        status = "OK" if self.success else "FALHA"
        return (
            f"[{status}] {self.vdp.produto} — "
            f"{self.attempts} tentativa(s), {self.elapsed_seconds:.1f}s"
        )


class NB2Engine:
    """
    Motor de geração NB2.

    Integra VDP loader, prompt builder, Gemini client e output manager
    em um fluxo coeso de geração de imagens product-in-scene.
    """

    def __init__(
        self,
        config: PipelineConfig,
        gemini_client: GeminiClient,
        output_manager: OutputManager,
    ) -> None:
        self._config = config
        self._client = gemini_client
        self._output = output_manager
        self._vdp_loader = VDPLoader()
        self._prompt_builder = PromptBuilder()

    def generate_from_vdp(
        self,
        vdp_path: Path,
        *,
        max_attempts: Optional[int] = None,
        output_subdir: str = "",
    ) -> GenerationResult:
        """
        Gera imagem NB2 a partir de um arquivo VDP.

        Args:
            vdp_path: Caminho para o arquivo .md do VDP.
            max_attempts: Máximo de tentativas (default da config).
            output_subdir: Subdiretório de output.

        Returns:
            GenerationResult com imagem e metadados.
        """
        max_attempts = max_attempts or self._config.nb2.max_generation_attempts
        start = time.monotonic()

        vdp = self._vdp_loader.load(vdp_path)
        product_path = self._resolve_product_image(vdp)
        prompt = self._prompt_builder.from_vdp_prompt(vdp.prompt_nb2)

        logger.info(
            "Iniciando NB2: %s | PNG: %s | Prompt: %d chars",
            vdp.produto,
            product_path.name,
            len(prompt),
        )

        uploaded_ref = None
        last_error = None
        image = None

        for attempt in range(1, max_attempts + 1):
            try:
                logger.info("Tentativa %d/%d para %s", attempt, max_attempts, vdp.produto)

                if uploaded_ref is None:
                    uploaded_ref = self._client.upload_reference_image(product_path)

                image = self._client.generate_nb2_image(
                    product_image_path=product_path,
                    prompt=prompt,
                    uploaded_ref=uploaded_ref,
                )

                if self._config.nb2.save_intermediate and attempt > 1:
                    self._save_intermediate(image, vdp, attempt, output_subdir)

                break

            except GeminiGenerationError as e:
                last_error = str(e)
                logger.warning(
                    "Tentativa %d falhou para %s: %s",
                    attempt, vdp.produto, last_error,
                )
                if attempt < max_attempts:
                    time.sleep(self._config.gemini.retry_delay_seconds * attempt)

        elapsed = time.monotonic() - start

        if image is None:
            logger.error("Todas as tentativas falharam para %s: %s", vdp.produto, last_error)
            return GenerationResult(
                vdp=vdp,
                image=None,
                output_path=None,
                success=False,
                attempts=max_attempts,
                elapsed_seconds=elapsed,
                error=last_error,
            )

        output_path = self._output.save_nb2_image(
            image=image,
            vdp=vdp,
            subdir=output_subdir,
        )

        self._output.save_generation_metadata(
            vdp=vdp,
            output_path=output_path,
            attempts=attempt,
            elapsed=elapsed,
            prompt=prompt,
        )

        result = GenerationResult(
            vdp=vdp,
            image=image,
            output_path=output_path,
            success=True,
            attempts=attempt,
            elapsed_seconds=elapsed,
            metadata={
                "prompt_length": len(prompt),
                "image_size": f"{image.width}x{image.height}",
                "product_png": product_path.name,
            },
        )

        logger.info("NB2 concluído: %s", result.summary)
        return result

    def generate_batch(
        self,
        vdp_paths: list[Path],
        *,
        output_subdir: str = "",
        stop_on_failure: bool = False,
    ) -> list[GenerationResult]:
        """
        Gera batch de imagens NB2 a partir de múltiplos VDPs.

        Args:
            vdp_paths: Lista de caminhos para VDPs.
            output_subdir: Subdiretório de output.
            stop_on_failure: Se True, para no primeiro erro.

        Returns:
            Lista de GenerationResult.
        """
        results = []
        total = len(vdp_paths)

        logger.info("Iniciando batch NB2: %d VDPs", total)

        for i, vdp_path in enumerate(vdp_paths, 1):
            logger.info("--- Batch %d/%d ---", i, total)

            result = self.generate_from_vdp(
                vdp_path,
                output_subdir=output_subdir,
            )
            results.append(result)

            if not result.success and stop_on_failure:
                logger.error("Batch interrompido por falha em %s", result.vdp.produto)
                break

        successes = sum(1 for r in results if r.success)
        logger.info(
            "Batch concluído: %d/%d sucesso, %d falhas",
            successes, total, total - successes,
        )

        return results

    def _resolve_product_image(self, vdp: VDPSpec) -> Path:
        """
        Resolve o caminho completo do PNG do produto.

        Tenta:
        1. Caminho relativo ao projeto (como especificado no VDP)
        2. Busca em assets_dir/imagem_produtos/
        """
        if vdp.png_referencia:
            # Caminho relativo ao projeto
            full_path = self._config.project_root / vdp.png_referencia
            if full_path.exists():
                return full_path

            # Caminho relativo ao assets_dir
            full_path = self._config.assets_dir / Path(vdp.png_referencia).name
            if full_path.exists():
                return full_path

            # Busca recursiva em product_images_dir
            product_images = self._config.product_images_dir
            if product_images.exists():
                target_name = Path(vdp.png_referencia).name
                for img_file in product_images.rglob(target_name):
                    return img_file

        raise FileNotFoundError(
            f"PNG do produto não encontrado: {vdp.png_referencia}. "
            f"Verificar em: {self._config.product_images_dir}"
        )

    def _save_intermediate(
        self,
        image: Image.Image,
        vdp: VDPSpec,
        attempt: int,
        subdir: str,
    ) -> None:
        """Salva imagem intermediária para análise de iterações."""
        try:
            self._output.save_nb2_image(
                image=image,
                vdp=vdp,
                subdir=subdir,
                suffix=f"_attempt{attempt}",
            )
        except Exception as e:
            logger.warning("Falha ao salvar intermediário: %s", e)
