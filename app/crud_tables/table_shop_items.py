from config import logger
from app.db import db


async def add_shop_item(category: str, text_m: str, text_f: str | None, price: int):
    pass  # TODO: Commercial logic


async def get_shop_items_by_category(category: str):
    pass  # TODO: Commercial logic


async def get_item_info(item_id: int):
    pass  # TODO: Commercial logic


async def remove_shop_item(item_id: int):
    pass  # TODO: Commercial logic
