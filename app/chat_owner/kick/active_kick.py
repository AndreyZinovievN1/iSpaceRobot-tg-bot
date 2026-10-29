from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
import re
from datetime import datetime, timedelta

from app.variables_and_funcs import is_chat_creator
from config import bot, logger
from app.kbs import (
    kick_active_ikb, kick_active_by_period_ikb, back_to_kick_active_ikb
)
from app.states import ChatOwner
from app.db import db
from app.lang import get_tr

router = Router()

@router.callback_query(F.data == "kick_active")
async def settings(query: CallbackQuery, state: FSMContext):
    pass  # TODO: Commercial logic


@router.callback_query(F.data == "kick_active_by_count")
async def ask_count(query: CallbackQuery, state: FSMContext):
    pass  # TODO: Commercial logic


@router.callback_query(F.data == "kick_active_by_period")
async def ask_period(query: CallbackQuery):
    pass  # TODO: Commercial logic


@router.callback_query(F.data.startswith("active_kick_by_count_"))
async def kick_active_by_count(query: CallbackQuery):
    pass  # TODO: Commercial logic


@router.callback_query(F.data.startswith("_active_kick_by_period_"))
async def kick_active_by_period(query: CallbackQuery):
    pass  # TODO: Commercial logic


@router.callback_query(F.data.startswith("active_kick_limit_"))
async def kick_active_with_limit(query: CallbackQuery):
    pass  # TODO: Commercial logic
