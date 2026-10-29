from __future__ import annotations

from typing import Any, Iterable

from app.crud_tables.table_ai_chat_helpers import (
    DEFAULT_CLEANUP_BATCH_SIZE,
    parse_execute_count,
    row_get,
)
from app.crud_tables.table_ai_chat_learning import AIChatLearningTable
from app.crud_tables.table_ai_chat_dialogue_pairs import AIChatDialoguePairsTable
from app.crud_tables.table_ai_chat_maintenance import AIChatMaintenanceTable
from app.crud_tables.table_ai_chat_media import (
    AIChatMediaTable,
    MEDIA_CATALOG_LIMIT_PER_CHAT,
    media_asset_from_row,
    normalize_metadata,
)
from app.crud_tables.table_ai_chat_memory import AIChatMemoryTable
from app.crud_tables.table_ai_chat_nsfw import (
    AIChatNSFWTable,
    _media_kind_value,
    _scan_job_status_for_result,
)
from app.crud_tables.table_ai_chat_nsfw_alerts import AIChatNSFWAlertsTable
from app.crud_tables.table_ai_chat_nsfw_human_labels import (
    AIChatNSFWHumanLabelsTable,
)
from app.crud_tables.table_ai_chat_safety import AIChatSafetyTable
from app.crud_tables.table_ai_chat_settings import (
    AIChatSettingsTable,
    DEFAULT_LEARNING_LOG_RETENTION_DAYS,
    DEFAULT_MEMORY_MAX_MESSAGES,
    DEFAULT_MEMORY_RETENTION_DAYS,
)
from app.crud_tables.table_ai_chat_messages import AIChatMessagesTable
from app.crud_tables.table_ai_chat_words import AIChatWordsTable
from app.ai_chat.models import (
    ChatMemory,
    ChatMessageRecord,
    LearningEventType,
    MediaAsset,
    MediaKind,
    MediaSafetySource,
    MediaSafetyStatus,
    UserMemory,
)
from app.ai_chat.nsfw_types import NSFWScanResult, NSFWScanStatus, NSFWVerdict


MEDIA_SEND_FAILURE_LIMIT = 3


