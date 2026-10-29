from aiogram import Router
from aiogram.types import Message
from aiogram.filters.command import Command
from aiogram.exceptions import TelegramBadRequest
from aiogram.types import ChatMemberAdministrator

from pytz import timezone
from datetime import datetime
from dateutil.parser import isoparse

from app.variables_and_funcs import (
    is_owner_or_admin, is_owner, is_admin, delete_after_delay, get_group_owner
)
from app.logs.logs import (
    log_marriage_registration, log_marriage_divorce, log_user_get_coins, log_user_lost_coins
)

from app.crud_tables.table_transactions import create_transaction_and_trim
from app.crud_tables.table_marriages import create_marriage, get_marriage, delete_marriage
from app.crud_tables.table_users import update_msg_count, update_coins, get_user_by_chat_id
from app.crud_tables.table_stats import update_req_count
from config import bot

router = Router()

@router.message(Command("брак", prefix="+"))
async def force_marriage(message: Message):
    pass  # TODO: Commercial logic

@router.message(Command("брак", prefix="-"))
async def force_divorce(message: Message):
    pass  # TODO: Commercial logic


@router.message(Command("брак", prefix="!"))
async def force_divorce(message: Message):
    pass  # TODO: Commercial logic

@router.message(Command("монеты", prefix="+"))
async def give_coins(message: Message):
    pass  # TODO: Commercial logic

@router.message(Command("монеты", prefix="-"))
async def take_coins(message: Message):
    pass  # TODO: Commercial logic


@router.message(Command("группа", prefix="!"))
async def create_rp_cmd_handler(message: Message):
    pass  # TODO: Commercial logic


@router.message(Command("отправь", prefix="!"))
async def send_custom_message(message: Message):
    pass  # TODO: Commercial logic
