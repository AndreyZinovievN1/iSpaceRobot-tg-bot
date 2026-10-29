from config import logger
from app.db import db

async def add_channel_to_control(channel_id: int, owner_id: int):
    pass  # TODO: Commercial logic

async def update_channels_to_control(channel_id: int, subs_count: int, diff: int):
    pass  # TODO: Commercial logic

async def get_channel_to_control(channel_id: int):
    pass  # TODO: Commercial logic

async def delete_channel_to_control(channel_id: int):
    pass  # TODO: Commercial logic

async def get_channels_by_owner(owner_id: int):
    pass  # TODO: Commercial logic
