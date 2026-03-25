"""Orquestração do pipeline de produção de conteúdo."""

__all__ = ["PipelineOrchestrator"]


def __getattr__(name: str):
    if name == "PipelineOrchestrator":
        from content_pipeline.pipeline.orchestrator import PipelineOrchestrator
        return PipelineOrchestrator
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
