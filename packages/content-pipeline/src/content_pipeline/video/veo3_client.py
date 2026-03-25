"""
Google Veo 3 — API client para Text-to-Video e Image-to-Video.

Veo 3 é o modelo de vídeo do Google DeepMind, acessível via Vertex AI
ou via API Gemini (generateContent com modelos de vídeo).

Pipeline: prompt (+ imagem opcional) → Veo 3 gera → video MP4.

Modos suportados:
  - Text-to-Video (T2V): gera vídeo a partir de prompt textual
  - Image-to-Video (I2V): gera vídeo a partir de imagem + prompt

Custo estimado: variável por resolução/duração (Vertex AI billing).

Uso:
    client = Veo3Client(api_key="...")
    result = await client.text_to_video(
        prompt="Camera orbits a modern surgical light in a sterile OR",
        duration=5,
    )
    result = await client.image_to_video(
        image_path="hero_lev.png",
        prompt="Slow orbit around the product",
        duration=5,
    )
"""

from __future__ import annotations

import asyncio
import base64
import logging
import os
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

import httpx

logger = logging.getLogger(__name__)

# Custo estimado (Vertex AI pricing varia, usar estimativa conservadora)
COST_PER_SECOND_720P = 0.05   # USD
COST_PER_SECOND_1080P = 0.10  # USD

RESOLUTION_COSTS = {
    "720p": COST_PER_SECOND_720P,
    "1080p": COST_PER_SECOND_1080P,
}


@dataclass
class Veo3Result:
    """Resultado de uma geração de vídeo Veo 3."""
    success: bool
    video_url: str = ""
    video_path: str = ""
    duration_seconds: float = 0
    cost_usd: float = 0
    elapsed_seconds: float = 0
    operation_name: str = ""
    model: str = "veo-3.0-generate-preview"
    error: str = ""
    preview_mode: bool = False

    def to_dict(self) -> dict:
        return {
            "success": self.success,
            "video_url": self.video_url,
            "video_path": self.video_path,
            "duration_seconds": self.duration_seconds,
            "cost_usd": round(self.cost_usd, 4),
            "elapsed_seconds": round(self.elapsed_seconds, 1),
            "operation_name": self.operation_name,
            "model": self.model,
            "error": self.error,
            "preview_mode": self.preview_mode,
            "provider": "veo3",
        }


