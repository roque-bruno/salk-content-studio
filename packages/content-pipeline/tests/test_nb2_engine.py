"""Testes do NB2 Engine — fluxo completo com mock do Gemini."""

from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest
from PIL import Image

from content_pipeline.config import GeminiConfig, NB2Config, PipelineConfig
from content_pipeline.nb2.engine import GenerationResult, NB2Engine
from content_pipeline.output.manager import OutputManager


@pytest.fixture
def pipeline_config(project_root):
    return PipelineConfig(
        project_root=project_root,
        assets_dir=project_root / "docs_user",
        output_dir=project_root / "output",
        vdp_dir=project_root / "squads" / "content-production" / "output",
        logs_dir=project_root / "output" / "logs",
        gemini=GeminiConfig(api_key="test-key"),
        nb2=NB2Config(max_generation_attempts=2, save_intermediate=True),
    )


@pytest.fixture
def mock_client(mock_generated_image):
    client = MagicMock()
    client.upload_reference_image.return_value = MagicMock(name="ref-uploaded")
    client.generate_nb2_image.return_value = mock_generated_image
    return client


@pytest.fixture
def engine(pipeline_config, mock_client):
    output_manager = OutputManager(base_dir=pipeline_config.output_dir)
    return NB2Engine(
        config=pipeline_config,
        gemini_client=mock_client,
        output_manager=output_manager,
    )


class TestGenerateFromVDP:
    def test_success(self, engine, sample_vdp_file, sample_product_png):
        result = engine.generate_from_vdp(sample_vdp_file)

        assert result.success is True
        assert result.image is not None
        assert result.output_path is not None
        assert result.output_path.exists()
        assert result.attempts == 1
        assert result.elapsed_seconds > 0
        assert result.error is None

    def test_result_summary(self, engine, sample_vdp_file, sample_product_png):
        result = engine.generate_from_vdp(sample_vdp_file)
        assert "[OK]" in result.summary
        assert "LEV" in result.summary

    def test_saves_metadata_json(self, engine, sample_vdp_file, sample_product_png):
        result = engine.generate_from_vdp(sample_vdp_file)
        meta_path = result.output_path.with_suffix(".meta.json")
        assert meta_path.exists()

    def test_output_subdir(self, engine, sample_vdp_file, sample_product_png):
        result = engine.generate_from_vdp(sample_vdp_file, output_subdir="calibracao")
        assert "calibracao" in str(result.output_path)

    def test_failure_returns_error(self, engine, sample_vdp_file, sample_product_png, mock_client):
        from content_pipeline.api.gemini_client import GeminiGenerationError

        mock_client.generate_nb2_image.side_effect = GeminiGenerationError("Safety filter")

        result = engine.generate_from_vdp(sample_vdp_file)

        assert result.success is False
        assert result.image is None
        assert result.output_path is None
        assert "Safety filter" in result.error
        assert result.attempts == 2  # max_generation_attempts

    def test_missing_png_raises(self, engine, project_root):
        vdp_content = """# VDP Test
**Produto:** Produto Inexistente
**PNG de Referencia:** `docs_user/imagem_produtos/missing.png`

## 1. Prompt NB2

```
Place this product in scene. No text, no logos.
```
"""
        vdp_path = project_root / "squads" / "content-production" / "output" / "calibracao" / "missing.md"
        vdp_path.write_text(vdp_content, encoding="utf-8")

        with pytest.raises(FileNotFoundError, match="missing.png"):
            engine.generate_from_vdp(vdp_path)


class TestGenerateBatch:
    def test_batch_all_success(self, engine, project_root, sample_product_png, sample_vdp_content):
        cal_dir = project_root / "squads" / "content-production" / "output" / "calibracao"

        for i in range(3):
            vdp = cal_dir / f"hero-test-{i}.md"
            vdp.write_text(sample_vdp_content, encoding="utf-8")

        vdp_paths = sorted(cal_dir.glob("*.md"))
        results = engine.generate_batch(vdp_paths, output_subdir="batch-test")

        assert len(results) == 3
        assert all(r.success for r in results)

    def test_batch_partial_failure(self, engine, project_root, sample_product_png, sample_vdp_content, mock_client):
        from content_pipeline.api.gemini_client import GeminiGenerationError

        cal_dir = project_root / "squads" / "content-production" / "output" / "calibracao"

        for i in range(3):
            vdp = cal_dir / f"hero-batch-{i}.md"
            vdp.write_text(sample_vdp_content, encoding="utf-8")

        call_count = 0
        original_image = mock_client.generate_nb2_image.return_value

        def fail_on_second(*args, **kwargs):
            nonlocal call_count
            call_count += 1
            if 3 <= call_count <= 4:  # Second VDP (attempts 1-2)
                raise GeminiGenerationError("Blocked")
            return original_image

        mock_client.generate_nb2_image.side_effect = fail_on_second

        vdp_paths = sorted(cal_dir.glob("*.md"))
        results = engine.generate_batch(vdp_paths)

        successes = sum(1 for r in results if r.success)
        failures = sum(1 for r in results if not r.success)
        assert successes == 2
        assert failures == 1

    def test_batch_stop_on_failure(self, engine, project_root, sample_product_png, sample_vdp_content, mock_client):
        from content_pipeline.api.gemini_client import GeminiGenerationError

        cal_dir = project_root / "squads" / "content-production" / "output" / "calibracao"

        for i in range(3):
            vdp = cal_dir / f"hero-stop-{i}.md"
            vdp.write_text(sample_vdp_content, encoding="utf-8")

        mock_client.generate_nb2_image.side_effect = GeminiGenerationError("Blocked")

        vdp_paths = sorted(cal_dir.glob("*.md"))
        results = engine.generate_batch(vdp_paths, stop_on_failure=True)

        assert len(results) == 1
        assert results[0].success is False


class TestGenerationResult:
    def test_success_summary(self):
        vdp = MagicMock()
        vdp.produto = "LEV 4LEV"
        result = GenerationResult(
            vdp=vdp, image=MagicMock(), output_path=Path("/out.png"),
            success=True, attempts=1, elapsed_seconds=12.5,
        )
        assert "[OK]" in result.summary
        assert "LEV 4LEV" in result.summary

    def test_failure_summary(self):
        vdp = MagicMock()
        vdp.produto = "KRATUS"
        result = GenerationResult(
            vdp=vdp, image=None, output_path=None,
            success=False, attempts=3, elapsed_seconds=45.0,
            error="Safety filter",
        )
        assert "[FALHA]" in result.summary
        assert "KRATUS" in result.summary
