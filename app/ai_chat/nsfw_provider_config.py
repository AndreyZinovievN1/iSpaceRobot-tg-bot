from __future__ import annotations

import os
from dataclasses import dataclass, field

from app.ai_chat.nsfw_types import NSFWVerdict


DEFAULT_NSFW_MODEL_NAME = "prithivMLmods/vit-mini-explicit-content"
PROVIDER_SAFE_REASON = "nsfw_scan_safe"
UNCERTAIN_WEAK_SAFE_REASON = "nsfw_scan_uncertain_weak_safe"


@dataclass(frozen=True, slots=True)
class NSFWProviderThresholds:
    block_pornography: float = 0.70
    block_hentai: float = 0.65
    approve_safe: float = 0.60
    approve_anime: float = 0.60
    max_explicit_for_safe: float = 0.25
    uncertain_sensual: float = 0.60
    # "Strong safe" gate: a SAFE verdict is only trusted when the model is
    # strongly confident about it OR when the explicit score is negligible.
    # Borderline "safe" results are escalated to UNCERTAIN so the cascade
    # (and, when disabled, the human owner) re-checks them instead of the bot
    # silently reusing possibly explicit media.
    strong_safe: float = 0.80
    weak_safe_max_explicit: float = 0.05


@dataclass(frozen=True, slots=True)
class NSFWProviderConfig:
    model_name: str = DEFAULT_NSFW_MODEL_NAME
    device: str = "auto"
    thresholds: NSFWProviderThresholds = field(default_factory=NSFWProviderThresholds)
    cache_enabled: bool = True


def verdict_from_scores(
    scores: dict[str, float],
    *,
    thresholds: NSFWProviderThresholds,
) -> tuple[NSFWVerdict, str]:
    pass  # TODO: Commercial logic


def _env_bool(name: str, default: bool) -> bool:
    pass  # TODO: Commercial logic


def load_nsfw_provider_config() -> NSFWProviderConfig:
    pass  # TODO: Commercial logic
