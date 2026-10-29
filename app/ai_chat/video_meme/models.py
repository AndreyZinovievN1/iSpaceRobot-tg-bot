from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum
from pathlib import Path


class CropMode(StrEnum):
    CENTER_SQUARE = "center_square"
    BLURRED_BACKGROUND = "blurred_background"


class OverlayMode(StrEnum):
    REQUIRED = "required"
    OPTIONAL = "optional"
    DISABLED = "disabled"


class OverlayPosition(StrEnum):
    # "top" means the safe top-center area of the square. The renderer keeps
    # it away from the corners that Telegram clips in a video note.
    TOP = "top"


class OverlayFit(StrEnum):
    COVER = "cover"
    CONTAIN = "contain"


@dataclass(frozen=True, slots=True)
class VideoMemeTemplate:
    id: str
    file: str
    path: Path
    title: str
    enabled: bool
    start: float
    end: float
    output_duration: float
    crop_mode: CropMode
    overlay_mode: OverlayMode
    overlay_position: OverlayPosition
    overlay_height_ratio: float
    overlay_width_ratio: float
    overlay_fit: OverlayFit
    mute: bool
    loop_overlay: bool
    loop_result: bool
    tags: tuple[str, ...]

    @property
    def fragment_duration(self) -> float:
        return self.end - self.start

    @property
    def needs_overlay(self) -> bool:
        return self.overlay_mode == OverlayMode.REQUIRED

    @property
    def accepts_overlay(self) -> bool:
        return self.overlay_mode != OverlayMode.DISABLED
