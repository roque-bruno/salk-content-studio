"""Testes de configuração do pipeline."""

import os

import pytest


def test_load_config_requires_api_key(monkeypatch):
    """Config deve falhar sem API key."""
    monkeypatch.delenv("GOOGLE_API_KEY", raising=False)
    monkeypatch.delenv("GEMINI_API_KEY", raising=False)

    from content_pipeline.config import load_config

    with pytest.raises(ValueError, match="GOOGLE_API_KEY"):
        load_config(env_file="/nonexistent/.env")


def test_load_config_with_api_key(monkeypatch, tmp_path):
    """Config deve funcionar com API key válida."""
    monkeypatch.setenv("GOOGLE_API_KEY", "test-key-12345")
    monkeypatch.delenv("GEMINI_API_KEY", raising=False)

    from content_pipeline.config import load_config

    config = load_config(env_file="/nonexistent/.env")
    assert config.gemini.api_key == "test-key-12345"
    assert config.nb2.default_width == 1080
    assert config.nb2.default_height == 1350


def test_load_config_gemini_key_fallback(monkeypatch):
    """GEMINI_API_KEY deve funcionar como fallback."""
    monkeypatch.delenv("GOOGLE_API_KEY", raising=False)
    monkeypatch.setenv("GEMINI_API_KEY", "gemini-fallback-key")

    from content_pipeline.config import load_config

    config = load_config(env_file="/nonexistent/.env")
    assert config.gemini.api_key == "gemini-fallback-key"


def test_config_defaults(monkeypatch):
    """Defaults devem estar corretos."""
    monkeypatch.setenv("GOOGLE_API_KEY", "test")

    from content_pipeline.config import load_config

    config = load_config(env_file="/nonexistent/.env")
    assert config.gemini.model == "gemini-2.0-flash-exp"
    assert config.gemini.temperature == 0.4
    assert config.gemini.max_retries == 3
    assert config.nb2.max_generation_attempts == 3
    assert config.nb2.output_format == "png"
    assert config.batch_size == 5