class Veo3Client:
    """
    Cliente para Google Veo 3 via Gemini API / Vertex AI.

    Suporta dois modos de acesso:
    1. Gemini API (api key simples) — endpoint generativelanguage.googleapis.com
    2. Vertex AI (service account) — endpoint us-central1-aiplatform.googleapis.com

    O modo é detectado automaticamente pela presença das env vars.
    """

    # Gemini API endpoint (modo simplificado com API key)
    GEMINI_BASE = "https://generativelanguage.googleapis.com/v1beta"

    # Vertex AI endpoint (modo enterprise)
    VERTEX_BASE = "https://us-central1-aiplatform.googleapis.com/v1"

    SUPPORTED_MODELS = {
        "veo-3.0-generate-preview": {
            "name": "Veo 3.0 Preview",
            "max_duration": 8,
            "resolutions": ["720p", "1080p"],
            "supports_i2v": True,
            "supports_audio": True,
        },
        "veo-2.0-generate-001": {
            "name": "Veo 2.0",
            "max_duration": 8,
            "resolutions": ["720p", "1080p"],
            "supports_i2v": True,
            "supports_audio": False,
        },
    }

    def __init__(
        self,
        api_key: Optional[str] = None,
        project_id: Optional[str] = None,
        location: str = "us-central1",
        output_dir: Optional[Path] = None,
        budget_tracker: Optional[object] = None,
    ) -> None:
        self.api_key = api_key or os.getenv("GOOGLE_API_KEY", "")
        self.project_id = project_id or os.getenv("GOOGLE_CLOUD_PROJECT", "")
        self.location = location
        self.output_dir = output_dir or Path("output/video/veo3")
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.budget_tracker = budget_tracker

        # Decidir modo de acesso
        self._use_vertex = bool(self.project_id)

    @property
    def configured(self) -> bool:
        return bool(self.api_key)

    @property
    def mode(self) -> str:
        if not self.configured:
            return "not_configured"
        return "vertex" if self._use_vertex else "gemini"

    async def text_to_video(
        self,
        prompt: str,
        duration: int = 5,
        aspect_ratio: str = "9:16",
        resolution: str = "720p",
        model: str = "veo-3.0-generate-preview",
        negative_prompt: str = "text, watermark, logo, blurry, distorted",
        generate_audio: bool = False,
        person_generation: str = "dont_allow",
    ) -> Veo3Result:
        """
        Gera vídeo a partir de texto (Text-to-Video).

        Args:
            prompt: Descrição do vídeo desejado
            duration: Duração em segundos (5-8)
            aspect_ratio: 16:9, 9:16, 1:1
            resolution: 720p ou 1080p
            model: Modelo Veo a usar
            negative_prompt: O que evitar na geração
            generate_audio: Gerar áudio nativo (apenas Veo 3.0)
            person_generation: dont_allow (seguro para B2B) ou allow_adult

        Returns:
            Veo3Result com video_path e metadados
        """
        if not self.configured:
            return Veo3Result(
                success=False,
                error="Veo 3 não configurado — GOOGLE_API_KEY ausente",
                preview_mode=True,
            )

        start = time.monotonic()

        try:
            # Construir request body
            full_prompt = prompt
            if negative_prompt:
                full_prompt = f"{prompt}. Avoid: {negative_prompt}"

            request_body = self._build_generate_request(
                prompt=full_prompt,
                image_b64=None,
                image_mime=None,
                duration=duration,
                aspect_ratio=aspect_ratio,
                model=model,
                generate_audio=generate_audio,
                person_generation=person_generation,
            )

            # Submeter geração (async long-running operation)
            operation_name = await self._submit_generation(request_body, model)

            if not operation_name:
                return Veo3Result(success=False, error="Falha ao submeter geração")

            # Poll até completar
            video_data = await self._poll_operation(operation_name, timeout=600)

            if not video_data:
                return Veo3Result(
                    success=False,
                    operation_name=operation_name,
                    error="Timeout esperando geração do vídeo (10min)",
                )

            # Salvar vídeo
            video_path = await self._save_video(video_data, operation_name)
            elapsed = time.monotonic() - start
            cost = duration * RESOLUTION_COSTS.get(resolution, COST_PER_SECOND_720P)

            # Registrar custo
            if self.budget_tracker and hasattr(self.budget_tracker, "record"):
                self.budget_tracker.record("video_veo3", cost, {
                    "operation": operation_name,
                    "duration": duration,
                    "model": model,
                    "resolution": resolution,
                })

            return Veo3Result(
                success=True,
                video_path=str(video_path),
                duration_seconds=duration,
                cost_usd=cost,
                elapsed_seconds=elapsed,
                operation_name=operation_name,
                model=model,
            )

        except Exception as e:
            elapsed = time.monotonic() - start
            logger.error("Veo 3 generation failed: %s", e)
            return Veo3Result(
                success=False,
                elapsed_seconds=elapsed,
                error=str(e),
            )

    async def image_to_video(
        self,
        image_path: str | Path,
        prompt: str,
        duration: int = 5,
        aspect_ratio: str = "9:16",
        resolution: str = "720p",
        model: str = "veo-3.0-generate-preview",
        negative_prompt: str = "text, watermark, logo, blurry, distorted",
        generate_audio: bool = False,
    ) -> Veo3Result:
        """
        Gera vídeo a partir de imagem + prompt (Image-to-Video).

        Args:
            image_path: Caminho da imagem PNG/JPG de entrada
            prompt: Descrição do movimento/animação desejado
            duration: Duração em segundos (5-8)

        Returns:
            Veo3Result com video_path e metadados
        """
        if not self.configured:
            return Veo3Result(
                success=False,
                error="Veo 3 não configurado — GOOGLE_API_KEY ausente",
                preview_mode=True,
            )

        image_path = Path(image_path)
        if not image_path.exists():
            return Veo3Result(success=False, error=f"Imagem não encontrada: {image_path}")

        model_info = self.SUPPORTED_MODELS.get(model, {})
        if not model_info.get("supports_i2v", False):
            return Veo3Result(success=False, error=f"Modelo {model} não suporta Image-to-Video")

        start = time.monotonic()

        try:
            # Encode imagem
            image_bytes = image_path.read_bytes()
            image_b64 = base64.b64encode(image_bytes).decode()
            suffix = image_path.suffix.lower()
            image_mime = "image/png" if suffix == ".png" else "image/jpeg"

            full_prompt = prompt
            if negative_prompt:
                full_prompt = f"{prompt}. Avoid: {negative_prompt}"

            request_body = self._build_generate_request(
                prompt=full_prompt,
                image_b64=image_b64,
                image_mime=image_mime,
                duration=duration,
                aspect_ratio=aspect_ratio,
                model=model,
                generate_audio=generate_audio,
                person_generation="dont_allow",
            )

            operation_name = await self._submit_generation(request_body, model)

            if not operation_name:
                return Veo3Result(success=False, error="Falha ao submeter geração I2V")

            video_data = await self._poll_operation(operation_name, timeout=600)

            if not video_data:
                return Veo3Result(
                    success=False,
                    operation_name=operation_name,
                    error="Timeout esperando geração do vídeo",
                )

            video_path = await self._save_video(video_data, operation_name)
            elapsed = time.monotonic() - start
            cost = duration * RESOLUTION_COSTS.get(resolution, COST_PER_SECOND_720P)

            if self.budget_tracker and hasattr(self.budget_tracker, "record"):
                self.budget_tracker.record("video_veo3", cost, {
                    "operation": operation_name,
                    "duration": duration,
                    "model": model,
                    "mode": "i2v",
                })

            return Veo3Result(
                success=True,
                video_path=str(video_path),
                duration_seconds=duration,
                cost_usd=cost,
                elapsed_seconds=elapsed,
                operation_name=operation_name,
                model=model,
            )

        except Exception as e:
            elapsed = time.monotonic() - start
            logger.error("Veo 3 I2V failed: %s", e)
            return Veo3Result(success=False, elapsed_seconds=elapsed, error=str(e))

    # ------------------------------------------------------------------
    # Internal
    # ------------------------------------------------------------------

    def _build_generate_request(
        self,
        prompt: str,
        image_b64: Optional[str],
        image_mime: Optional[str],
        duration: int,
        aspect_ratio: str,
        model: str,
        generate_audio: bool,
        person_generation: str = "dont_allow",
    ) -> dict:
        """Constrói o request body para a API de geração."""
        # Conteúdo do prompt
        parts = []

        if image_b64 and image_mime:
            parts.append({
                "inlineData": {
                    "mimeType": image_mime,
                    "data": image_b64,
                }
            })

        parts.append({"text": prompt})

        body = {
            "contents": [{"role": "user", "parts": parts}],
            "generationConfig": {
                "responseModalities": ["video"],
                "videoDuration": duration,
            },
            "safetySettings": [
                {
                    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                    "threshold": "BLOCK_LOW_AND_ABOVE",
                },
            ],
        }

        # Configurações específicas do Veo
        video_config = {}
        if aspect_ratio:
            video_config["aspectRatio"] = aspect_ratio
        if person_generation:
            video_config["personGeneration"] = person_generation
        if generate_audio and model == "veo-3.0-generate-preview":
            body["generationConfig"]["responseModalities"] = ["video", "audio"]

        if video_config:
            body["generationConfig"]["videoGenerationConfig"] = video_config

        return body

    def _get_endpoint(self, model: str) -> str:
        """Retorna endpoint correto baseado no modo de acesso."""
        if self._use_vertex:
            return (
                f"{self.VERTEX_BASE}/projects/{self.project_id}"
                f"/locations/{self.location}"
                f"/publishers/google/models/{model}:generateContent"
            )
        return f"{self.GEMINI_BASE}/models/{model}:generateContent"

    def _get_poll_endpoint(self, operation_name: str) -> str:
        """Retorna endpoint de polling."""
        if self._use_vertex:
            return f"{self.VERTEX_BASE}/{operation_name}"
        return f"{self.GEMINI_BASE}/{operation_name}"

    def _headers(self) -> dict:
        """Headers para as requisições."""
        if self._use_vertex:
            return {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            }
        return {"Content-Type": "application/json"}

    def _params(self) -> dict:
        """Query params (API key para modo Gemini)."""
        if not self._use_vertex:
            return {"key": self.api_key}
        return {}

    async def _submit_generation(self, request_body: dict, model: str) -> str:
        """Submete requisição de geração. Retorna operation name."""
        endpoint = self._get_endpoint(model)

        async with httpx.AsyncClient(timeout=60) as client:
            response = await client.post(
                endpoint,
                headers=self._headers(),
                params=self._params(),
                json=request_body,
            )
            response.raise_for_status()
            data = response.json()

            # Resposta pode ser síncrona (vídeo direto) ou assíncrona (operation)
            if "name" in data:
                # Long-running operation
                return data["name"]

            # Resposta direta (raro para vídeo, mas possível)
            candidates = data.get("candidates", [])
            if candidates:
                parts = candidates[0].get("content", {}).get("parts", [])
                for part in parts:
                    if "videoMetadata" in part or part.get("mimeType", "").startswith("video/"):
                        # Vídeo inline — salvar diretamente
                        return f"__direct__{id(data)}"

            return data.get("name", "")

    async def _poll_operation(
        self, operation_name: str, timeout: int = 600
    ) -> Optional[bytes]:
        """Faz polling de long-running operation. Retorna bytes do vídeo."""
        if operation_name.startswith("__direct__"):
            return None  # Tratado separadamente

        start = time.monotonic()
        poll_interval = 5

        async with httpx.AsyncClient(timeout=30) as client:
            while time.monotonic() - start < timeout:
                endpoint = self._get_poll_endpoint(operation_name)
                response = await client.get(
                    endpoint,
                    headers=self._headers(),
                    params=self._params(),
                )

                if response.status_code == 200:
                    data = response.json()

                    if data.get("done"):
                        # Operação concluída
                        result = data.get("response", data.get("result", {}))
                        candidates = result.get("candidates", [])

                        for candidate in candidates:
                            parts = candidate.get("content", {}).get("parts", [])
                            for part in parts:
                                # Vídeo inline (base64)
                                inline = part.get("inlineData", {})
                                if inline.get("mimeType", "").startswith("video/"):
                                    return base64.b64decode(inline["data"])

                                # File URI (precisa download)
                                file_uri = part.get("fileData", {}).get("fileUri", "")
                                if file_uri:
                                    return await self._download_from_uri(file_uri)

                        # Verificar erro
                        error = data.get("error", {})
                        if error:
                            logger.error("Veo 3 operation error: %s", error)
                            return None

                    elif data.get("error"):
                        logger.error("Veo 3 poll error: %s", data["error"])
                        return None

                await asyncio.sleep(poll_interval)
                poll_interval = min(poll_interval + 3, 20)

        return None

    async def _download_from_uri(self, file_uri: str) -> bytes:
        """Download de vídeo via File URI do Google."""
        async with httpx.AsyncClient(timeout=120) as client:
            if self._use_vertex:
                response = await client.get(
                    file_uri,
                    headers=self._headers(),
                )
            else:
                response = await client.get(
                    file_uri,
                    params=self._params(),
                )
            response.raise_for_status()
            return response.content

    async def _save_video(self, video_data: bytes, operation_name: str) -> Path:
        """Salva bytes de vídeo em arquivo MP4."""
        safe_name = operation_name.replace("/", "_").replace(":", "_")[-40:]
        output_path = self.output_dir / f"veo3_{safe_name}.mp4"
        output_path.write_bytes(video_data)
        logger.info("Veo 3 video saved: %s (%d bytes)", output_path, len(video_data))
        return output_path

    @classmethod
    def list_models(cls) -> list[dict]:
        """Lista modelos Veo disponíveis."""
        return [
            {
                "model_id": mid,
                "name": info["name"],
                "max_duration": info["max_duration"],
                "resolutions": info["resolutions"],
                "supports_i2v": info["supports_i2v"],
                "supports_audio": info["supports_audio"],
            }
            for mid, info in cls.SUPPORTED_MODELS.items()
        ]
