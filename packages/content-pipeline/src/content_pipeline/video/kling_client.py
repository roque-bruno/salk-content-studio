"""
Kling 3.0 Pro — API client para Image-to-Video (I2V).

Pipeline: NB2 hero shot (PNG) → Kling anima → video MP4 output.
Custo: $0.14/segundo de video.

Uso:
    client = KlingClient(api_key="...")
    result = await client.image_to_video(
        image_path="hero_lev.png",
        prompt="Camera slowly rotates around the surgical light",
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

COST_PER_SECOND = 0.14  # USD


@dataclass
class KlingResult:
    """Resultado de uma geracao de video."""
    success: bool
    video_url: str = ""
    video_path: str = ""
    duration_seconds: float = 0
    cost_usd: float = 0
    elapsed_seconds: float = 0
    task_id: str = ""
    error: str = ""

    def to_dict(self) -> dict:
        return {
            "success": self.success,
            "video_url": self.video_url,
            "video_path": self.video_path,
            "duration_seconds": self.duration_seconds,
            "cost_usd": round(self.cost_usd, 4),
            "elapsed_seconds": round(self.elapsed_seconds, 1),
            "task_id": self.task_id,
            "error": self.error,
        }


class KlingClient:
    """Cliente para Kling 3.0 Pro API."""

    BASE_URL = "https://api.klingai.com/v1"

    def __init__(
        self,
        api_key: Optional[str] = None,
        output_dir: Optional[Path] = None,
        budget_tracker: Optional[object] = None,
    ) -> None:
        self.api_key = api_key or os.getenv("KLING_API_KEY", "")
        self.output_dir = output_dir or Path("output/video")
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.budget_tracker = budget_tracker

    @property
    def configured(self) -> bool:
        return bool(self.api_key)

    async def image_to_video(
        self,
        image_path: str | Path,
        prompt: str,
        duration: int = 5,
        aspect_ratio: str = "9:16",
        model: str = "kling-v1-5",
        negative_prompt: str = "text, watermark, logo, blurry, distorted, low quality",
        cfg_scale: float = 0.5,
    ) -> KlingResult:
        """
        Gera video a partir de imagem (Image-to-Video).

        Args:
            image_path: Caminho da imagem PNG/JPG de entrada
            prompt: Descricao do movimento/animacao desejado
            duration: Duracao do video em segundos (5 ou 10)
            aspect_ratio: Aspecto (16:9, 9:16, 1:1)
            model: Modelo Kling (kling-v1-5)
            negative_prompt: O que evitar
            cfg_scale: Aderencia ao prompt (0-1)

        Returns:
            KlingResult com video_path e metadados
        """
        if not self.configured:
            return KlingResult(
                success=False,
                error="Kling API nao configurado — KLING_API_KEY ausente",
            )

        image_path = Path(image_path)
        if not image_path.exists():
            return KlingResult(success=False, error=f"Imagem nao encontrada: {image_path}")

        start = time.monotonic()

        try:
            # Encode imagem em base64
            image_b64 = base64.b64encode(image_path.read_bytes()).decode()
            image_type = "image/png" if image_path.suffix.lower() == ".png" else "image/jpeg"

            # Submeter tarefa
            task_id = await self._submit_task(
                image_b64=image_b64,
                image_type=image_type,
                prompt=prompt,
                duration=duration,
                aspect_ratio=aspect_ratio,
                model=model,
                negative_prompt=negative_prompt,
                cfg_scale=cfg_scale,
            )

            if not task_id:
                return KlingResult(success=False, error="Falha ao submeter tarefa")

            # Polling por resultado
            video_url = await self._poll_result(task_id, timeout=300)

            if not video_url:
                return KlingResult(
                    success=False,
                    task_id=task_id,
                    error="Timeout esperando geracao do video",
                )

            # Download do video
            video_path = await self._download_video(video_url, task_id)
            elapsed = time.monotonic() - start
            cost = duration * COST_PER_SECOND

            # Registrar custo
            if self.budget_tracker and hasattr(self.budget_tracker, "record"):
                self.budget_tracker.record("video_kling", cost, {
                    "task_id": task_id,
                    "duration": duration,
                    "model": model,
                })

            return KlingResult(
                success=True,
                video_url=video_url,
                video_path=str(video_path),
                duration_seconds=duration,
                cost_usd=cost,
                elapsed_seconds=elapsed,
                task_id=task_id,
            )

        except Exception as e:
            elapsed = time.monotonic() - start
            logger.error("Kling I2V failed: %s", e)
            return KlingResult(
                success=False,
                elapsed_seconds=elapsed,
                error=str(e),
            )

    async def text_to_video(
        self,
        prompt: str,
        duration: int = 5,
        aspect_ratio: str = "9:16",
    ) -> KlingResult:
        """Gera video a partir de texto (Text-to-Video). Menos usado que I2V."""
        if not self.configured:
            return KlingResult(
                success=False,
                error="Kling API nao configurado — KLING_API_KEY ausente",
            )

        start = time.monotonic()
        try:
            async with httpx.AsyncClient(timeout=30) as client:
                response = await client.post(
                    f"{self.BASE_URL}/videos/text2video",
                    headers=self._headers(),
                    json={
                        "prompt": prompt,
                        "duration": str(duration),
                        "aspect_ratio": aspect_ratio,
                        "negative_prompt": "text, watermark, blurry, distorted",
                    },
                )
                response.raise_for_status()
                data = response.json()
                task_id = data.get("data", {}).get("task_id", "")

            video_url = await self._poll_result(task_id, timeout=300)
            if not video_url:
                return KlingResult(success=False, task_id=task_id, error="Timeout")

            video_path = await self._download_video(video_url, task_id)
            elapsed = time.monotonic() - start
            cost = duration * COST_PER_SECOND

            if self.budget_tracker and hasattr(self.budget_tracker, "record"):
                self.budget_tracker.record("video_kling", cost, {"task_id": task_id, "duration": duration})

            return KlingResult(
                success=True, video_url=video_url, video_path=str(video_path),
                duration_seconds=duration, cost_usd=cost, elapsed_seconds=elapsed, task_id=task_id,
            )
        except Exception as e:
            return KlingResult(success=False, elapsed_seconds=time.monotonic() - start, error=str(e))

    # ------------------------------------------------------------------
    # Internal
    # ------------------------------------------------------------------

    def _headers(self) -> dict:
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

    async def _submit_task(self, **kwargs) -> str:
        """Submete tarefa I2V e retorna task_id."""
        async with httpx.AsyncClient(timeout=30) as client:
            response = await client.post(
                f"{self.BASE_URL}/videos/image2video",
                headers=self._headers(),
                json={
                    "model_name": kwargs.get("model", "kling-v1-5"),
                    "image": f"data:{kwargs['image_type']};base64,{kwargs['image_b64']}",
                    "prompt": kwargs.get("prompt", ""),
                    "negative_prompt": kwargs.get("negative_prompt", ""),
                    "duration": str(kwargs.get("duration", 5)),
                    "aspect_ratio": kwargs.get("aspect_ratio", "9:16"),
                    "cfg_scale": kwargs.get("cfg_scale", 0.5),
                },
            )
            response.raise_for_status()
            data = response.json()
            return data.get("data", {}).get("task_id", "")

    async def _poll_result(self, task_id: str, timeout: int = 300) -> str:
        """Faz polling ate o video estar pronto. Retorna URL ou string vazia."""
        start = time.monotonic()
        poll_interval = 5  # segundos

        async with httpx.AsyncClient(timeout=30) as client:
            while time.monotonic() - start < timeout:
                response = await client.get(
                    f"{self.BASE_URL}/videos/{task_id}",
                    headers=self._headers(),
                )
                if response.status_code == 200:
                    data = response.json()
                    status = data.get("data", {}).get("task_status", "")

                    if status == "succeed":
                        videos = data.get("data", {}).get("task_result", {}).get("videos", [])
                        if videos:
                            return videos[0].get("url", "")

                    elif status in ("failed", "cancelled"):
                        logger.error("Kling task %s: %s", task_id, status)
                        return ""

                await asyncio.sleep(poll_interval)
                poll_interval = min(poll_interval + 2, 15)

        return ""

    async def _download_video(self, url: str, task_id: str) -> Path:
        """Faz download do video gerado."""
        output_path = self.output_dir / f"kling_{task_id}.mp4"
        async with httpx.AsyncClient(timeout=120) as client:
            response = await client.get(url)
            response.raise_for_status()
            output_path.write_bytes(response.content)
        logger.info("Video downloaded: %s (%d bytes)", output_path, len(response.content))
        return output_path
