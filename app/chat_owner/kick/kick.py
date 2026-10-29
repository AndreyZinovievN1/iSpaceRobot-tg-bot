from aiogram import Router, F
from aiogram.types import CallbackQuery

from app.variables_and_funcs import is_chat_creator
from app.kbs import kick_ikb

router = Router()

@router.callback_query(F.data == "kick_menu")
async def settings(query: CallbackQuery):
    pass  # TODO: Commercial logic
