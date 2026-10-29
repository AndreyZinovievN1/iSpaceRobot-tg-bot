from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters.command import Command

from app.user.donate.donate_kbs import donate_ikb
from app.user.donate.categories import build_donate_text

router = Router()


@router.message(Command("donate"))
async def donate_cmd(message: Message):
    pass  # TODO: Commercial logic


@router.callback_query(F.data == "donate_menu")
async def donate_menu_callback(callback: CallbackQuery):
    pass  # TODO: Commercial logic
