"""
/stats — графики активности

Верхний график: сообщения по часам за последние 24 часа (из user_activity_stats)
Нижний график: новые пользователи за 7 дней (из users через get_weekly_new_users)

Права:
- обычный пользователь: только свои данные (в личке это chat_id == user_id)
- админ/владелец чата/владелец бота: может запросить другого через reply или /stats <user_id>
"""

from __future__ import annotations

import io
from typing import Optional, Tuple, List, Dict

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, BufferedInputFile

from config import logger
from app.crud_tables.table_activity import get_daily_activity, get_weekly_new_users

# Функции доступа (у тебя уже есть в проекте)
from app.variables_and_funcs import (
    is_owner,
    is_admin,
    is_chat_admin,
    is_owner_or_admin,
)

# matplotlib
import matplotlib
matplotlib.use("Agg")  # важно для серверов без GUI
import matplotlib.pyplot as plt


router = Router()


# ---------- helpers ----------

def _extract_target_user_id(message: Message) -> Optional[int]:
    """
    Пытается получить target user_id:
    1) из reply (сообщение, на которое ответили)
    2) из аргумента: /stats 12345
    """
    pass  # TODO: Commercial logic


async def _has_rights_to_other(message: Message) -> bool:
    """
    Проверка прав: владелец/админ бота или админ чата.
    Важно: is_chat_admin обычно имеет смысл только в группах.
    """
    pass  # TODO: Commercial logic


def create_activity_graph(
    daily_data: List[Dict],
    weekly_data: List[Dict],
) -> io.BytesIO:
    """
    Рисует картинку 2-в-1:
    - сверху: bar (24 часа)
    - снизу: line (7 дней)

    Возвращает BytesIO (PNG).
    """
    pass  # TODO: Commercial logic


# ---------- handler ----------

@router.message(Command("stats"))
async def cmd_stats(message: Message) -> None:
    pass  # TODO: Commercial logic
