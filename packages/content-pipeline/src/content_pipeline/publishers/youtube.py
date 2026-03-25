"""
Publisher Worker YouTube — API YouTube Data v3.

Publica Shorts (videos curtos verticais) no canal corporativo.
Requer: OAuth2 access token com scope youtube.upload.
"""

from __future__ import annotations

import logging
import os
from datetime import datetime
from pathlib import Path
from typing import Optional

import httpx

from content_pipeline.publishers.base import PostMetrics, PublishResult, PublisherBase

logger = logging.getLogger(__name__)

YOUTUBE_API_BASE = "https://www.googleapis.com/youtube/v3"
YOUTUBE_UPLOAD_URL = "https://www.googleapis.com/upload/youtube/v3/videos"


class YouTubePublisher(PublisherBase):
    """Publisher para YouTube Shorts via Data API v3."""

    platform = "youtube"

    def __init__(self, preview_mode: bool = True):
        super().__init__(preview_mode=preview_mode)
        self._access_token = os.getenv("YOUTUBE_ACCESS_TOKEN", "")
        self._configured = bool(self._access_token)

    async def publish(
        self,
        content: str,
        media_paths: Optional[list[str]] = None,
        schedule_time: Optional[str] = None,
        title: str = "",
        tags: Optional[list[str]] = None,
        privacy: str = "public",
        **kwargs,
    ) -> PublishResult:
        """
        Publica video no YouTube (Shorts).

        Args:
            content: Descricao do video
            media_paths: Caminho do arquivo de video local
            title: Titulo do video
            tags: Tags do video
            privacy: public, private, unlisted
        """
        if self.preview_mode or not self._configured:
            return self._preview_result(content, media_paths=media_paths)

        if not media_paths:
            return PublishResult(
                success=False,
                platform=self.platform,
                error="Video file path obrigatorio para YouTube",
            )

        video_path = Path(media_paths[0])
        if not video_path.exists():
            return PublishResult(
                success=False,
                platform=self.platform,
                error=f"Video nao encontrado: {video_path}",
            )

        try:
            # YouTube requires multipart upload
            # Step 1: Initiate resumable upload
            headers = {
                "Authorization": f"Bearer {self._access_token}",
                "Content-Type": "application/json",
            }

            metadata = {
                "snippet": {
                    "title": title or content[:100],
                    "description": content,
                    "tags": tags or [],
                    "categoryId": "28",  # Science & Technology
                },
                "status": {
                    "privacyStatus": privacy,
                    "selfDeclaredMadeForKids": False,
                },
            }

            # For Shorts: title should include #Shorts
            if "#Shorts" not in metadata["snippet"]["title"]:
                metadata["snippet"]["title"] += " #Shorts"

            async with httpx.AsyncClient(timeout=300) as client:
                # Initiate upload
                init_resp = await client.post(
                    f"{YOUTUBE_UPLOAD_URL}?uploadType=resumable&part=snippet,status",
                    headers=headers,
                    json=metadata,
                )
                init_resp.raise_for_status()
                upload_url = init_resp.headers.get("Location", "")

                if not upload_url:
                    return PublishResult(
                        success=False,
                        platform=self.platform,
                        error="Failed to get upload URL",
                    )

                # Upload video file
                video_data = video_path.read_bytes()
                upload_resp = await client.put(
                    upload_url,
                    content=video_data,
                    headers={
                        "Authorization": f"Bearer {self._access_token}",
                        "Content-Type": "video/mp4",
                        "Content-Length": str(len(video_data)),
                    },
                )
                upload_resp.raise_for_status()
                video_id = upload_resp.json().get("id", "")

            return PublishResult(
                success=True,
                platform=self.platform,
                post_id=video_id,
                post_url=f"https://youtube.com/shorts/{video_id}",
                published_at=datetime.now().isoformat(),
                metadata={"title": title, "privacy": privacy},
            )

        except Exception as e:
            logger.error(f"YouTube publish error: {e}")
            return PublishResult(
                success=False, platform=self.platform, error=str(e)
            )

    async def get_post_metrics(self, post_id: str) -> PostMetrics:
        """Coleta metricas de um video YouTube."""
        if self.preview_mode or not self._configured:
            return PostMetrics(
                post_id=post_id,
                platform=self.platform,
                collected_at=datetime.now().isoformat(),
            )

        try:
            async with httpx.AsyncClient() as client:
                resp = await client.get(
                    f"{YOUTUBE_API_BASE}/videos",
                    params={
                        "part": "statistics",
                        "id": post_id,
                        "key": os.getenv("YOUTUBE_API_KEY", self._access_token),
                    },
                )
                resp.raise_for_status()
                items = resp.json().get("items", [])

                if not items:
                    return PostMetrics(
                        post_id=post_id,
                        platform=self.platform,
                        collected_at=datetime.now().isoformat(),
                    )

                stats = items[0].get("statistics", {})
                views = int(stats.get("viewCount", 0))
                likes = int(stats.get("likeCount", 0))
                comments = int(stats.get("commentCount", 0))

                return PostMetrics(
                    post_id=post_id,
                    platform=self.platform,
                    video_views=views,
                    likes=likes,
                    comments=comments,
                    engagement=likes + comments,
                    collected_at=datetime.now().isoformat(),
                )

        except Exception as e:
            logger.error(f"YouTube metrics error: {e}")
            return PostMetrics(
                post_id=post_id,
                platform=self.platform,
                collected_at=datetime.now().isoformat(),
            )
