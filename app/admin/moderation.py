from aiogram import Router
from aiogram.types import Message, ChatPermissions, ChatMemberRestricted
from aiogram.filters.command import Command, CommandObject
from contextlib import suppress
from aiogram.exceptions import (
    TelegramBadRequest
)

from app.variables_and_funcs import (
    parse_time, get_group_owner,
    is_owner_or_admin, is_owner, is_chat_admin, is_chat_creator, is_admin, delete_after_delay, 

)
from app.crud_tables.table_chat_owners import get_chat_owner_by_chat_id
from app.crud_tables.table_users import update_msg_count
from app.crud_tables.table_stats import update_req_count
from config import bot
from app.lang import tr_msg

router = Router()

@router.message(Command("бан", prefix="!"))
async def cmd_ban(message: Message, command: CommandObject):
    pass  # TODO: Commercial logic

@router.message(Command("кик", prefix="!"))
async def cmd_kick(message: Message):
    pass  # TODO: Commercial logic

@router.message(Command("мут", prefix="!"))
async def mute(message: Message, command: CommandObject):
    pass  # TODO: Commercial logic

@router.message(Command("ремут", prefix="!"))
async def mute(message: Message, command: CommandObject):
    pass  # TODO: Commercial logic
