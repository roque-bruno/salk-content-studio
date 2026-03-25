"""
Configuração centralizada do Content Pipeline.

Carrega variáveis de ambiente e define defaults para todos os módulos.
"""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

from dotenv import load_dotenv


def _find_project_root() -> Path:
    """Resolve a raiz do projeto subindo até encontrar pyproject.toml ou .git."""
    current = Path(__file__).resolve()
    for parent in current.parents:
        if (parent / "pyproject.toml").exists() or (parent / ".git").exists():
            return parent
    return Path.cwd()


@dataclass(frozen=True)
class GeminiConfig:
    """Configuração do Google Gemini API."""

    api_key: str
    model: str = "gemini-2.0-flash-exp"
    image_model: str = "gemini-2.0-flash-exp"
    max_output_tokens: int = 8192
    temperature: float = 0.4
    top_p: float = 0.95
    top_k: int = 40
    timeout_seconds: int = 120
    max_retries: int = 3
    retry_delay_seconds: float = 2.0


@dataclass(frozen=True)
class NB2Config:
    """Configuração da geração NB2 (product-in-scene)."""

    default_width: int = 1080
    default_height: int = 1350
    default_aspect_ratio: str = "4:5"
    max_generation_attempts: int = 3
    save_intermediate: bool = True
    output_format: str = "png"
    output_quality: int = 95


@dataclass(frozen=True)
class PipelineConfig:
    """Configuração geral do pipeline."""

    project_root: Path
    assets_dir: Path
    output_dir: Path
    vdp_dir: Path
    logs_dir: Path
    gemini: GeminiConfig
    nb2: NB2Config
    batch_size: int = 5
    parallel_workers: int = 2
    log_level: str = "INFO"

    @property
    def product_images_dir(self) -> Path:
        return self.assets_dir / "imagem_produtos"

    @property
    def logos_dir(self) -> Path:
        return self.assets_dir / "logos"


def load_config(env_file: Optional[str] = None) -> PipelineConfig:
    """
    Carrega configuração completa a partir de variáveis de ambiente.

    Args:
        env_file: Caminho para arquivo .env (opcional, auto-detecta se omitido).

    Returns:
        PipelineConfig configurado e validado.

    Raises:
        ValueError: Se GOOGLE_API_KEY não estiver definida.
    """
    project_root = _find_project_root()

    if env_file:
        load_dotenv(env_file)
    else:
        for candidate in [project_root / ".env", Path.cwd() / ".env"]:
            if candidate.exists():
                load_dotenv(candidate)
                break

    api_key = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY", "")
    if not api_key:
        raise ValueError(
            "GOOGLE_API_KEY ou GEMINI_API_KEY deve estar definida. "
            "Adicione ao arquivo .env ou exporte como variável de ambiente."
        )

    gemini = GeminiConfig(
        api_key=api_key,
        model=os.getenv("GEMINI_MODEL", "gemini-2.0-flash-exp"),
        image_model=os.getenv("GEMINI_IMAGE_MODEL", "gemini-2.0-flash-exp"),
        max_output_tokens=int(os.getenv("GEMINI_MAX_TOKENS", "8192")),
        temperature=float(os.getenv("GEMINI_TEMPERATURE", "0.4")),
        timeout_seconds=int(os.getenv("GEMINI_TIMEOUT", "120")),
        max_retries=int(os.getenv("GEMINI_MAX_RETRIES", "3")),
    )

    nb2 = NB2Config(
        default_width=int(os.getenv("NB2_WIDTH", "1080")),
        default_height=int(os.getenv("NB2_HEIGHT", "1350")),
        max_generation_attempts=int(os.getenv("NB2_MAX_ATTEMPTS", "3")),
        save_intermediate=os.getenv("NB2_SAVE_INTERMEDIATE", "true").lower() == "true",
    )

    output_base = Path(os.getenv("OUTPUT_DIR", str(project_root / "output")))

    return PipelineConfig(
        project_root=project_root,
        assets_dir=Path(
            os.getenv("ASSETS_DIR", str(project_root / "docs_user"))
        ),
        output_dir=output_base,
        vdp_dir=Path(
            os.getenv(
                "VDP_DIR",
                str(project_root / "squads" / "content-production" / "output"),
            )
        ),
        logs_dir=output_base / "logs",
        gemini=gemini,
        nb2=nb2,
        batch_size=int(os.getenv("BATCH_SIZE", "5")),
        parallel_workers=int(os.getenv("PARALLEL_WORKERS", "2")),
        log_level=os.getenv("LOG_LEVEL", "INFO"),
    )
