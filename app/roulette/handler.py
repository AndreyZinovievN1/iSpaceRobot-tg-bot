import re
from aiogram import Router, F
from aiogram.types import Message

from app.roulette.roulette_kbs import roulette_menu
from app.variables_and_funcs import delete_after_delay
from app.roulette.functions import (
    recalc_tables_occupied, kick_from_roulette_after_60_sec, ROULETTE_TEXT,
    spawn_roulette_task,
)
from app.lang import tr_chat
from app.crud_tables.table_roulette_msgs import (
    get_roulette_msg, update_roulette_msg_text, add_roulette_msg
)
from config import bot

router = Router()

# Точный фильтр для ставок: "Число Пробел Что-угодно"
ROULETTE_REGEXP = r"^(\d+)\s+(.+)$"

@router.message(F.text.regexp(ROULETTE_REGEXP))
async def handle_roulette_bet(message: Message):
    # 1. Первичная проверка паттерна
    pass  # TODO: Commercial logic
