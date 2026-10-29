from aiogram import Router
from aiogram.types import Message
from aiogram.filters.command import Command
from aiogram.exceptions import TelegramBadRequest, TelegramForbiddenError

from app.variables_and_funcs import is_owner_or_admin, delete_after_delay
from app.logs.logs import (
    log_add_user_to_blacklist, log_add_group_to_blacklist,
    log_delete_chat_from_blacklist, log_delete_user_from_blacklist,
    log_bot_left
)
from app.crud_tables.table_users import update_msg_count
from app.crud_tables.table_stats import update_req_count
from app.crud_tables.table_admins import remove_admin
from app.crud_tables.table_groups_blacklist import (
    add_group_to_blacklist, is_group_in_blacklist, delete_group_from_blacklist
)
from app.crud_tables.table_users_blacklist import (
    add_user_to_blacklist, is_user_in_blacklist, delete_user_from_blacklist
)
from config import bot

router = Router()

@router.message(Command("чс", prefix="+"))
async def create_rp_cmd_handler(message: Message):
    pass  # TODO: Commercial logic

@router.message(Command("чс", prefix="-"))
async def create_rp_cmd_handler(message: Message):
    pass  # TODO: Commercial logic
