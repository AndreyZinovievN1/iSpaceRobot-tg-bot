from datetime import datetime
from pytz import timezone

from config import logger
from app.db import db

MSK_TZ = timezone("Europe/Moscow")


async def add_vip_user(user_id: int, start_date: datetime, end_date: datetime):
    pass  # TODO: Commercial logic


async def remove_vip_user(user_id: int):
    pass  # TODO: Commercial logic


async def get_vip_user(user_id: int):
    pass  # TODO: Commercial logic


async def update_vip_expiry(user_id: int, new_end_date: datetime):
    pass  # TODO: Commercial logic


async def is_user_vip(user_id: int) -> bool:
    """
    Безопасная проверка VIP с таймзоной.
    Решает проблему aware/naive datetime (когда end_date из БД с tz, а datetime.now() без tz).
    """
    pass  # TODO: Commercial logic
