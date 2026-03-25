"""Testes do Pipeline Orchestrator — fluxo completo com mock."""

from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest
from PIL import Image

from content_pipeline.config import GeminiConfig, NB2Config, PipelineConfig
from content_pipeline.pipeline.orchestrator import (
    BatchRun,
    JobStatus,
    PipelineOrchestrator,
    PipelineStage,
)


@pytest.fixture
def pipeline_config(project_root):
    return PipelineConfig(
        project_root=project_root,
        assets_dir=project_root / "docs_user",
        output_dir=project_root / "output",
        vdp_dir=project_root / "squads" / "content-production" / "output",
        logs_dir=project_root / "output" / "logs",
        gemini=GeminiConfig(api_key="test-key"),
        nb2=NB2Config(),
    )


@pytest.fixture
def mock_orchestrator(pipeline_config, mock_generated_image):
    """Orchestrator com Gemini mockado."""
    with patch("content_pipeline.pipeline.orchestrator.GeminiClient") as MockClient:
        instance = MockClient.return_value
        instance.upload_reference_image.return_value = MagicMock(name="ref")
        instance.generate_nb2_image.return_value = mock_generated_image
        instance.cleanup_uploaded_files.return_value = None

        orchestrator = PipelineOrchestrator(pipeline_config)
        yield orchestrator


class TestRunSingle:
    def test_generates_single_image(self, mock_orchestrator, sample_vdp_file, sample_product_png):
        result = mock_orchestrator.run_single(sample_vdp_file)
        assert result.success is True
        assert result.output_path.exists()

    def test_single_with_subdir(self, mock_orchestrator, sample_vdp_file, sample_product_png):
        result = mock_orchestrator.run_single(sample_vdp_file, output_subdir="test-run")
        assert "test-run" in str(result.output_path)


class TestRunCalibration:
    def test_calibration_batch(self, mock_orchestrator, project_root, sample_product_png, sample_vdp_content):
        cal_dir = project_root / "squads" / "content-production" / "output" / "calibracao"
        for name in ["hero-lev-v1.md", "hero-kratus-v1.md"]:
            (cal_dir / name).write_text(sample_vdp_content, encoding="utf-8")

        batch = mock_orchestrator.run_calibration()
        assert batch.total == 2
        assert batch.completed == 2
        assert batch.failed == 0
        assert batch.success_rate == 100.0
        assert "calibracao" in batch.batch_id

    def test_calibration_empty_dir(self, mock_orchestrator, project_root):
        batch = mock_orchestrator.run_calibration()
        assert batch.total == 0

    def test_calibration_custom_dir(self, mock_orchestrator, project_root, sample_product_png, sample_vdp_content):
        custom_dir = project_root / "custom_vdps"
        custom_dir.mkdir()
        (custom_dir / "test.md").write_text(sample_vdp_content, encoding="utf-8")

        batch = mock_orchestrator.run_calibration(vdp_dir=custom_dir)
        assert batch.total == 1


class TestRunBatch:
    def test_batch_execution(self, mock_orchestrator, project_root, sample_product_png, sample_vdp_content):
        batch_dir = project_root / "batch_vdps"
        batch_dir.mkdir()
        for i in range(3):
            (batch_dir / f"piece-{i}.md").write_text(sample_vdp_content, encoding="utf-8")

        batch = mock_orchestrator.run_batch(batch_dir, batch_id="batch-001")
        assert batch.batch_id == "batch-001"
        assert batch.total == 3
        assert batch.completed == 3

    def test_batch_auto_id(self, mock_orchestrator, project_root, sample_product_png, sample_vdp_content):
        batch_dir = project_root / "auto_batch"
        batch_dir.mkdir()
        (batch_dir / "single.md").write_text(sample_vdp_content, encoding="utf-8")

        batch = mock_orchestrator.run_batch(batch_dir)
        assert batch.batch_id.startswith("batch_")


class TestBatchRun:
    def test_metrics(self):
        batch = BatchRun(batch_id="test")
        batch.jobs = [
            MagicMock(status=JobStatus.COMPLETED),
            MagicMock(status=JobStatus.COMPLETED),
            MagicMock(status=JobStatus.FAILED),
        ]
        assert batch.total == 3
        assert batch.completed == 2
        assert batch.failed == 1
        assert batch.success_rate == pytest.approx(66.7, abs=0.1)

    def test_empty_batch(self):
        batch = BatchRun(batch_id="empty")
        assert batch.total == 0
        assert batch.success_rate == 0.0


class TestCleanup:
    def test_cleanup_calls_client(self, mock_orchestrator):
        mock_orchestrator.cleanup()
        mock_orchestrator._client.cleanup_uploaded_files.assert_called_once()


class TestPipelineStage:
    def test_stages(self):
        assert PipelineStage.VISUAL_DESIGN.value == "visual-design"
        assert PipelineStage.COMPOSITION.value == "composition"
        assert PipelineStage.REVIEW.value == "review"
