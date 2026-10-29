from aiogram import Router
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import BaseFilter
import asyncio

from .db import db 
from .crud_tables.table_users import get_user_by_chat_id, update_msg_count
from config import bot

update_user_data_router = Router()

class TrackUserChangesFilter(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        pass  # TODO: Commercial logic

from aiogram import Router
from aiogram import Bot
from aiogram.types import Message
from aiogram.filters import BaseFilter
from .db import Database
from .crud_tables.table_users import get_user_by_chat_id, update_msg_count
from config import bot

update_user_data_router = Router()

user_last_data = {}

class TrackUserChangesFilter(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        pass  # TODO: Commercial logic

@update_user_data_router.message(TrackUserChangesFilter())
async def track_user_changes(message: Message):
    pass  # TODO: Commercial logic
