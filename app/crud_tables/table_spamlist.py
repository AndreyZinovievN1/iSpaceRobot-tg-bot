from config import logger
from app.db import db


async def add_user_to_spamlist(user_id: int, auto: bool = True, reason: str | None = None) -> bool:
    pass  # TODO: Commercial logic


async def is_user_in_spamlist(user_id: int) -> bool:
    pass  # TODO: Commercial logic


async def get_user_from_spamlist(user_id: int):
    pass  # TODO: Commercial logic


async def delete_user_from_spamlist(user_id: int):
    pass  # TODO: Commercial logic


async def clear_spamlist():
    pass  # TODO: Commercial logic
