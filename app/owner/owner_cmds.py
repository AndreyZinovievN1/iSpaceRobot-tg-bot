from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters.command import Command
from aiogram.exceptions import TelegramBadRequest
import asyncio
from asyncio import sleep
import time
from datetime import datetime
from pytz import timezone

import pysqlite3
import sys
sys.modules["sqlite3"] = pysqlite3

from ..crud_tables.table_transactions import create_transaction_and_trim
from ..kbs import when_groups_blacklist_ikb, when_users_blacklist_ikb
from ..variables_and_funcs import delete_after_delay, is_owner
from ..logs.logs import log_user_get_starcoins, log_user_lost_starcoins
from app.user_bot.cleaner_logic import is_running, parse_clean_mode, run_daily_clean
from ..crud_tables.table_users import get_user_by_chat_id, update_msg_count, update_starcoins
from ..crud_tables.table_log_group import update_log_group
from ..crud_tables.table_log_group import get_log_group_id
from ..crud_tables.table_stats import update_req_count, update_users_count
from ..crud_tables.table_settings import update_members_count
from ..db import db
from config import bot, logger
from app.shutdown import cancel_tasks

router = Router()

# Ссылки на фоновые задачи уборки (чтобы их не собрал сборщик мусора)
_clean_tasks: set = set()


def _clean_task_done(task) -> None:
    pass  # TODO: Commercial logic


async def stop_clean_tasks() -> None:
    """Отменяет ручные запуски уборки при остановке бота."""
    pass  # TODO: Commercial logic


@router.message(Command("логи", prefix="!"))
async def add_moder_for_group(message: Message):
    pass  # TODO: Commercial logic

@router.message(Command("очистка", prefix="!"))
async def cmd_daily_clean(message: Message):
    pass  # TODO: Commercial logic

@router.message(Command("чс", prefix="!"))
async def create_rp_cmd_handler(message: Message):
    pass  # TODO: Commercial logic

@router.callback_query(F.data == "users_blacklist")
async def adult_rp_cmds(query: CallbackQuery):
    pass  # TODO: Commercial logic

@router.callback_query(F.data == "groups_blacklist")
async def adult_rp_cmds(query: CallbackQuery):
    pass  # TODO: Commercial logic

@router.message(Command("вали", prefix="!"))
async def leave_chat_cmd(message: Message):
    pass  # TODO: Commercial logic


@router.message(Command("астроны", prefix="+"))
async def give_starcoins(message: Message):
    pass  # TODO: Commercial logic

@router.message(Command("астроны", prefix="-"))
async def remove_starcoins(message: Message):
    pass  # TODO: Commercial logic


@router.message(Command("считать", prefix="!"))
async def leave_chat_cmd(message: Message):
    pass  # TODO: Commercial logic

@router.message(Command("ce", prefix="!"))
async def get_custom_emoji_ids(message: Message):
    pass  # TODO: Commercial logic
