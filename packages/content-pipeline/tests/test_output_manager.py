"""Testes do Output Manager — salvamento, naming, metadados."""

import json
from pathlib import Path

import pytest
from PIL import Image

from content_pipeline.nb2.vdp_loader import VDPLoader
from content_pipeline.output.manager import OutputManager


@pytest.fixture
def output_dir(tmp_path):
    return tmp_path / "output"


@pytest.fixture
def manager(output_dir):
    return OutputManager(base_dir=output_dir)


@pytest.fixture
def vdp_spec(sample_vdp_file):
    loader = VDPLoader()
    return loader.load(sample_vdp_file)


class TestSaveNB2Image:
    def test_creates_nb2_subdir(self, manager, output_dir, vdp_spec, mock_generated_image):
        manager.save_nb2_image(image=mock_generated_image, vdp=vdp_spec)
        assert (output_dir / "nb2").exists()

    def test_saves_png(self, manager, vdp_spec, mock_generated_image):
        path = manager.save_nb2_image(image=mock_generated_image, vdp=vdp_spec)
        assert path.exists()
        assert path.suffix == ".png"
        img = Image.open(path)
        assert img.size == (1080, 1350)

    def test_naming_convention(self, manager, vdp_spec, mock_generated_image):
        path = manager.save_nb2_image(image=mock_generated_image, vdp=vdp_spec)
        name = path.name
        assert "foco-cirurgico-lev-4lev-simplex-teto" in name
        assert "v1" in name
        assert name.endswith(".png")

    def test_subdir(self, manager, vdp_spec, mock_generated_image):
        path = manager.save_nb2_image(
            image=mock_generated_image, vdp=vdp_spec, subdir="calibracao"
        )
        assert "calibracao" in str(path)

    def test_suffix(self, manager, vdp_spec, mock_generated_image):
        path = manager.save_nb2_image(
            image=mock_generated_image, vdp=vdp_spec, suffix="_attempt2"
        )
        assert "_attempt2" in path.name

    def test_increments_counter(self, manager, vdp_spec, mock_generated_image):
        path1 = manager.save_nb2_image(image=mock_generated_image, vdp=vdp_spec)
        path2 = manager.save_nb2_image(image=mock_generated_image, vdp=vdp_spec)
        assert path1 != path2
        assert "_001" in path1.name
        assert "_002" in path2.name

    def test_rgba_image(self, manager, vdp_spec):
        rgba = Image.new("RGBA", (1080, 1350), (30, 30, 30, 255))
        path = manager.save_nb2_image(image=rgba, vdp=vdp_spec)
        assert path.exists()


class TestSaveMetadata:
    def test_creates_meta_json(self, manager, vdp_spec, mock_generated_image):
        img_path = manager.save_nb2_image(image=mock_generated_image, vdp=vdp_spec)
        meta_path = manager.save_generation_metadata(
            vdp=vdp_spec,
            output_path=img_path,
            attempts=2,
            elapsed=15.3,
            prompt="test prompt content",
        )
        assert meta_path.exists()
        assert meta_path.suffix == ".json"

    def test_meta_content(self, manager, vdp_spec, mock_generated_image):
        img_path = manager.save_nb2_image(image=mock_generated_image, vdp=vdp_spec)
        meta_path = manager.save_generation_metadata(
            vdp=vdp_spec,
            output_path=img_path,
            attempts=1,
            elapsed=8.5,
            prompt="Place this product in scene",
        )
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
        assert meta["vdp"]["produto"] == "Foco Cirurgico LEV 4LEV (Simplex Teto)"
        assert meta["vdp"]["marca"] == "Mendel Medical (conteudo tecnico)"
        assert meta["generation"]["attempts"] == 1
        assert meta["generation"]["elapsed_seconds"] == 8.5
        assert meta["generation"]["prompt_length"] == len("Place this product in scene")
        assert len(meta["claims"]) == 4
        assert meta["claims"][0]["id"] == "LEV-01"
        assert meta["canva"]["headline"] != ""
        assert meta["canva"]["logo"] != ""

    def test_meta_alongside_image(self, manager, vdp_spec, mock_generated_image):
        img_path = manager.save_nb2_image(image=mock_generated_image, vdp=vdp_spec)
        meta_path = manager.save_generation_metadata(
            vdp=vdp_spec, output_path=img_path, attempts=1, elapsed=5.0, prompt="x"
        )
        assert meta_path.parent == img_path.parent
        assert img_path.stem in meta_path.name


class TestProductionLog:
    def test_appends_jsonl(self, manager):
        manager.append_production_log({"action": "test", "detail": "first"})
        manager.append_production_log({"action": "test", "detail": "second"})

        log_path = manager._logs_dir / "production-log.jsonl"
        assert log_path.exists()
        lines = log_path.read_text(encoding="utf-8").strip().split("\n")
        assert len(lines) == 2

        entry1 = json.loads(lines[0])
        assert entry1["action"] == "test"
        assert entry1["detail"] == "first"
        assert "timestamp" in entry1

    def test_creates_logs_dir(self, manager):
        assert not manager._logs_dir.exists()
        manager.append_production_log({"action": "init"})
        assert manager._logs_dir.exists()


class TestOutputSummary:
    def test_empty_summary(self, manager):
        summary = manager.get_output_summary()
        assert summary["nb2_images"] == 0
        assert summary["compositions"] == 0

    def test_counts_images(self, manager, vdp_spec, mock_generated_image):
        manager.save_nb2_image(image=mock_generated_image, vdp=vdp_spec)
        manager.save_nb2_image(image=mock_generated_image, vdp=vdp_spec)

        summary = manager.get_output_summary()
        assert summary["nb2_images"] == 2
        assert summary["total_size_mb"] > 0
