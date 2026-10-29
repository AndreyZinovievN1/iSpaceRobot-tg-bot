from aiogram import Router, html
from aiogram.types import Message
from aiogram.filters.command import Command
import re

from app.variables_and_funcs import ( 
    TUTORIAL_TO_ADD_GRP_CMD, is_owner_or_admin, delete_after_delay
)
from app.crud_tables.table_users import update_msg_count
from app.crud_tables.table_stats import update_req_count
from app.crud_tables.table_global_rp_cmds import (
    create_global_rp_cmd, global_rp_cmd_exists, remove_global_rp_cmd
)

router = Router()

@router.message(Command("грп", prefix="+"))
async def create_rp_cmd_handler(message: Message):
    pass  # TODO: Commercial logic

@router.message(Command("грп", prefix="-"))
async def create_rp_cmd_handler(message: Message):
    pass  # TODO: Commercial logic
