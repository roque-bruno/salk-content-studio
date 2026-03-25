"""Testes do Gemini Client — com mock do SDK."""

from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest
from PIL import Image

from content_pipeline.api.gemini_client import (
    GeminiAuthError,
    GeminiClient,
    GeminiClientError,
    GeminiGenerationError,
)
from content_pipeline.config import GeminiConfig


@pytest.fixture
def config():
    return GeminiConfig(api_key="test-key-12345")


@pytest.fixture
def mock_genai():
    with patch("content_pipeline.api.gemini_client.genai") as mock:
        mock.GenerativeModel.return_value = MagicMock()
        mock.GenerationConfig = MagicMock
        yield mock


@pytest.fixture
def client(config, mock_genai):
    return GeminiClient(config)


class TestInit:
    def test_configures_sdk(self, config, mock_genai):
        GeminiClient(config)
        mock_genai.configure.assert_called_once_with(api_key="test-key-12345")

    def test_raises_without_key(self, mock_genai):
        config = GeminiConfig(api_key="")
        with pytest.raises(GeminiAuthError):
            GeminiClient(config)


class TestUploadReference:
    def test_upload_existing_file(self, client, mock_genai, sample_product_png):
        mock_genai.upload_file.return_value = MagicMock(name="uploaded-file-id")
        result = client.upload_reference_image(sample_product_png)
        mock_genai.upload_file.assert_called_once()
        assert result is not None

    def test_upload_missing_file(self, client):
        with pytest.raises(FileNotFoundError):
            client.upload_reference_image(Path("/nonexistent/product.png"))

    def test_upload_wrong_format(self, client, tmp_path):
        txt_file = tmp_path / "file.txt"
        txt_file.write_text("not an image")
        with pytest.raises(GeminiClientError, match="Formato"):
            client.upload_reference_image(txt_file)


class TestGenerateNB2Image:
    def test_generates_image(self, client, mock_genai, sample_product_png, mock_gemini_response):
        mock_genai.upload_file.return_value = MagicMock(name="ref-id")
        client._model.generate_content.return_value = mock_gemini_response

        result = client.generate_nb2_image(
            product_image_path=sample_product_png,
            prompt="Place this product in scene",
        )
        assert isinstance(result, Image.Image)
        assert result.size == (1080, 1350)

    def test_uses_uploaded_ref(self, client, sample_product_png, mock_gemini_response):
        uploaded = MagicMock(name="pre-uploaded")
        client._model.generate_content.return_value = mock_gemini_response

        result = client.generate_nb2_image(
            product_image_path=sample_product_png,
            prompt="test",
            uploaded_ref=uploaded,
        )
        assert isinstance(result, Image.Image)

    def test_raises_on_empty_response(self, client, mock_genai, sample_product_png):
        mock_genai.upload_file.return_value = MagicMock(name="ref-id")

        empty_response = MagicMock()
        empty_response.candidates = []
        client._model.generate_content.return_value = empty_response

        with pytest.raises((GeminiGenerationError, Exception)):
            client.generate_nb2_image(
                product_image_path=sample_product_png,
                prompt="test",
            )

    def test_raises_on_text_only_response(self, client, mock_genai, sample_product_png):
        mock_genai.upload_file.return_value = MagicMock(name="ref-id")

        text_part = MagicMock()
        text_part.inline_data = None
        del text_part._result

        content = MagicMock()
        content.parts = [text_part]

        candidate = MagicMock()
        candidate.content = content

        response = MagicMock()
        response.candidates = [candidate]
        response._result = MagicMock()
        response._result.candidates = []

        client._model.generate_content.return_value = response

        with pytest.raises((GeminiGenerationError, Exception)):
            client.generate_nb2_image(
                product_image_path=sample_product_png,
                prompt="test",
            )


class TestGenerateText:
    def test_generates_text(self, client):
        client._model.generate_content.return_value = MagicMock(text="Generated copy text")
        result = client.generate_text("Write copy for LEV")
        assert result == "Generated copy text"

    def test_raises_on_error(self, client):
        client._model.generate_content.side_effect = Exception("API error")
        with pytest.raises(GeminiGenerationError):
            client.generate_text("test")


class TestCleanup:
    def test_cleanup_files(self, client, mock_genai):
        mock_file = MagicMock(name="temp-file")
        mock_genai.list_files.return_value = [mock_file]
        client.cleanup_uploaded_files()
        mock_genai.delete_file.assert_called_once()
