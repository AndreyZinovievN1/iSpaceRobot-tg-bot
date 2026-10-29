import pytz
from datetime import datetime, time
from aiogram import Router, F
from aiogram.types import CallbackQuery

from ..kbs import night_mode_ikb
from ..variables_and_funcs import is_chat_creator
from ..crud_tables.table_night_mode import (
    add_night_mode, update_night_mode, get_night_mode_by_group_id, fetch_all_night_modes
)
from config import bot, scheduler
from ..lang import tr_chat


router = Router()

# --- ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ ---

async def send_night_start_notification(chat_id: int):
    pass  # TODO: Commercial logic

async def send_night_end_notification(chat_id: int):
    pass  # TODO: Commercial logic

async def setup_night_notification(chat_id):
    """Обновляет задачи в планировщике"""
    pass  # TODO: Commercial logic

async def sync_all_night_modes():
    """Запуск при старте бота"""
    pass  # TODO: Commercial logic

# --- ХЕНДЛЕРЫ МЕНЮ ---

@router.callback_query(F.data == "night_mode")
async def settings(query: CallbackQuery):
    pass  # TODO: Commercial logic

@router.callback_query(F.data == "on_off_night_mode")
async def toggle_night_mode(query: CallbackQuery):
    pass  # TODO: Commercial logic

@router.callback_query(F.data.startswith("confirmNightModeTime_"))
async def confirm_handler(query: CallbackQuery):
    pass  # TODO: Commercial logic

# --- КНОПКИ ФУНКЦИЙ (Удаление медиа, Тишина и т.д.) ---

async def update_line_night_mode(query: CallbackQuery, field: str):
    pass  # TODO: Commercial logic

@router.callback_query(F.data == "delete_media")
async def set_delete_media(query: CallbackQuery):
    pass  # TODO: Commercial logic

@router.callback_query(F.data == "global_silence")
async def set_global_silence(query: CallbackQuery):
    pass  # TODO: Commercial logic

@router.callback_query(F.data == "silence")
async def set_silence(query: CallbackQuery):
    pass  # TODO: Commercial logic

@router.callback_query(F.data == "night_mode_notify")
async def set_notify(query: CallbackQuery):
    pass  # TODO: Commercial logic
