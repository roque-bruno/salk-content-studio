"""
Metrics Collector — Coleta automatica de metricas 48h pos-publicacao.

Percorre todos os posts publicados, identifica quais estao a 48h+,
e coleta metricas de engajamento de cada plataforma.

Salva no banco de metricas (Pulse) para analise de performance.
"""

from __future__ import annotations

import logging
from datetime import datetime, timedelta
from typing import Optional

from content_pipeline.publishers.base import PostMetrics, PublisherBase

logger = logging.getLogger(__name__)


class MetricsCollector:
    """Coletor automatico de metricas pos-publicacao."""

    def __init__(
        self,
        publishers: Optional[dict[str, PublisherBase]] = None,
        db=None,
    ):
        self.publishers = publishers or {}
        self.db = db

    async def collect_pending(
        self,
        hours_after_publish: int = 48,
    ) -> dict:
        """
        Coleta metricas de todos os posts pendentes (publicados ha X horas).

        Returns:
            dict com total coletado, erros, e resultados por plataforma
        """
        if self.db is None:
            return {"error": "Database nao configurado", "collected": 0}

        # Buscar pecas publicadas
        pieces = self.db.list_pieces(stage="published")
        cutoff = datetime.now() - timedelta(hours=hours_after_publish)
        results = {"collected": 0, "errors": 0, "by_platform": {}}

        for piece in pieces:
            # Verificar se ja passou tempo suficiente
            published_at = piece.get("published_at") or piece.get("updated_at", "")
            if not published_at:
                continue

            try:
                pub_dt = datetime.fromisoformat(published_at)
                if pub_dt > cutoff:
                    continue  # Muito recente, esperar
            except (ValueError, TypeError):
                continue

            # Verificar se ja coletou metricas para este post
            post_id = piece.get("post_id", "")
            platform = piece.get("platform", "")
            if not post_id or not platform:
                continue

            # Coletar metricas da plataforma
            publisher = self.publishers.get(platform)
            if publisher is None:
                continue

            try:
                metrics = await publisher.get_post_metrics(post_id)
                if metrics.impressions > 0 or metrics.likes > 0:
                    # Salvar metricas no banco
                    self.db.save_metric({
                        "piece_id": piece.get("id", ""),
                        "post_id": post_id,
                        "platform": platform,
                        "impressions": metrics.impressions,
                        "reach": metrics.reach,
                        "engagement": metrics.engagement,
                        "likes": metrics.likes,
                        "comments": metrics.comments,
                        "shares": metrics.shares,
                        "saves": metrics.saves,
                        "clicks": metrics.clicks,
                        "video_views": metrics.video_views,
                        "collected_at": metrics.collected_at,
                    })
                    results["collected"] += 1
                    plat_key = platform
                    results["by_platform"].setdefault(plat_key, 0)
                    results["by_platform"][plat_key] += 1

            except Exception as e:
                logger.error(f"Metrics collection error for {post_id}: {e}")
                results["errors"] += 1

        return results

    async def collect_single(
        self,
        platform: str,
        post_id: str,
    ) -> dict:
        """Coleta metricas de um post especifico."""
        publisher = self.publishers.get(platform)
        if publisher is None:
            return {"error": f"Publisher nao encontrado: {platform}"}

        try:
            metrics = await publisher.get_post_metrics(post_id)
            return metrics.to_dict()
        except Exception as e:
            return {"error": str(e), "post_id": post_id, "platform": platform}

    def get_collection_status(self) -> dict:
        """Retorna status das plataformas configuradas."""
        status = {}
        for name, pub in self.publishers.items():
            status[name] = {
                "configured": pub.configured,
                "preview_mode": pub.preview_mode,
            }
        return {
            "platforms": status,
            "total_configured": sum(1 for p in status.values() if p["configured"]),
        }
