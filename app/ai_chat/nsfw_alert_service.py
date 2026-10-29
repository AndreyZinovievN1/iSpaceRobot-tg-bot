from __future__ import annotations

import html
import logging
from dataclasses import dataclass
from typing import Any, Awaitable, Callable

from app.ai_chat.models import MediaSafetySource, MediaSafetyStatus
from app.ai_chat.nsfw_config import nsfw_benchmark_ui_enabled
from app.ai_chat.nsfw_types import NSFWScanResult, NSFWVerdict
from app.ai_chat.repository import AIChatRepository, row_get
from app.crud_tables.table_ai_chat_media import normalize_metadata
from app.logs.logs import (
    NSFWAlertSendError,
    NSFWAlertSendResult,
    resolve_nsfw_alert_telegram_context,
    send_nsfw_moderation_alert,
)


logger = logging.getLogger(__name__)

AlertSender = Callable[..., Awaitable[NSFWAlertSendResult]]

TERMINAL_ALERT_REASONS = {
    "unsupported",
    "too_large",
    "extractor_timeout",
    "extractor_error",
    "extractor_unexpected",
    "provider_error",
    "provider_unexpected",
    "worker_interrupted",
    "worker_unexpected",
}

TERMINAL_REASON_LABELS = {
    "unsupported": "Формат не поддерживается безопасным сканером",
    "too_large": "Файл превышает безопасный лимит проверки",
    "extractor_timeout": "Превышено время извлечения кадров из файла",
    "extractor_error": "Не удалось извлечь кадры из файла",
    "extractor_unexpected": "Внутренняя ошибка извлечения кадров",
    "provider_error": "Классификатор завершил проверку с ошибкой",
    "provider_unexpected": "Внутренняя ошибка классификатора",
}

TERMINAL_REASON_LABELS.update(
    {
        "worker_interrupted": "Проверка была аварийно прервана после исчерпания попыток",
        "worker_unexpected": "Внутренняя ошибка обработки файла",
    }
)

TERMINAL_KIND_LABELS = {
    "photo": "Фото",
    "video": "Видео",
    "animation": "GIF",
    "document_animation": "GIF",
    "sticker": "Стикер",
}


@dataclass(frozen=True, slots=True)
class NSFWAlertActionResult:
    success: bool
    status: str
    idempotent: bool = False


@dataclass(frozen=True, slots=True)
class NSFWAlertLabelResult:
    success: bool
    human_label: str
    idempotent: bool = False


BENCHMARK_LABEL_NOTICE = (
    "Разметка используется только для тестирования моделей "
    "и не разрешает файл боту."
)


def _safe_value(value: Any) -> str:
    pass  # TODO: Commercial logic


def _percent_value(scores: dict[str, Any], name: str) -> str:
    pass  # TODO: Commercial logic


def build_nsfw_alert_text(
    *,
    alert_id: int,
    asset_id: int,
    payload: Any,
    result: NSFWScanResult,
    scan_job_id: int | None,
    group_html: str = "Группа",
    sender_html: str = "—",
    message_html: str = "—",
) -> str:
    pass  # TODO: Commercial logic


def build_nsfw_terminal_alert_text(
    *,
    alert_id: int,
    asset_id: int,
    payload: Any,
    terminal_reason: str,
    scan_job_id: int | None,
) -> str:
    pass  # TODO: Commercial logic


def _alert_key_for_result(result: NSFWScanResult) -> str | None:
    pass  # TODO: Commercial logic


class NSFWAlertService:
    def __init__(
        self,
        db,
        *,
        repository: AIChatRepository | None = None,
        sender: AlertSender = send_nsfw_moderation_alert,
    ) -> None:
        pass  # TODO: Commercial logic

    async def process_scan_result(
        self,
        *,
        asset_id: int,
        chat_id: int,
        job_id: int | None,
        result: NSFWScanResult,
    ) -> bool:
        pass  # TODO: Commercial logic

    async def _record_send_error(
        self,
        *,
        alert_id: int,
        asset_id: int,
        verdict: str,
        exc: NSFWAlertSendError,
    ) -> None:
        pass  # TODO: Commercial logic

    async def fetch_alert(self, alert_id: int):
        pass  # TODO: Commercial logic

    async def fetch_human_label(self, *, alert_id: int):
        pass  # TODO: Commercial logic

    async def apply_human_label(
        self,
        *,
        alert_id: int,
        human_label: str,
        labeled_by_user_id: int,
    ) -> NSFWAlertLabelResult:
        pass  # TODO: Commercial logic

    async def apply_action(
        self,
        *,
        alert_id: int,
        action: str,
        acted_by_user_id: int,
    ) -> NSFWAlertActionResult:
        pass  # TODO: Commercial logic
