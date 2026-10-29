from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter

from ...variables_and_funcs import delete_after_delay, is_owner, is_chat_creator, apply_replacements
from ...crud_tables.table_users import update_msg_count
from ...crud_tables.table_stats import update_req_count
from ...crud_tables.table_texts import update_global_welcome_text, update_intro_text
from ...states import Owner
from ...kbs import delete_ikb_like_back
from ...db import db

router = Router()

@router.message(Command("привет", prefix="!"))
async def add_moder_for_group(message: Message):
    pass  # TODO: Commercial logic

@router.message(Command("интро", prefix="!"))
async def add_moder_for_group(message: Message):
    pass  # TODO: Commercial logic

@router.callback_query(F.data == "global_welcome_text")
async def add_moder_for_group(query: CallbackQuery, state: FSMContext):
    pass  # TODO: Commercial logic

@router.message(StateFilter(Owner.welcome_text))
async def process_name(message: Message, state: FSMContext) -> None:
    pass  # TODO: Commercial logic
