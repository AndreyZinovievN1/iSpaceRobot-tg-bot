from config import logger
from app.db import db


async def create_business_rp_cmd(user_id: int, cmd: str, text: str, gif_id: str = None):
    pass  # TODO: Commercial logic


async def get_business_rp_cmds(user_id: int, cmd: str = None):
    """
    Если cmd передан -> вернет одну команду (dict) или None.
    Если cmd НЕ передан -> вернет список команд (list[dict]).
    """
    pass  # TODO: Commercial logic


async def business_rp_cmd_exists(user_id: int, cmd: str) -> bool:
    pass  # TODO: Commercial logic


async def remove_business_rp_cmd(user_id: int, cmd: str):
    pass  # TODO: Commercial logic
