from aiogram import Router, F
from aiogram.types import (
    Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
)
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter
from asyncio import sleep

from ..kbs import events_ikb, events_settings_ikb
from ..variables_and_funcs import is_chat_creator, delete_after_delay, get_group_owner
from ..crud_tables.table_events import add_events, update_events, get_events_by_group_id
from ..crud_tables.table_chat_owners import (
    create_chat_owner, get_chat_owner_by_chat_id, update_log_chat_id
)
from config import bot
from ..states import ChatOwner
from ..lang import tr_chat

router = Router()

@router.callback_query(F.data == "events")
async def settings(query: CallbackQuery, state: FSMContext):
    pass  # TODO: Commercial logic

@router.callback_query(F.data == "what_writing_to_channel")
async def settings(query: CallbackQuery):
    pass  # TODO: Commercial logic

async def update_event(query, event, word):
    pass  # TODO: Commercial logic
    
@router.callback_query(F.data == "introductions_event_info")
async def settings(query: CallbackQuery):
    pass  # TODO: Commercial logic
@router.callback_query(F.data == "introductions_event")
async def settings(query: CallbackQuery):
    # Pass the English event name as fallback instead of Russian
    pass  # TODO: Commercial logic

@router.callback_query(F.data == "exits_event_info")
async def settings(query: CallbackQuery):
    pass  # TODO: Commercial logic
@router.callback_query(F.data == "exits_event")
async def settings(query: CallbackQuery):
    pass  # TODO: Commercial logic

# @router.callback_query(F.data == "warnings_event_info")
# async def settings(query: CallbackQuery):
#     await query.answer(
#         "⚠️ Запись начисления/снятия предупреждений администраторами/модераторами.",
#         show_alert=True
#     )
# @router.callback_query(F.data == "warnings_event")
# async def settings(query: CallbackQuery):
#     await update_event(query, "warnings", "предупреждений")

@router.callback_query(F.data == "punishments_event_info")
async def settings(query: CallbackQuery):
    pass  # TODO: Commercial logic
@router.callback_query(F.data == "punishments_event")
async def settings(query: CallbackQuery):
    pass  # TODO: Commercial logic

@router.callback_query(F.data == "arab_event_info")
async def settings(query: CallbackQuery):
    pass  # TODO: Commercial logic
@router.callback_query(F.data == "arab_event")
async def settings(query: CallbackQuery):
    pass  # TODO: Commercial logic

@router.callback_query(F.data == "bot_added_event_info")
async def settings(query: CallbackQuery):
    pass  # TODO: Commercial logic
@router.callback_query(F.data == "bot_added_event")
async def settings(query: CallbackQuery):
    pass  # TODO: Commercial logic

@router.callback_query(F.data == "ban_mute_event_info")
async def settings(query: CallbackQuery):
    pass  # TODO: Commercial logic
@router.callback_query(F.data == "ban_mute_event")
async def settings(query: CallbackQuery):
    pass  # TODO: Commercial logic

@router.callback_query(F.data == "admin_event_info")
async def settings(query: CallbackQuery):
    pass  # TODO: Commercial logic
@router.callback_query(F.data == "admin_event")
async def settings(query: CallbackQuery):
    pass  # TODO: Commercial logic

@router.callback_query(F.data == "settings_event_info")
async def settings(query: CallbackQuery):
    pass  # TODO: Commercial logic
@router.callback_query(F.data == "settings_event")
async def settings(query: CallbackQuery):
    pass  # TODO: Commercial logic

@router.callback_query(F.data == "role_event_info")
async def settings(query: CallbackQuery):
    pass  # TODO: Commercial logic
@router.callback_query(F.data == "role_event")
async def settings(query: CallbackQuery):
    pass  # TODO: Commercial logic

@router.callback_query(F.data == "change_log_group")
async def change_log_group(query: CallbackQuery, state: FSMContext):
    pass  # TODO: Commercial logic

@router.message(StateFilter(ChatOwner.log_group_id))
async def process_name(message: Message, state: FSMContext) -> None:
    pass  # TODO: Commercial logic

@router.callback_query(F.data == "delete_log_group")
async def change_log_group(query: CallbackQuery):
    pass  # TODO: Commercial logic
