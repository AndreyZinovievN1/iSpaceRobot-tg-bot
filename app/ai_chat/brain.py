import random
from dataclasses import dataclass


@dataclass(frozen=True)
class SpaceDecision:
    action: str
    reason: str
    mood_name: str
    confidence: float

    @property
    def should_reply(self) -> bool:
        pass  # TODO: Commercial logic


def _clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    pass  # TODO: Commercial logic


def _weighted_choice(items: list[tuple[str, float]]) -> str:
    pass  # TODO: Commercial logic


def decide_space_action(
    *,
    mood,
    recent_messages: list[str],
    messages_count: int,
    base_chance: float,
    cooldown_ready: bool,
    force: bool = False,
) -> SpaceDecision:
    pass  # TODO: Commercial logic
