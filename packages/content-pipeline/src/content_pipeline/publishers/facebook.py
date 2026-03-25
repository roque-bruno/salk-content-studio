"""
Publisher Worker Facebook — API Facebook Graph.

Publica posts com texto, imagem ou video na pagina corporativa.
Requer: page access token com permissoes pages_manage_posts, pages_read_engagement.
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


class FacebookPublisher(PublisherBase):
    """Publisher para Facebook via Graph API."""

    platform = "facebook"

    def __init__(self, preview_mode: bool = True):
        super().__init__(preview_mode=preview_mode)
        self._access_token = os.getenv("FACEBOOK_ACCESS_TOKEN", "")
        self._page_id = os.getenv("FACEBOOK_PAGE_ID", "")
        self._configured = bool(self._access_token and self._page_id)

    async def publish(
        self,
        content: str,
        media_paths: Optional[list[str]] = None,
        schedule_time: Optional[str] = None,
        media_urls: Optional[list[str]] = None,
        link: str = "",
        **kwargs,
    ) -> PublishResult:
        """Publica no Facebook."""
        if self.preview_mode or not self._configured:
            return self._preview_result(content, media_paths=media_paths)

        try:
            async with httpx.AsyncClient() as client:
                urls = media_urls or []

                if urls:
                    # Post com foto
                    resp = await client.post(
                        f"{GRAPH_API_BASE}/{self._page_id}/photos",
                        data={
                            "url": urls[0],
                            "caption": content,
                            "access_token": self._access_token,
                        },
                    )
                elif link:
                    # Post com link
                    resp = await client.post(
                        f"{GRAPH_API_BASE}/{self._page_id}/feed",
                        data={
                            "message": content,
                            "link": link,
                            "access_token": self._access_token,
                        },
                    )
                else:
                    # Post apenas texto
                    resp = await client.post(
                        f"{GRAPH_API_BASE}/{self._page_id}/feed",
                        data={
                            "message": content,
                            "access_token": self._access_token,
                        },
                    )

                resp.raise_for_status()
                post_id = resp.json().get("id", resp.json().get("post_id", ""))

            return PublishResult(
                success=True,
                platform=self.platform,
                post_id=post_id,
                post_url=f"https://www.facebook.com/{post_id}",
                published_at=datetime.now().isoformat(),
            )

        except Exception as e:
            logger.error(f"Facebook publish error: {e}")
            return PublishResult(
                success=False, platform=self.platform, error=str(e)
            )

    async def get_post_metrics(self, post_id: str) -> PostMetrics:
        """Coleta metricas de um post Facebook."""
        if self.preview_mode or not self._configured:
            return PostMetrics(
                post_id=post_id,
                platform=self.platform,
                collected_at=datetime.now().isoformat(),
            )

        try:
            async with httpx.AsyncClient() as client:
                resp = await client.get(
                    f"{GRAPH_API_BASE}/{post_id}",
                    params={
                        "fields": "likes.summary(true),comments.summary(true),shares",
                        "access_token": self._access_token,
                    },
                )
                resp.raise_for_status()
                data = resp.json()

                likes = data.get("likes", {}).get("summary", {}).get("total_count", 0)
                comments = data.get("comments", {}).get("summary", {}).get("total_count", 0)
                shares = data.get("shares", {}).get("count", 0)

                # Get insights
                insights_resp = await client.get(
                    f"{GRAPH_API_BASE}/{post_id}/insights",
                    params={
                        "metric": "post_impressions,post_impressions_unique,post_clicks",
                        "access_token": self._access_token,
                    },
                )

                impressions = 0
                reach = 0
                clicks = 0
                if insights_resp.status_code == 200:
                    for item in insights_resp.json().get("data", []):
                        val = item.get("values", [{}])[0].get("value", 0)
                        if item["name"] == "post_impressions":
                            impressions = val
                        elif item["name"] == "post_impressions_unique":
                            reach = val
                        elif item["name"] == "post_clicks":
                            clicks = val

                return PostMetrics(
                    post_id=post_id,
                    platform=self.platform,
                    impressions=impressions,
                    reach=reach,
                    likes=likes,
                    comments=comments,
                    shares=shares,
                    clicks=clicks,
                    engagement=likes + comments + shares,
                    collected_at=datetime.now().isoformat(),
                )

        except Exception as e:
            logger.error(f"Facebook metrics error: {e}")
            return PostMetrics(
                post_id=post_id,
                platform=self.platform,
                collected_at=datetime.now().isoformat(),
            )
