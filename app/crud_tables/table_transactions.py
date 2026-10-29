from typing import Optional
from datetime import datetime
from pytz import timezone
from config import logger
from app.db import db # Наш глобальный пул

MSK_TZ = timezone("Europe/Moscow")

async def create_transaction_and_trim(
    user_id: int,
    stars_amount: int,
    transaction_id: str,
    text: str,
    starcoins_amount: Optional[int] = None,
    trim_limit: int = 200,
):
    pass  # TODO: Commercial logic

async def get_last_transaction_by_user(user_id: int):
    pass  # TODO: Commercial logic

async def get_user_transactions(user_id: int, limit: int = 5, offset: int = 0):
    pass  # TODO: Commercial logic

async def count_user_transactions(user_id: int) -> int:
    pass  # TODO: Commercial logic

async def update_last_transaction(user_id: int, transaction_id: str, is_finish: bool):
    pass  # TODO: Commercial logic
