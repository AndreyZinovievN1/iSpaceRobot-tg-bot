from __future__ import annotations

import html
import logging

from aiogram import F, Router
from aiogram.types import CallbackQuery

from app.ai_chat.nsfw_alert_service import NSFWAlertService
from app.ai_chat.nsfw_config import nsfw_benchmark_ui_enabled
from app.crud_tables.table_ai_chat_helpers import row_get
from app.crud_tables.table_log_group import get_log_group_id
from app.db import db
from app.logs.logs import (
    NSFW_MODERATION_TOPIC_ID,
    nsfw_alert_keyboard,
    nsfw_benchmark_confirmation_keyboard,
    nsfw_benchmark_label_keyboard,
)
from app.variables_and_funcs import is_owner


logger = logging.getLogger(__name__)
router = Router()

ACTION_LABELS = {
    "block": "blocked",
    "pending": "pending",
    "delete": "deleted",
}
BENCHMARK_LABELS = {
    "safe": "✅ Безопасно",
    "porn": "🔞 Порно",
    "hentai": "🎨 Хентай",
    "borderline": "🟡 Пограничное",
    "unusable": "⚫ Не удалось определить",
}
BENCHMARK_LABEL_NAMES = {
    "safe": "Безопасно",
    "porn": "Порно",
    "hentai": "Хентай",
    "borderline": "Пограничное",
    "unusable": "Не удалось определить",
}


def _parse_callback(data: str | None) -> tuple[str, int] | None:
    pass  # TODO: Commercial logic


def _parse_label_callback(data: str | None) -> tuple[str, int] | None:
    pass  # TODO: Commercial logic


def _parse_label_confirmation_callback(
    data: str | None,
) -> tuple[str, str, int] | None:
    pass  # TODO: Commercial logic


def _parse_label_cancel_callback(data: str | None) -> int | None:
    pass  # TODO: Commercial logic


def _with_action_status(text: str, *, status: str, idempotent: bool) -> str:
    pass  # TODO: Commercial logic


async def _edit_action_message(
    query: CallbackQuery,
    *,
    alert_id: int,
    status: str,
    idempotent: bool,
) -> None:
    pass  # TODO: Commercial logic


def _with_benchmark_label(text: str, *, human_label: str) -> str:
    pass  # TODO: Commercial logic


def _without_label_confirmation(text: str) -> str:
    pass  # TODO: Commercial logic


def _with_label_confirmation(
    text: str,
    *,
    current_label: str,
    new_label: str,
) -> str:
    pass  # TODO: Commercial logic


async def _edit_label_confirmation(
    query: CallbackQuery,
    *,
    alert_id: int,
    current_label: str,
    new_label: str,
) -> None:
    pass  # TODO: Commercial logic


async def _cancel_label_confirmation(
    query: CallbackQuery,
    *,
    alert_id: int,
) -> None:
    pass  # TODO: Commercial logic


async def _edit_label_message(
    query: CallbackQuery,
    *,
    alert_id: int,
    human_label: str,
) -> None:
    pass  # TODO: Commercial logic


@router.callback_query(F.data.startswith("owner:nsfw:"))
async def handle_nsfw_alert_action(query: CallbackQuery) -> None:
    pass  # TODO: Commercial logic
