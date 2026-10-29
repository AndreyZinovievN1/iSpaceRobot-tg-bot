from aiogram import Router, F
from aiogram.types import Message
from aiogram.types import ChatPermissions
from datetime import datetime, timedelta

from app.variables_and_funcs import is_owner_or_admin, is_chat_admin, tr_chat, delete_after_delay
from app.crud_tables.table_settings import get_settings_by_group_id
from config import bot
from app.db import db
from config import logger

router = Router()

@router.message(F.forward_from | F.forward_from_chat)
async def anti_forward_handler(message: Message):
    pass  # TODO: Commercial logic
