from aiogram import Router
from aiogram.types import Message
from aiogram.filters.command import Command, CommandObject
import re

from app.variables_and_funcs import is_owner, delete_after_delay
from app.crud_tables.table_users import get_user_by_chat_id, update_msg_count
from app.crud_tables.table_stats import update_req_count
from app.crud_tables.table_admins import add_admin, get_admin_by_chat, remove_admin, update_admin_broadcast_flag

router = Router()

@router.message(Command("агент", prefix="+"))
async def add_moder_for_group(message: Message, command: CommandObject):
    pass  # TODO: Commercial logic

@router.message(Command("агент", prefix="-"))
async def remove_moder_for_group(message: Message, command: CommandObject):
    pass  # TODO: Commercial logic
