from aiogram.exceptions import (
    TelegramMigrateToChat, TelegramForbiddenError, TelegramNotFound
)
from asyncio import sleep
from ..db import db
from ..crud_tables.table_users import update_username
from ..crud_tables.table_stats import update_users_count
from ..crud_tables.table_settings import remove_settings, update_settings
from ..crud_tables.table_log_group import get_log_group_id
from config import bot

async def log_daily_clear():
    pass  # TODO: Commercial logic
