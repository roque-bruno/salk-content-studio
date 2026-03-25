"""
Publisher Base — Classe abstrata para todos os publisher workers.

Cada publisher implementa publish() e get_metrics().
Todos suportam preview_mode (simula sem publicar de fato).
"""

from __future__ import annotations

import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

logger = logging.getLogger(__name__)


@dataclass
class PublishResult:
    """Resultado de uma publicacao."""
    success: bool
    platform: str
    post_id: str = ""
    post_url: str = ""
    published_at: str = ""
    preview_mode: bool = False
    error: str = ""
    metadata: dict = field(default_factory=dict)

    def to_dict(self) -> dict:
        return {
            "success": self.success,
            "platform": self.platform,
            "post_id": self.post_id,
            "post_url": self.post_url,
            "published_at": self.published_at,
            "preview_mode": self.preview_mode,
            "error": self.error,
            "metadata": self.metadata,
        }


@dataclass
class PostMetrics:
    """Metricas de um post publicado."""
    post_id: str
    platform: str
    impressions: int = 0
    reach: int = 0
    engagement: int = 0
    likes: int = 0
    comments: int = 0
    shares: int = 0
    saves: int = 0
    clicks: int = 0
    video_views: int = 0
    collected_at: str = ""

    def to_dict(self) -> dict:
        return {
            "post_id": self.post_id,
            "platform": self.platform,
            "impressions": self.impressions,
            "reach": self.reach,
            "engagement": self.engagement,
            "likes": self.likes,
            "comments": self.comments,
            "shares": self.shares,
            "saves": self.saves,
            "clicks": self.clicks,
            "video_views": self.video_views,
            "collected_at": self.collected_at,
        }


class PublisherBase(ABC):
    """Classe abstrata para publisher workers."""

    platform: str = "unknown"

    def __init__(self, preview_mode: bool = True):
        self.preview_mode = preview_mode
        self._configured = False

    @property
    def configured(self) -> bool:
        return self._configured

    @abstractmethod
    async def publish(
        self,
        content: str,
        media_paths: Optional[list[str]] = None,
        schedule_time: Optional[str] = None,
        **kwargs,
    ) -> PublishResult:
        """Publica conteudo na plataforma."""
        ...

    @abstractmethod
    async def get_post_metrics(self, post_id: str) -> PostMetrics:
        """Coleta metricas de um post especifico."""
        ...

    def _preview_result(self, content: str, **kwargs) -> PublishResult:
        """Retorna resultado simulado em preview mode."""
        return PublishResult(
            success=True,
            platform=self.platform,
            post_id=f"preview_{self.platform}_{datetime.now().strftime('%Y%m%d%H%M%S')}",
            post_url=f"https://{self.platform}.com/preview",
            published_at=datetime.now().isoformat(),
            preview_mode=True,
            metadata={
                "content_length": len(content),
                "media_count": len(kwargs.get("media_paths") or []),
            },
        )
