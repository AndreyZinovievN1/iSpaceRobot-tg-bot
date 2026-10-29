from aiogram import Router, F
from aiogram.types import CallbackQuery, ChatPermissions
from datetime import datetime, timedelta
import re

from app.variables_and_funcs import is_chat_creator
from config import bot, logger
from app.kbs import kick_nubs_by_period_ikb, kick_silence_by_period_ikb
from app.db import db

router = Router()

async def kick_users_by_activity(chat_id: int, users: list[dict], dt_limit: datetime = None, only_inactive: bool = False) -> int:
    """Универсальная функция кика пользователей по активности"""
    pass  # TODO: Commercial logic


@router.callback_query(F.data == "kick_nubs")
async def kick_nubs_settings(query: CallbackQuery):
    pass  # TODO: Commercial logic


@router.callback_query(lambda c: c.data.startswith("nubs_kick_by_period_"))
async def kick_nubs(query: CallbackQuery):
    pass  # TODO: Commercial logic


@router.callback_query(F.data == "kick_silence")
async def kick_silence_settings(query: CallbackQuery):
    pass  # TODO: Commercial logic


@router.callback_query(lambda c: c.data.startswith("silence_kick_by_period_"))
async def kick_silence(query: CallbackQuery):
    pass  # TODO: Commercial logic
