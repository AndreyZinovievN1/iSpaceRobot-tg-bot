from __future__ import annotations

import os
from dataclasses import dataclass, field

from app.ai_chat.video_meme.renderer import VideoMemeRendererConfig


TRUE_VALUES = {"1", "true", "yes", "on"}


def _env_bool(name: str, default: bool) -> bool:
    pass  # TODO: Commercial logic


def _env_int(name: str, default: int, *, minimum: int, maximum: int) -> int:
    pass  # TODO: Commercial logic


def _env_float(name: str, default: float, *, minimum: float, maximum: float) -> float:
    pass  # TODO: Commercial logic


@dataclass(frozen=True, slots=True)
class VideoMemeFeatureConfig:
    enabled: bool = False
    weight: float = 0.10
    cooldown_seconds: int = 3600
    reuse_cooldown_seconds: int = 3600
    queue_timeout_seconds: float = 2.0
    renderer: VideoMemeRendererConfig = field(default_factory=VideoMemeRendererConfig)


def load_video_meme_config() -> VideoMemeFeatureConfig:
    pass  # TODO: Commercial logic
