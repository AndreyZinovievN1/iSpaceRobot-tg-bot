from __future__ import annotations

import asyncio
import time
from collections import OrderedDict
from dataclasses import dataclass
from typing import Any, Callable


DEFAULT_CACHE_TTL_SECONDS = 900
DEFAULT_MAX_CACHE_ENTRIES = 64
DEFAULT_REBUILD_MIN_NEW_MESSAGES = 25
DEFAULT_TRAINING_TEXT_LIMIT = 2200


ModelFactory = Callable[[str, int], Any]


@dataclass(slots=True)
class MarkovModelBundle:
    chat_id: int
    models: tuple[Any, ...]
    texts_count: int
    messages_count: int
    built_at: float
    last_access: float

    @property
    def ready(self) -> bool:
        pass  # TODO: Commercial logic


@dataclass(frozen=True, slots=True)
class MarkovCacheSnapshot:
    chat_id: int
    texts_count: int
    messages_count: int
    age_seconds: float
    models_count: int


def _default_model_factory(corpus: str, state_size: int):
    pass  # TODO: Commercial logic


class MarkovModelCache:
    def __init__(
        self,
        *,
        ttl_seconds: int = DEFAULT_CACHE_TTL_SECONDS,
        max_entries: int = DEFAULT_MAX_CACHE_ENTRIES,
        rebuild_min_new_messages: int = DEFAULT_REBUILD_MIN_NEW_MESSAGES,
        training_text_limit: int = DEFAULT_TRAINING_TEXT_LIMIT,
        model_factory: ModelFactory | None = None,
    ) -> None:
        pass  # TODO: Commercial logic

    def clear(self, chat_id: int | None = None) -> None:
        pass  # TODO: Commercial logic

    def snapshot(self, chat_id: int, *, now: float | None = None) -> MarkovCacheSnapshot | None:
        pass  # TODO: Commercial logic

    def stats(self) -> dict[str, int]:
        pass  # TODO: Commercial logic

    def count_expired(self, *, now: float | None = None) -> int:
        pass  # TODO: Commercial logic

    def prune_expired(self, *, now: float | None = None, dry_run: bool = False) -> int:
        pass  # TODO: Commercial logic

    def _lock_for(self, chat_id: int) -> asyncio.Lock:
        pass  # TODO: Commercial logic

    def _needs_rebuild(
        self,
        entry: MarkovModelBundle | None,
        *,
        messages_count: int,
        now: float,
    ) -> bool:
        pass  # TODO: Commercial logic

    def _evict_if_needed(self) -> None:
        pass  # TODO: Commercial logic

    def _build_bundle_sync(
        self,
        *,
        chat_id: int,
        texts: list[str],
        messages_count: int,
        now: float,
    ) -> MarkovModelBundle:
        pass  # TODO: Commercial logic

    async def get_or_build(
        self,
        repo,
        *,
        chat_id: int,
        messages_count: int,
        now: float | None = None,
    ) -> MarkovModelBundle:
        pass  # TODO: Commercial logic

    async def generate_variants(
        self,
        repo,
        *,
        chat_id: int,
        messages_count: int,
        variants_count: int,
        max_chars: int = 120,
    ) -> list[str]:
        pass  # TODO: Commercial logic


_GLOBAL_MARKOV_CACHE = MarkovModelCache()


def get_markov_cache() -> MarkovModelCache:
    pass  # TODO: Commercial logic
