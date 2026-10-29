from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters.command import Command
import re

from app.variables_and_funcs import ( 
    TUTORIAL_TO_ADD_GRP_CMD, is_owner, delete_after_delay
)
from app.crud_tables.table_users import update_msg_count
from app.crud_tables.table_stats import update_req_count
from app.crud_tables.table_catalog_gifs import get_gif_from_catalog_by_id, delete_gif_from_catalog

router = Router()

@router.message(Command("гиф", prefix="-"))
async def create_rp_cmd_handler(message: Message):
    pass  # TODO: Commercial logic
