from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter

from app.kbs import back_to_chat_management_ikb
from app.variables_and_funcs import delete_after_delay, is_chat_creator
from app.crud_tables.table_users import update_msg_count
from app.crud_tables.table_stats import update_req_count
from app.crud_tables.table_settings import update_welcome_text, get_settings_by_group_id
from app.states import ChatOwner
from app.db import db
from app.lang import tr_msg

router = Router()

@router.callback_query(F.data == "welcome_text")
async def add_moder_for_group(query: CallbackQuery, state: FSMContext):
    pass  # TODO: Commercial logic


@router.message(StateFilter(ChatOwner.welcome_text))
async def process_name(message: Message, state: FSMContext) -> None:
    pass  # TODO: Commercial logic
