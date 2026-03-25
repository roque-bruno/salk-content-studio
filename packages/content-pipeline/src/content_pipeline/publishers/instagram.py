"""
Publisher Worker Instagram — API Instagram Graph.

Usa a Instagram Graph API via Facebook Business para:
- Posts com imagem (single e carrossel)
- Reels (video curto)
- Stories (imagem/video)

Requer: page access token com permissoes instagram_basic, instagram_content_publish.
"""

from __future__ import annotations

import logging
import os
from datetime import datetime
from typing import Optional

import httpx

from content_pipeline.publishers.base import PostMetrics, PublishResult, PublisherBase

logger = logging.getLogger(__name__)

GRAPH_API_BASE = "https://graph.facebook.com/v19.0"


class InstagramPublisher(PublisherBase):
    """Publisher para Instagram via Graph API."""

    platform = "instagram"

    def __init__(self, preview_mode: bool = True):
        super().__init__(preview_mode=preview_mode)
        self._access_token = os.getenv("INSTAGRAM_ACCESS_TOKEN", "")
        self._ig_user_id = os.getenv("INSTAGRAM_USER_ID", "")
        self._configured = bool(self._access_token and self._ig_user_id)

    async def publish(
        self,
        content: str,
        media_paths: Optional[list[str]] = None,
        schedule_time: Optional[str] = None,
        media_type: str = "IMAGE",
        media_urls: Optional[list[str]] = None,
        **kwargs,
    ) -> PublishResult:
        """
        Publica no Instagram.

        Args:
            content: Caption do post
            media_paths: Caminhos locais das midias (nao suportado direto, precisa URL)
            media_urls: URLs publicas das imagens/videos
            media_type: IMAGE, VIDEO, CAROUSEL_ALBUM, REELS
            schedule_time: ISO timestamp para agendamento (futuro)
        """
        if self.preview_mode or not self._configured:
            return self._preview_result(content, media_paths=media_paths)

        try:
            urls = media_urls or []
            if not urls:
                return PublishResult(
                    success=False,
                    platform=self.platform,
                    error="Media URLs obrigatorias para Instagram (imagens devem estar em URL publica)",
                )

            async with httpx.AsyncClient() as client:
                if media_type == "CAROUSEL_ALBUM" and len(urls) > 1:
                    result = await self._publish_carousel(client, content, urls)
                else:
                    result = await self._publish_single(
                        client, content, urls[0], media_type
                    )

            return result

        except Exception as e:
            logger.error(f"Instagram publish error: {e}")
            return PublishResult(
                success=False, platform=self.platform, error=str(e)
            )

    async def _publish_single(
        self, client: httpx.AsyncClient, caption: str, media_url: str, media_type: str
    ) -> PublishResult:
        """Publica post com uma unica midia."""
        # Step 1: Create media container
        container_data = {
            "access_token": self._access_token,
            "caption": caption,
        }

        if media_type == "REELS":
            container_data["media_type"] = "REELS"
            container_data["video_url"] = media_url
        elif media_type == "VIDEO":
            container_data["media_type"] = "VIDEO"
            container_data["video_url"] = media_url
        else:
            container_data["image_url"] = media_url

        resp = await client.post(
            f"{GRAPH_API_BASE}/{self._ig_user_id}/media",
            data=container_data,
        )
        resp.raise_for_status()
        container_id = resp.json()["id"]

        # Step 2: Publish container
        pub_resp = await client.post(
            f"{GRAPH_API_BASE}/{self._ig_user_id}/media_publish",
            data={
                "creation_id": container_id,
                "access_token": self._access_token,
            },
        )
        pub_resp.raise_for_status()
        post_id = pub_resp.json()["id"]

        return PublishResult(
            success=True,
            platform=self.platform,
            post_id=post_id,
            post_url=f"https://www.instagram.com/p/{post_id}/",
            published_at=datetime.now().isoformat(),
            metadata={"media_type": media_type},
        )

    async def _publish_carousel(
        self, client: httpx.AsyncClient, caption: str, media_urls: list[str]
    ) -> PublishResult:
        """Publica carrossel com multiplas imagens."""
        # Step 1: Create individual containers
        children_ids = []
        for url in media_urls[:10]:  # Instagram max 10 slides
            resp = await client.post(
                f"{GRAPH_API_BASE}/{self._ig_user_id}/media",
                data={
                    "image_url": url,
                    "is_carousel_item": "true",
                    "access_token": self._access_token,
                },
            )
            resp.raise_for_status()
            children_ids.append(resp.json()["id"])

        # Step 2: Create carousel container
        resp = await client.post(
            f"{GRAPH_API_BASE}/{self._ig_user_id}/media",
            data={
                "media_type": "CAROUSEL",
                "caption": caption,
                "children": ",".join(children_ids),
                "access_token": self._access_token,
            },
        )
        resp.raise_for_status()
        container_id = resp.json()["id"]

        # Step 3: Publish
        pub_resp = await client.post(
            f"{GRAPH_API_BASE}/{self._ig_user_id}/media_publish",
            data={
                "creation_id": container_id,
                "access_token": self._access_token,
            },
        )
        pub_resp.raise_for_status()
        post_id = pub_resp.json()["id"]

        return PublishResult(
            success=True,
            platform=self.platform,
            post_id=post_id,
            post_url=f"https://www.instagram.com/p/{post_id}/",
            published_at=datetime.now().isoformat(),
            metadata={"media_type": "CAROUSEL_ALBUM", "slides": len(children_ids)},
        )

    async def get_post_metrics(self, post_id: str) -> PostMetrics:
        """Coleta metricas de um post via Instagram Insights API."""
        if self.preview_mode or not self._configured:
            return PostMetrics(
                post_id=post_id,
                platform=self.platform,
                collected_at=datetime.now().isoformat(),
            )

        try:
            async with httpx.AsyncClient() as client:
                # Get basic metrics
                resp = await client.get(
                    f"{GRAPH_API_BASE}/{post_id}",
                    params={
                        "fields": "like_count,comments_count,timestamp",
                        "access_token": self._access_token,
                    },
                )
                resp.raise_for_status()
                basic = resp.json()

                # Get insights
                insights_resp = await client.get(
                    f"{GRAPH_API_BASE}/{post_id}/insights",
                    params={
                        "metric": "impressions,reach,saved,shares",
                        "access_token": self._access_token,
                    },
                )

                insights = {}
                if insights_resp.status_code == 200:
                    for item in insights_resp.json().get("data", []):
                        insights[item["name"]] = item["values"][0]["value"]

                return PostMetrics(
                    post_id=post_id,
                    platform=self.platform,
                    impressions=insights.get("impressions", 0),
                    reach=insights.get("reach", 0),
                    likes=basic.get("like_count", 0),
                    comments=basic.get("comments_count", 0),
                    shares=insights.get("shares", 0),
                    saves=insights.get("saved", 0),
                    engagement=(
                        basic.get("like_count", 0)
                        + basic.get("comments_count", 0)
                        + insights.get("shares", 0)
                        + insights.get("saved", 0)
                    ),
                    collected_at=datetime.now().isoformat(),
                )

        except Exception as e:
            logger.error(f"Instagram metrics error: {e}")
            return PostMetrics(
                post_id=post_id,
                platform=self.platform,
                collected_at=datetime.now().isoformat(),
            )
