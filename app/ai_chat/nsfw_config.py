from __future__ import annotations

import os
from dataclasses import dataclass


NSFW_SCAN_ENV = "NSFW_SCAN_ENABLED"
NSFW_BENCHMARK_UI_ENV = "NSFW_BENCHMARK_UI_ENABLED"
NSFW_SHADOW_ENV = "NSFW_SHADOW_ENABLED"
NSFW_CASCADE_ENV = "NSFW_CASCADE_ENABLED"
NSFW_CASCADE_POLICY_VERSION = "v1"
NSFW_HENTAI_BORDERLINE_MAX_PORNOGRAPHY = 0.20
NSFW_HENTAI_BORDERLINE_MAX_SENSUAL = 0.20
_TRUE_VALUES = {"1", "true", "yes", "on", "enabled"}


@dataclass(frozen=True, slots=True)
class NSFWShadowConfig:
    enabled: bool = False
    marqo_enabled: bool = True
    owen_enabled: bool = True
    load_timeout_seconds: float = 60.0
    inference_timeout_seconds: float = 5.0
    output_path: str = "var/nsfw_shadow/results.jsonl"


@dataclass(frozen=True, slots=True)
class NSFWCascadeConfig:
    enabled: bool = False
    policy_version: str = NSFW_CASCADE_POLICY_VERSION
    marqo_safe_threshold: float = 0.98
    marqo_block_threshold: float = 0.90
    owen_safe_threshold: float = 0.95
    owen_block_threshold: float = 0.80
    owen_max_nsfw_for_safe: float = 0.10
    owen_max_nsfl_for_safe: float = 0.20
    hentai_borderline_max_pornography: float = NSFW_HENTAI_BORDERLINE_MAX_PORNOGRAPHY
    hentai_borderline_max_sensual: float = NSFW_HENTAI_BORDERLINE_MAX_SENSUAL
    load_timeout_seconds: float = 60.0
    inference_timeout_seconds: float = 5.0


def _env_flag(name: str, default: bool) -> bool:
    pass  # TODO: Commercial logic


def _env_positive_float(name: str, default: float) -> float:
    pass  # TODO: Commercial logic


def _env_probability(name: str, default: float) -> float:
    pass  # TODO: Commercial logic


def nsfw_scan_enabled() -> bool:
    pass  # TODO: Commercial logic


def nsfw_benchmark_ui_enabled() -> bool:
    pass  # TODO: Commercial logic


def nsfw_shadow_enabled() -> bool:
    pass  # TODO: Commercial logic


def load_nsfw_shadow_config() -> NSFWShadowConfig:
    pass  # TODO: Commercial logic


def nsfw_cascade_enabled() -> bool:
    pass  # TODO: Commercial logic


def load_nsfw_cascade_config() -> NSFWCascadeConfig:
    pass  # TODO: Commercial logic
