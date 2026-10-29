from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters.command import Command
from asyncio import sleep
import time

# Импорты из твоего проекта
from app.variables_and_funcs import delete_after_delay, is_owner
from app.logs.daily_logs import log_daily_clear
from app.crud_tables.table_users import update_msg_count
from app.crud_tables.table_log_group import get_log_group_id
from app.crud_tables.table_stats import update_req_count, update_users_count
from app.crud_tables.table_settings import update_members_count
from app.db import db
from config import bot

router = Router()

@router.message(Command("очистка", prefix="!"))
async def cmd_clear_daily_logs(message: Message):
    """Команда для ручной очистки ежедневных логов"""
    pass  # TODO: Commercial logic


@router.message(Command("считать", prefix="!"))
async def cmd_count_users(message: Message):
    """Тяжелая команда подсчета всех пользователей во всех чатах"""
    pass  # TODO: Commercial logic
