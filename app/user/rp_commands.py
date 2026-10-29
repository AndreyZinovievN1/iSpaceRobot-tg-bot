from aiogram import Router
from aiogram.types import Message

from app.filters.rp_filter import IsRPCommand
from app.crud_tables.table_stats import update_req_count

router = Router()
    
@router.message(IsRPCommand())
async def rp_handler(message: Message, rp_data: dict, is_global: bool):
    pass  # TODO: Commercial logic
