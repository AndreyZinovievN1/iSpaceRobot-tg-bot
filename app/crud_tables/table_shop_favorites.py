from config import logger
from app.db import db


async def add_shop_favorite(user_id: int, item_id: int):
    pass  # TODO: Commercial logic


async def remove_shop_favorite(user_id: int, item_id: int):
    pass  # TODO: Commercial logic


async def is_shop_favorite(user_id: int, item_id: int) -> bool:
    pass  # TODO: Commercial logic


async def toggle_shop_favorite(user_id: int, item_id: int) -> bool:
    pass  # TODO: Commercial logic


async def get_favorite_shop_items(user_id: int, categories: list[str] | None = None):
    pass  # TODO: Commercial logic
