from html import escape
from random import choices
from string import ascii_letters, digits

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters.command import Command

from app.filters.migration_filter import IsMigrationKey
from app.variables_and_funcs import delete_after_delay, is_chat_creator
from app.crud_tables.table_users import update_msg_count
from app.crud_tables.table_stats import update_req_count
from app.crud_tables.table_migration_keys import add_migration_key, delete_migration_key
from app.crud_tables.table_settings import get_settings_by_group_id, update_msg_count_for_group
from app.lang import tr_msg, tr_chat
from config import bot

router = Router()

# ТВОЙ ID (исключение — можешь создавать ключ в любом чате)
OWNER_EXCEPTION_ID = 0  # TODO: Commercial logic


def _pack_key(raw_key: str, old_chat_id: int) -> str:
    # Храним old_chat_id внутри key, чтобы не менять таблицу
    pass  # TODO: Commercial logic


def _unpack_old_chat_id(packed_key: str) -> int:
    # packed_key: "K:<raw>|C:<old_chat_id>"
    pass  # TODO: Commercial logic


# --- 1) ОБРАБОТКА КЛЮЧА (вставили ключ в новый чат) ---

@router.message(IsMigrationKey())
async def handle_migration_execution(message: Message, migration_key: dict):
    # Пытаемся удалить сообщение с ключом (если нет прав — просто игнор)
    pass  # TODO: Commercial logic


# --- 2) ГЕНЕРАЦИЯ КЛЮЧА ЧЕРЕЗ КОМАНДУ !миграция ---

@router.message(Command("миграция", prefix="!"))
async def cmd_migration_start(message: Message):
    pass  # TODO: Commercial logic


# --- 3) ГЕНЕРАЦИЯ КЛЮЧА ЧЕРЕЗ CALLBACK ---

@router.callback_query(F.data == "migration")
async def cb_migration_start(query: CallbackQuery):
    # Уже было исключение по ID — оставляем
    pass  # TODO: Commercial logic


# --- ВСПОМОГАТЕЛЬНАЯ ФУНКЦИЯ ---

async def _create_and_send_migration_key(user_id: int, old_chat_id: int) -> str:
    # чистим старый ключ пользователя (если у тебя delete умеет только по chat_id=user_id)
    pass  # TODO: Commercial logic
