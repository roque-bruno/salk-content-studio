"""API clients para serviços externos."""

__all__ = ["GeminiClient"]


def __getattr__(name: str):
    if name == "GeminiClient":
        from content_pipeline.api.gemini_client import GeminiClient
        return GeminiClient
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
