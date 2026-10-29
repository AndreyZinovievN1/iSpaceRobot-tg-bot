from aiogram import Router, F
from aiogram.types import Message, ChatPermissions
from datetime import datetime, timedelta

from app.logs.logs import log_new_member
from app.crud_tables.table_users import update_msg_count
from app.crud_tables.table_users_in_private import get_user_in_private_by_chat, add_user_in_private
from app.crud_tables.table_users_blacklist import is_user_in_blacklist
from config import bot

router = Router()

@router.message(F.chat.type == "private")
async def private_filter(message: Message):
        
    pass  # TODO: Commercial logic
