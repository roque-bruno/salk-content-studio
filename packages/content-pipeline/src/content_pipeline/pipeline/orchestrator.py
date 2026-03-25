"""
Pipeline Orchestrator — orquestração do fluxo completo de produção.

Coordena as 8 etapas do pipeline de conteúdo:
1. Briefing → 2. Research → 3. Copy → 4. Copy Review →
5. Visual Design (NB2) → 6. Composition → 7. Review → 8. Publish

Este módulo foca nas etapas automatizáveis via API:
- Geração NB2 (etapa 5)
- Preparação de metadados para composição (etapa 6)
- Validação de qualidade (etapa 7)
"""

from __future__ import annotations

import logging
import time
from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from pathlib import Path
from typing import Optional

from content_pipeline.api.gemini_client import GeminiClient
from content_pipeline.config import PipelineConfig, load_config
from content_pipeline.nb2.engine import GenerationResult, NB2Engine
from content_pipeline.output.manager import OutputManager

logger = logging.getLogger(__name__)


class PipelineStage(Enum):
    """Etapas do pipeline de produção."""

    BRIEFING = "briefing"
    RESEARCH = "research"
    COPY = "copy"
    COPY_REVIEW = "copy-review"
    VISUAL_DESIGN = "visual-design"
    COMPOSITION = "composition"
    REVIEW = "review"
    PUBLISH = "publish"


class JobStatus(Enum):
    """Status de um job de produção."""

    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    SKIPPED = "skipped"


@dataclass
class PipelineJob:
    """Um job individual no pipeline."""

    vdp_path: Path
    stage: PipelineStage = PipelineStage.VISUAL_DESIGN
    status: JobStatus = JobStatus.PENDING
    result: Optional[GenerationResult] = None
    started_at: Optional[str] = None
    completed_at: Optional[str] = None
    error: Optional[str] = None


@dataclass
class BatchRun:
    """Execução de um batch de produção."""

    batch_id: str
    jobs: list[PipelineJob] = field(default_factory=list)
    started_at: str = ""
    completed_at: str = ""

    @property
    def total(self) -> int:
        return len(self.jobs)

    @property
    def completed(self) -> int:
        return sum(1 for j in self.jobs if j.status == JobStatus.COMPLETED)

    @property
    def failed(self) -> int:
        return sum(1 for j in self.jobs if j.status == JobStatus.FAILED)

    @property
    def success_rate(self) -> float:
        if self.total == 0:
            return 0.0
        return self.completed / self.total * 100


class PipelineOrchestrator:
    """
    Orquestrador principal do pipeline de produção de conteúdo.

    Gerencia o fluxo de trabalho desde o carregamento de VDPs
    até a geração de imagens NB2 e preparação para composição.
    """

    def __init__(self, config: Optional[PipelineConfig] = None) -> None:
        self._config = config or load_config()
        self._output = OutputManager(
            base_dir=self._config.output_dir,
            quality=self._config.nb2.output_quality,
        )
        self._client = GeminiClient(self._config.gemini)
        self._engine = NB2Engine(
            config=self._config,
            gemini_client=self._client,
            output_manager=self._output,
        )

    def run_calibration(
        self,
        vdp_dir: Optional[Path] = None,
    ) -> BatchRun:
        """
        Executa calibração — gera hero shots dos VDPs de calibração.

        Fluxo:
        1. Carrega todos os VDPs do diretório de calibração
        2. Gera imagem NB2 para cada um
        3. Salva em output/nb2/calibracao/
        4. Retorna relatório do batch

        Args:
            vdp_dir: Diretório com VDPs de calibração.

        Returns:
            BatchRun com resultados de cada geração.
        """
        if vdp_dir is None:
            vdp_dir = self._config.vdp_dir / "calibracao"

        return self._run_batch(
            vdp_dir=vdp_dir,
            batch_id=f"calibracao_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}",
            output_subdir="calibracao",
        )

    def run_batch(
        self,
        vdp_dir: Path,
        batch_id: Optional[str] = None,
    ) -> BatchRun:
        """
        Executa batch de produção.

        Args:
            vdp_dir: Diretório com VDPs do batch.
            batch_id: Identificador do batch (auto-gerado se omitido).

        Returns:
            BatchRun com resultados.
        """
        if batch_id is None:
            batch_id = f"batch_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}"

        return self._run_batch(
            vdp_dir=vdp_dir,
            batch_id=batch_id,
            output_subdir=batch_id,
        )

    def run_single(
        self,
        vdp_path: Path,
        *,
        output_subdir: str = "",
    ) -> GenerationResult:
        """
        Gera uma única peça a partir de um VDP.

        Args:
            vdp_path: Caminho para o arquivo VDP.
            output_subdir: Subdiretório de output.

        Returns:
            GenerationResult com imagem e metadados.
        """
        return self._engine.generate_from_vdp(
            vdp_path,
            output_subdir=output_subdir,
        )

    def _run_batch(
        self,
        vdp_dir: Path,
        batch_id: str,
        output_subdir: str,
    ) -> BatchRun:
        """Execução interna de um batch."""
        batch = BatchRun(
            batch_id=batch_id,
            started_at=datetime.now(timezone.utc).isoformat(),
        )

        vdp_dir = Path(vdp_dir)
        if not vdp_dir.exists():
            logger.error("Diretório VDP não encontrado: %s", vdp_dir)
            return batch

        vdp_files = sorted(vdp_dir.glob("*.md"))
        if not vdp_files:
            logger.warning("Nenhum VDP encontrado em: %s", vdp_dir)
            return batch

        logger.info("=== BATCH %s ===", batch_id)
        logger.info("VDPs encontrados: %d", len(vdp_files))

        for vdp_path in vdp_files:
            job = PipelineJob(vdp_path=vdp_path)
            batch.jobs.append(job)

            job.status = JobStatus.RUNNING
            job.started_at = datetime.now(timezone.utc).isoformat()

            try:
                result = self._engine.generate_from_vdp(
                    vdp_path,
                    output_subdir=output_subdir,
                )
                job.result = result
                job.status = JobStatus.COMPLETED if result.success else JobStatus.FAILED
                job.error = result.error

            except Exception as e:
                job.status = JobStatus.FAILED
                job.error = str(e)
                logger.error("Job falhou para %s: %s", vdp_path.name, e)

            job.completed_at = datetime.now(timezone.utc).isoformat()

        batch.completed_at = datetime.now(timezone.utc).isoformat()

        self._output.append_production_log({
            "action": "batch_completed",
            "batch_id": batch_id,
            "total": batch.total,
            "completed": batch.completed,
            "failed": batch.failed,
            "success_rate": f"{batch.success_rate:.1f}%",
        })

        logger.info(
            "=== BATCH CONCLUÍDO: %d/%d sucesso (%.1f%%) ===",
            batch.completed, batch.total, batch.success_rate,
        )

        return batch

    def cleanup(self) -> None:
        """Limpa recursos temporários (uploaded files)."""
        self._client.cleanup_uploaded_files()
        logger.info("Cleanup concluído")
