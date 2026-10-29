from config import logger
from app.db import db

async def create_allowed_link(link: str, group_id):
    pass  # TODO: Commercial logic

async def get_allowed_links_by_group_id(group_id: int):
    pass  # TODO: Commercial logic

async def allowed_link_exists(link: str, group_id: int) -> bool:
    pass  # TODO: Commercial logic

async def remove_allowed_link(link: str, group_id: int):
    pass  # TODO: Commercial logic
