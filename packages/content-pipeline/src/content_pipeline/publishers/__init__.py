"""Publishers — Workers para publicacao em redes sociais."""

from content_pipeline.publishers.base import PublisherBase, PublishResult
from content_pipeline.publishers.instagram import InstagramPublisher
from content_pipeline.publishers.linkedin import LinkedInPublisher
from content_pipeline.publishers.facebook import FacebookPublisher
from content_pipeline.publishers.youtube import YouTubePublisher
from content_pipeline.publishers.metrics_collector import MetricsCollector
from content_pipeline.publishers.batch_approval import BatchApproval

__all__ = [
    "BatchApproval",
    "FacebookPublisher",
    "InstagramPublisher",
    "LinkedInPublisher",
    "MetricsCollector",
    "PublishResult",
    "PublisherBase",
    "YouTubePublisher",
]
