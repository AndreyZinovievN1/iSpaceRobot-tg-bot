from aiogram import Router
from aiogram.types import Message
from aiogram.filters.command import Command

from ..variables_and_funcs import (
    is_owner_or_admin, is_owner, is_admin, is_chat_creator, delete_after_delay,
)
from ..crud_tables.table_users import update_msg_count
from ..crud_tables.table_allowed_links import (
    create_allowed_link, allowed_link_exists, remove_allowed_link
)
from ..crud_tables.table_stats import update_req_count
from config import bot

manage_allowed_links_router = Router()

@manage_allowed_links_router.message(Command("ссылка", prefix="+"))
async def create_rp_cmd_handler(message: Message):
    pass  # TODO: Commercial logic

@manage_allowed_links_router.message(Command("ссылка", prefix="-"))
async def create_rp_cmd_handler(message: Message):
    pass  # TODO: Commercial logic
