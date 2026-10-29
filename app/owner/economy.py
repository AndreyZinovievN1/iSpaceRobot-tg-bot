from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters.command import Command
from aiogram.exceptions import TelegramBadRequest
from asyncio import sleep
import time

from ..kbs import when_groups_blacklist_ikb, when_users_blacklist_ikb
from ..variables_and_funcs import delete_after_delay, is_owner
from ..logs.logs import log_user_get_starcoins, log_user_lost_starcoins
from ..logs.daily_logs import log_daily_clear
from ..crud_tables.table_users import get_user_by_chat_id, update_msg_count, update_starcoins
from ..crud_tables.table_log_group import update_log_group
from ..crud_tables.table_log_group import get_log_group_id
from ..crud_tables.table_stats import update_req_count, update_users_count
from ..crud_tables.table_settings import update_members_count
from ..db import db
from config import bot

router = Router()

@router.message(Command("астроны", prefix="+"))
async def give_starcoins(message: Message):
    pass  # TODO: Commercial logic

@router.message(Command("астроны", prefix="-"))
async def remove_starcoins(message: Message):
    pass  # TODO: Commercial logic
