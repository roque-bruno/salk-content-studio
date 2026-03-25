"""Motor NB2 — geração product-in-scene via Gemini API."""

from content_pipeline.nb2.prompt_builder import PromptBuilder
from content_pipeline.nb2.vdp_loader import VDPLoader, VDPSpec

__all__ = ["NB2Engine", "PromptBuilder", "VDPLoader", "VDPSpec"]


def __getattr__(name: str):
    if name == "NB2Engine":
        from content_pipeline.nb2.engine import NB2Engine
        return NB2Engine
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
