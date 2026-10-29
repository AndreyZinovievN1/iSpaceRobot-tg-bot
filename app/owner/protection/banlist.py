from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters.command import Command
from aiogram.exceptions import TelegramBadRequest

from app.kbs import when_banlist_ikb
from app.variables_and_funcs import delete_after_delay, is_owner, is_user_in_group
from app.logs.logs import log_add_user_to_banlist, log_delete_user_from_banlist
from app.crud_tables.table_users import update_msg_count, get_user_by_chat_id, get_user_groups
from app.crud_tables.table_stats import update_req_count
from app.crud_tables.table_banlist import add_user_to_banlist, is_user_in_banlist, delete_user_from_banlist
from config import bot
from app.db import db

router = Router()

@router.message(Command("бан", prefix="+"))
async def create_rp_cmd_handler(message: Message):
    pass  # TODO: Commercial logic

@router.message(Command("бан", prefix="-"))
async def create_rp_cmd_handler(message: Message):
    pass  # TODO: Commercial logic

@router.message(Command("банлист", prefix="!"))
async def create_rp_cmd_handler(message: Message):
    pass  # TODO: Commercial logic

@router.callback_query(F.data == "banlist")
async def adult_rp_cmds(query: CallbackQuery):
    pass  # TODO: Commercial logic