class AIChatRepository:
    def __init__(self, db):
        pass  # TODO: Commercial logic

    async def get_settings(self, chat_id: int):
        pass  # TODO: Commercial logic

    async def ensure_settings(self, chat_id: int):
        pass  # TODO: Commercial logic

    async def insert_user_message(
        self,
        record: ChatMessageRecord,
        *,
        telegram_message_id: int | None = None,
        reply_to_message_id: int | None = None,
        message_thread_id: int | None = None,
        sender_user_id: int | None = None,
    ) -> int | None:
        pass  # TODO: Commercial logic

    async def insert_space_message(
        self,
        chat_id: int,
        text: str,
        *,
        telegram_message_id: int | None = None,
        reply_to_message_id: int | None = None,
        message_thread_id: int | None = None,
        sender_user_id: int | None = None,
    ) -> int | None:
        pass  # TODO: Commercial logic

    async def fetch_recent_user_messages(
        self,
        chat_id: int,
        limit: int = 40,
    ) -> list[str]:
        pass  # TODO: Commercial logic

    async def fetch_dialogue_pair_candidate(
        self,
        chat_id: int,
        response_message_id: int,
    ):
        pass  # TODO: Commercial logic

    async def insert_dialogue_pair(
        self,
        *,
        chat_id: int,
        source_message_id: int,
        response_message_id: int,
        source_text: str,
        response_text: str,
        source_user_id: int | None,
        response_user_id: int | None,
        message_thread_id: int | None,
        response_role: str,
    ) -> int | None:
        pass  # TODO: Commercial logic

    async def fetch_similar_dialogue_pairs(
        self,
        *,
        chat_id: int,
        source_text: str,
        message_thread_id: int | None = None,
        exclude_response_message_id: int | None = None,
        limit: int = 10,
    ):
        pass  # TODO: Commercial logic

    async def fetch_recent_space_messages(
        self,
        chat_id: int,
        limit: int = 30,
    ) -> list[str]:
        pass  # TODO: Commercial logic

    async def fetch_training_texts(self, chat_id: int, limit: int = 2200) -> list[str]:
        pass  # TODO: Commercial logic

    async def count_user_messages(self, chat_id: int) -> int:
        pass  # TODO: Commercial logic

    async def count_recent_user_messages(self, chat_id: int, hours: int = 2) -> int:
        pass  # TODO: Commercial logic

    async def update_last_action(self, chat_id: int) -> None:
        pass  # TODO: Commercial logic

    async def update_markov_text_action(self, chat_id: int) -> None:
        pass  # TODO: Commercial logic

    async def fetch_top_chat_words(self, chat_id: int, limit: int = 20) -> list[str]:
        pass  # TODO: Commercial logic

    async def fetch_top_user_words(
        self,
        chat_id: int,
        user_id: int,
        limit: int = 16,
    ) -> list[str]:
        pass  # TODO: Commercial logic

    async def fetch_idle_candidate_settings(self):
        pass  # TODO: Commercial logic

    async def fetch_maintenance_chat_ids(self) -> list[int]:
        pass  # TODO: Commercial logic

    async def upsert_chat_memory_saved(self, chat_id: int, reason: str) -> int:
        pass  # TODO: Commercial logic

    async def upsert_chat_memory_skipped(self, chat_id: int, reason: str) -> None:
        pass  # TODO: Commercial logic

    async def upsert_user_memory_saved(self, record: ChatMessageRecord) -> None:
        pass  # TODO: Commercial logic

    async def upsert_user_memory_skipped(
        self,
        chat_id: int,
        user_id: int,
        user_name: str,
        reason: str,
    ) -> None:
        pass  # TODO: Commercial logic

    async def upsert_chat_words(self, chat_id: int, words: Iterable[str]) -> None:
        pass  # TODO: Commercial logic

    async def upsert_user_words(
        self,
        chat_id: int,
        user_id: int,
        words: Iterable[str],
    ) -> None:
        pass  # TODO: Commercial logic

    async def log_learning_event(
        self,
        *,
        chat_id: int,
        user_id: int | None,
        event_type: LearningEventType,
        reason: str,
        message_id: int | None = None,
        text_sample: str | None = None,
        metadata: dict[str, Any] | None = None,
    ) -> None:
        pass  # TODO: Commercial logic

    async def upsert_media_asset(self, asset: MediaAsset) -> None:
        pass  # TODO: Commercial logic

    async def fetch_media_asset_by_unique(
        self,
        *,
        chat_id: int,
        file_unique_id: str,
        kind: MediaKind,
    ) -> MediaAsset | None:
        pass  # TODO: Commercial logic

    async def fetch_media_asset_by_id(self, asset_id: int) -> MediaAsset | None:
        pass  # TODO: Commercial logic

    async def delete_media_asset_by_id(self, asset_id: int) -> int:
        pass  # TODO: Commercial logic

    async def fetch_pending_media_assets_without_scan_jobs(
        self,
        *,
        limit: int = 500,
    ) -> list[MediaAsset]:
        pass  # TODO: Commercial logic

    async def set_media_safety_status(
        self,
        *,
        chat_id: int,
        file_id: str | None = None,
        file_unique_id: str | None = None,
        safety_status: MediaSafetyStatus,
        reason: str = "manual",
        source: MediaSafetySource = MediaSafetySource.MANUAL,
        decided_by_user_id: int | None = None,
    ) -> int:
        pass  # TODO: Commercial logic

    async def set_media_safety_status_by_asset_id(
        self,
        *,
        asset_id: int,
        safety_status: MediaSafetyStatus,
        reason: str,
        source: MediaSafetySource = MediaSafetySource.MANUAL,
        decided_by_user_id: int | None = None,
    ) -> int:
        pass  # TODO: Commercial logic

    async def fetch_approved_media_asset(
        self,
        *,
        chat_id: int,
        kinds: Iterable[MediaKind],
        exclude_file_ids: Iterable[str] = (),
        reuse_cooldown_seconds: int = 3600,
        fresh_delay_seconds: int = 0,
        exclude_safety_reasons: Iterable[str] = (),
    ) -> MediaAsset | None:
        pass  # TODO: Commercial logic

    async def count_approved_media_assets(
        self,
        *,
        chat_id: int,
        kinds: Iterable[MediaKind],
        fresh_delay_seconds: int = 0,
        exclude_safety_reasons: Iterable[str] = (),
    ) -> int:
        pass  # TODO: Commercial logic

    async def mark_media_used(
        self,
        *,
        chat_id: int,
        file_id: str,
    ) -> None:
        pass  # TODO: Commercial logic

    async def record_media_send_failure(
        self,
        *,
        chat_id: int,
        file_id: str,
        error_text: str,
    ) -> int:
        pass  # TODO: Commercial logic

    async def clear_media_send_failures(
        self,
        *,
        chat_id: int,
        file_id: str,
    ) -> None:
        pass  # TODO: Commercial logic

    async def mark_media_broken(
        self,
        *,
        chat_id: int,
        file_id: str,
        file_unique_id: str | None = None,
        reason: str = "broken_send_failed",
    ) -> int:
        pass  # TODO: Commercial logic

    async def cleanup_media_catalog_limit(
        self,
        *,
        chat_id: int,
        limit: int = MEDIA_CATALOG_LIMIT_PER_CHAT,
    ) -> int:
        pass  # TODO: Commercial logic

    async def upsert_media_safety_rule(
        self,
        *,
        chat_id: int,
        rule_type: str,
        file_id: str | None = None,
        file_unique_id: str | None = None,
        reason: str,
        source: MediaSafetySource = MediaSafetySource.MANUAL,
        decided_by_user_id: int | None = None,
    ) -> None:
        pass  # TODO: Commercial logic

    async def fetch_media_safety_rule(
        self,
        *,
        chat_id: int,
        rule_type: str,
        file_id: str | None = None,
        file_unique_id: str | None = None,
    ):
        pass  # TODO: Commercial logic

    async def deactivate_media_safety_rules(
        self,
        *,
        chat_id: int,
        file_id: str | None = None,
        file_unique_id: str | None = None,
    ) -> int:
        pass  # TODO: Commercial logic

    async def log_media_safety_event(
        self,
        *,
        chat_id: int,
        file_id: str | None,
        file_unique_id: str | None,
        safety_status: MediaSafetyStatus,
        reason: str,
        source: MediaSafetySource,
        decided_by_user_id: int | None = None,
    ) -> None:
        pass  # TODO: Commercial logic

    async def list_media_assets_by_status(
        self,
        *,
        chat_id: int,
        safety_status: MediaSafetyStatus,
        limit: int = 50,
    ) -> list[MediaAsset]:
        pass  # TODO: Commercial logic

    async def create_nsfw_scan_job(
        self,
        asset: MediaAsset,
        *,
        priority: int = 100,
        max_attempts: int = 3,
    ) -> int | None:
        pass  # TODO: Commercial logic

    async def claim_nsfw_scan_jobs(
        self,
        *,
        worker_id: str,
        limit: int = 5,
        lock_seconds: int = 300,
    ) -> list[Any]:
        pass  # TODO: Commercial logic

    async def mark_nsfw_scan_job_done(self, *, job_id: int) -> int:
        pass  # TODO: Commercial logic

    async def mark_nsfw_scan_job_failed(
        self,
        *,
        job_id: int,
        error_text: str,
        retry: bool = True,
        retry_delay_seconds: int = 300,
        terminal_reason: str = "nsfw_scan_failed",
    ) -> int:
        pass  # TODO: Commercial logic

    async def fetch_nsfw_scan_cache(
        self,
        *,
        file_unique_id: str,
        kind: MediaKind | str,
        provider: str,
        model_name: str,
    ):
        pass  # TODO: Commercial logic

    async def fetch_media_scan_evidence(
        self,
        *,
        chat_id: int,
        file_unique_id: str,
        kind: MediaKind | str,
    ):
        pass  # TODO: Commercial logic

    async def upsert_nsfw_scan_cache(
        self,
        *,
        file_unique_id: str,
        kind: MediaKind | str,
        provider: str,
        model_name: str,
        safety_status: MediaSafetyStatus,
        safety_reason: str,
        scores: dict[str, Any] | None = None,
        model_version: str | None = None,
        max_pornography_score: float | None = None,
        max_hentai_score: float | None = None,
        max_sensual_score: float | None = None,
        frames_checked: int = 0,
        content_hash: str | None = None,
        phash: str | None = None,
        error: str | None = None,
    ) -> None:
        pass  # TODO: Commercial logic

    async def apply_nsfw_scan_result(
        self,
        *,
        asset_id: int,
        result: NSFWScanResult,
        job_id: int | None = None,
    ) -> int:
        pass  # TODO: Commercial logic

    async def claim_nsfw_alert(
        self,
        *,
        asset_id: int,
        chat_id: int,
        verdict: str,
    ):
        pass  # TODO: Commercial logic

    async def fetch_nsfw_alert_payload(self, *, asset_id: int):
        pass  # TODO: Commercial logic

    async def mark_nsfw_alert_media_sent(
        self,
        *,
        alert_id: int,
        media_message_id: int,
    ) -> None:
        pass  # TODO: Commercial logic

    async def mark_nsfw_alert_sent(
        self,
        *,
        alert_id: int,
        media_message_id: int,
        metadata_message_id: int,
    ) -> None:
        pass  # TODO: Commercial logic

    async def mark_nsfw_alert_error(
        self,
        *,
        alert_id: int,
        error_stage: str,
        error_type: str,
    ) -> None:
        pass  # TODO: Commercial logic

    async def fetch_nsfw_alert_by_id(self, alert_id: int):
        pass  # TODO: Commercial logic

    async def claim_nsfw_alert_action(
        self,
        *,
        alert_id: int,
        action: str,
        acted_by_user_id: int,
    ):
        pass  # TODO: Commercial logic

    async def complete_nsfw_alert_action(
        self,
        *,
        alert_id: int,
        action: str,
        acted_by_user_id: int,
    ) -> None:
        pass  # TODO: Commercial logic

    async def release_nsfw_alert_action(
        self,
        *,
        alert_id: int,
        action: str,
        acted_by_user_id: int,
    ) -> None:
        pass  # TODO: Commercial logic

    async def set_nsfw_human_label(
        self,
        *,
        alert_id: int,
        human_label: str,
        labeled_by_user_id: int,
    ):
        pass  # TODO: Commercial logic

    async def fetch_nsfw_human_label_for_alert(self, *, alert_id: int):
        pass  # TODO: Commercial logic

    async def fetch_current_nsfw_human_labels(self):
        pass  # TODO: Commercial logic

    async def fetch_memory_retention_settings(self, chat_id: int) -> tuple[int, int, int]:
        pass  # TODO: Commercial logic

    async def cleanup_chat_messages(
        self,
        chat_id: int,
        *,
        max_messages: int = DEFAULT_MEMORY_MAX_MESSAGES,
        retention_days: int = DEFAULT_MEMORY_RETENTION_DAYS,
        batch_size: int = DEFAULT_CLEANUP_BATCH_SIZE,
    ) -> int:
        pass  # TODO: Commercial logic

    async def cleanup_learning_events(
        self,
        chat_id: int,
        *,
        retention_days: int = DEFAULT_LEARNING_LOG_RETENTION_DAYS,
        batch_size: int = DEFAULT_CLEANUP_BATCH_SIZE,
    ) -> int:
        pass  # TODO: Commercial logic

    async def get_chat_memory(self, chat_id: int) -> ChatMemory | None:
        pass  # TODO: Commercial logic

    async def get_user_memory(self, chat_id: int, user_id: int) -> UserMemory | None:
        pass  # TODO: Commercial logic
