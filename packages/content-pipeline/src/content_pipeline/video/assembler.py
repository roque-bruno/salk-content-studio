"""
Video Assembler — Worker deterministico para montagem de video.

Combina: clip Kling + narracao ElevenLabs + musica de fundo + legendas.
Usa FFmpeg como engine (deve estar no PATH).

Pipeline: hero_shot.mp4 + narration.mp3 + bgm.mp3 → final.mp4
"""

from __future__ import annotations

import logging
import shutil
import subprocess
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

logger = logging.getLogger(__name__)


@dataclass
class AssemblyResult:
    """Resultado da montagem de video."""
    success: bool
    output_path: str = ""
    duration_seconds: float = 0
    file_size_mb: float = 0
    elapsed_seconds: float = 0
    error: str = ""

    def to_dict(self) -> dict:
        return {
            "success": self.success,
            "output_path": self.output_path,
            "duration_seconds": round(self.duration_seconds, 1),
            "file_size_mb": round(self.file_size_mb, 2),
            "elapsed_seconds": round(self.elapsed_seconds, 1),
            "error": self.error,
        }


class VideoAssembler:
    """Montagem de video com FFmpeg."""

    def __init__(self, output_dir: Optional[Path] = None) -> None:
        self.output_dir = output_dir or Path("output/video/final")
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self._ffmpeg = shutil.which("ffmpeg")

    @property
    def available(self) -> bool:
        return self._ffmpeg is not None

    def assemble(
        self,
        video_path: str | Path,
        narration_path: Optional[str | Path] = None,
        bgm_path: Optional[str | Path] = None,
        subtitle_text: Optional[str] = None,
        output_name: Optional[str] = None,
        bgm_volume: float = 0.15,
        fade_in: float = 0.5,
        fade_out: float = 1.0,
    ) -> AssemblyResult:
        """
        Monta video final combinando clip + narração + musica + legendas.

        Args:
            video_path: Video base (Kling output)
            narration_path: Audio de narracao (ElevenLabs)
            bgm_path: Musica de fundo (opcional)
            subtitle_text: Texto para legendas burn-in (opcional)
            output_name: Nome do arquivo de saida
            bgm_volume: Volume da musica de fundo (0-1)
            fade_in: Fade in em segundos
            fade_out: Fade out em segundos

        Returns:
            AssemblyResult com output_path
        """
        if not self.available:
            return AssemblyResult(success=False, error="FFmpeg nao encontrado no PATH")

        video_path = Path(video_path)
        if not video_path.exists():
            return AssemblyResult(success=False, error=f"Video nao encontrado: {video_path}")

        if output_name is None:
            output_name = f"final_{video_path.stem}_{int(time.time())}.mp4"
        output_path = self.output_dir / output_name

        start = time.monotonic()

        try:
            if narration_path and bgm_path:
                self._assemble_full(
                    video_path, Path(narration_path), Path(bgm_path),
                    output_path, bgm_volume, fade_in, fade_out,
                )
            elif narration_path:
                self._assemble_with_narration(
                    video_path, Path(narration_path), output_path, fade_in, fade_out,
                )
            elif bgm_path:
                self._assemble_with_bgm(
                    video_path, Path(bgm_path), output_path, bgm_volume,
                )
            else:
                # Apenas processar video (fade in/out)
                self._process_video_only(video_path, output_path, fade_in, fade_out)

            # Burn-in subtitles se fornecido
            if subtitle_text and output_path.exists():
                self._burn_subtitles(output_path, subtitle_text)

            elapsed = time.monotonic() - start

            if not output_path.exists():
                return AssemblyResult(success=False, elapsed_seconds=elapsed, error="Output nao gerado")

            # Obter duracao e tamanho
            duration = self._get_duration(output_path)
            size_mb = output_path.stat().st_size / (1024 * 1024)

            return AssemblyResult(
                success=True,
                output_path=str(output_path),
                duration_seconds=duration,
                file_size_mb=size_mb,
                elapsed_seconds=elapsed,
            )

        except Exception as e:
            logger.error("Video assembly failed: %s", e)
            return AssemblyResult(
                success=False,
                elapsed_seconds=time.monotonic() - start,
                error=str(e),
            )

    # ------------------------------------------------------------------
    # FFmpeg commands
    # ------------------------------------------------------------------

    def _assemble_full(
        self, video: Path, narration: Path, bgm: Path,
        output: Path, bgm_vol: float, fade_in: float, fade_out: float,
    ) -> None:
        """Video + narracao + musica de fundo."""
        cmd = [
            self._ffmpeg, "-y",
            "-i", str(video),
            "-i", str(narration),
            "-i", str(bgm),
            "-filter_complex",
            f"[2:a]volume={bgm_vol}[bgm];"
            f"[1:a][bgm]amix=inputs=2:duration=first[aout];"
            f"[0:v]fade=t=in:st=0:d={fade_in},fade=t=out:st=end:d={fade_out}[vout]",
            "-map", "[vout]",
            "-map", "[aout]",
            "-c:v", "libx264", "-preset", "medium", "-crf", "23",
            "-c:a", "aac", "-b:a", "192k",
            "-movflags", "+faststart",
            str(output),
        ]
        self._run(cmd)

    def _assemble_with_narration(
        self, video: Path, narration: Path, output: Path,
        fade_in: float, fade_out: float,
    ) -> None:
        """Video + narracao (sem BGM)."""
        cmd = [
            self._ffmpeg, "-y",
            "-i", str(video),
            "-i", str(narration),
            "-filter_complex",
            f"[0:v]fade=t=in:st=0:d={fade_in},fade=t=out:st=end:d={fade_out}[vout]",
            "-map", "[vout]",
            "-map", "1:a",
            "-c:v", "libx264", "-preset", "medium", "-crf", "23",
            "-c:a", "aac", "-b:a", "192k",
            "-shortest",
            "-movflags", "+faststart",
            str(output),
        ]
        self._run(cmd)

    def _assemble_with_bgm(
        self, video: Path, bgm: Path, output: Path, bgm_vol: float,
    ) -> None:
        """Video + musica de fundo (sem narracao)."""
        cmd = [
            self._ffmpeg, "-y",
            "-i", str(video),
            "-i", str(bgm),
            "-filter_complex",
            f"[1:a]volume={bgm_vol}[bgm]",
            "-map", "0:v",
            "-map", "[bgm]",
            "-c:v", "copy",
            "-c:a", "aac", "-b:a", "192k",
            "-shortest",
            "-movflags", "+faststart",
            str(output),
        ]
        self._run(cmd)

    def _process_video_only(
        self, video: Path, output: Path, fade_in: float, fade_out: float,
    ) -> None:
        """Apenas aplicar fades no video."""
        cmd = [
            self._ffmpeg, "-y",
            "-i", str(video),
            "-vf", f"fade=t=in:st=0:d={fade_in},fade=t=out:st=end:d={fade_out}",
            "-c:v", "libx264", "-preset", "medium", "-crf", "23",
            "-c:a", "copy",
            "-movflags", "+faststart",
            str(output),
        ]
        self._run(cmd)

    def _burn_subtitles(self, video_path: Path, text: str) -> None:
        """Burn-in subtitles diretamente no video."""
        # Criar arquivo SRT temporario
        srt_path = video_path.with_suffix(".srt")
        duration = self._get_duration(video_path)
        h, m, s = 0, 0, int(duration)
        srt_content = f"1\n00:00:00,000 --> 00:{m:02d}:{s:02d},000\n{text}\n"
        srt_path.write_text(srt_content, encoding="utf-8")

        temp_output = video_path.with_name(f"sub_{video_path.name}")
        cmd = [
            self._ffmpeg, "-y",
            "-i", str(video_path),
            "-vf", f"subtitles={str(srt_path).replace(chr(92), '/')}:force_style='FontSize=18,PrimaryColour=&Hffffff&'",
            "-c:v", "libx264", "-preset", "medium", "-crf", "23",
            "-c:a", "copy",
            str(temp_output),
        ]
        try:
            self._run(cmd)
            if temp_output.exists():
                temp_output.replace(video_path)
        finally:
            srt_path.unlink(missing_ok=True)
            temp_output.unlink(missing_ok=True)

    def _get_duration(self, path: Path) -> float:
        """Obtem duracao do video em segundos."""
        try:
            ffprobe = shutil.which("ffprobe")
            if not ffprobe:
                return 0
            result = subprocess.run(
                [ffprobe, "-v", "error", "-show_entries", "format=duration",
                 "-of", "default=noprint_wrappers=1:nokey=1", str(path)],
                capture_output=True, text=True, timeout=10,
            )
            return float(result.stdout.strip())
        except Exception:
            return 0

    def _run(self, cmd: list[str]) -> None:
        """Executa comando FFmpeg."""
        logger.info("FFmpeg: %s", " ".join(cmd[:6]) + "...")
        result = subprocess.run(
            cmd, capture_output=True, text=True, timeout=300,
        )
        if result.returncode != 0:
            raise RuntimeError(f"FFmpeg error: {result.stderr[:500]}")
