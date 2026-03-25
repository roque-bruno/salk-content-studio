"""
Publisher Worker LinkedIn — API LinkedIn v2.

Publica posts com texto, imagem ou artigo no perfil/pagina corporativa.
Requer: OAuth2 access token com permissoes w_member_social ou w_organization_social.
"""

from __future__ import annotations

import logging
import os
from datetime import datetime
from typing import Optional

import httpx

from content_pipeline.publishers.base import PostMetrics, PublishResult, PublisherBase

logger = logging.getLogger(__name__)

LINKEDIN_API_BASE = "https://api.linkedin.com/v2"


class LinkedInPublisher(PublisherBase):
    """Publisher para LinkedIn via API v2."""

    platform = "linkedin"

    def __init__(self, preview_mode: bool = True):
        super().__init__(preview_mode=preview_mode)
        self._access_token = os.getenv("LINKEDIN_ACCESS_TOKEN", "")
        self._org_id = os.getenv("LINKEDIN_ORG_ID", "")  # URN da organizacao
        self._configured = bool(self._access_token and self._org_id)

    async def publish(
        self,
        content: str,
        media_paths: Optional[list[str]] = None,
        schedule_time: Optional[str] = None,
        media_urls: Optional[list[str]] = None,
        article_url: str = "",
        article_title: str = "",
        **kwargs,
    ) -> PublishResult:
        """
        Publica no LinkedIn.

        Args:
            content: Texto do post
            media_urls: URLs de imagens (upload separado necessario)
            article_url: URL de artigo para compartilhar
            article_title: Titulo do artigo compartilhado
        """
        if self.preview_mode or not self._configured:
            return self._preview_result(content, media_paths=media_paths)

        try:
            author = f"urn:li:organization:{self._org_id}"
            headers = {
                "Authorization": f"Bearer {self._access_token}",
                "Content-Type": "application/json",
                "X-Restli-Protocol-Version": "2.0.0",
            }

            # Build share content
            share_content = {
                "author": author,
                "lifecycleState": "PUBLISHED",
                "specificContent": {
                    "com.linkedin.ugc.ShareContent": {
                        "shareCommentary": {"text": content},
                        "shareMediaCategory": "NONE",
                    }
                },
                "visibility": {
                    "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
                },
            }

            # Add article if provided
            if article_url:
                share_content["specificContent"]["com.linkedin.ugc.ShareContent"]["shareMediaCategory"] = "ARTICLE"
                share_content["specificContent"]["com.linkedin.ugc.ShareContent"]["media"] = [{
                    "status": "READY",
                    "originalUrl": article_url,
                    "title": {"text": article_title or content[:100]},
                }]

            async with httpx.AsyncClient() as client:
                resp = await client.post(
                    f"{LINKEDIN_API_BASE}/ugcPosts",
                    headers=headers,
                    json=share_content,
                )
                resp.raise_for_status()
                post_id = resp.json().get("id", "")

            return PublishResult(
                success=True,
                platform=self.platform,
                post_id=post_id,
                post_url=f"https://www.linkedin.com/feed/update/{post_id}/",
                published_at=datetime.now().isoformat(),
                metadata={"has_article": bool(article_url)},
            )

        except Exception as e:
            logger.error(f"LinkedIn publish error: {e}")
            return PublishResult(
                success=False, platform=self.platform, error=str(e)
            )

    async def get_post_metrics(self, post_id: str) -> PostMetrics:
        """Coleta metricas de um post LinkedIn."""
        if self.preview_mode or not self._configured:
            return PostMetrics(
                post_id=post_id,
                platform=self.platform,
                collected_at=datetime.now().isoformat(),
            )

        try:
            headers = {
                "Authorization": f"Bearer {self._access_token}",
                "X-Restli-Protocol-Version": "2.0.0",
            }

            async with httpx.AsyncClient() as client:
                resp = await client.get(
                    f"{LINKEDIN_API_BASE}/socialActions/{post_id}",
                    headers=headers,
                )

                if resp.status_code != 200:
                    return PostMetrics(
                        post_id=post_id,
                        platform=self.platform,
                        collected_at=datetime.now().isoformat(),
                    )

                data = resp.json()
                likes = data.get("likesSummary", {}).get("totalLikes", 0)
                comments = data.get("commentsSummary", {}).get("totalFirstLevelComments", 0)

                return PostMetrics(
                    post_id=post_id,
                    platform=self.platform,
                    likes=likes,
                    comments=comments,
                    engagement=likes + comments,
                    collected_at=datetime.now().isoformat(),
                )

        except Exception as e:
            logger.error(f"LinkedIn metrics error: {e}")
            return PostMetrics(
                post_id=post_id,
                platform=self.platform,
                collected_at=datetime.now().isoformat(),
            )
