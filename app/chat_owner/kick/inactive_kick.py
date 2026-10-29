from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
import re
from datetime import datetime, timedelta

from app.variables_and_funcs import is_chat_creator
from config import bot, logger
from app.kbs import (
    kick_inactive_ikb, kick_inactive_by_period_ikb, back_to_kick_inactive_ikb
)
from app.states import ChatOwner
from app.db import db

router = Router()

@router.callback_query(F.data == "kick_inactive")
async def settings(query: CallbackQuery, state: FSMContext):
    pass  # TODO: Commercial logic

@router.callback_query(F.data == "kick_inactive_by_count")
async def settings(query: CallbackQuery, state: FSMContext):
    pass  # TODO: Commercial logic

@router.callback_query(F.data == "kick_inactive_by_period")
async def settings(query: CallbackQuery):
    pass  # TODO: Commercial logic

@router.callback_query(F.data.startswith("inactive_kick_by_count_"))
async def kick_inactive_by_count(query: CallbackQuery):
    pass  # TODO: Commercial logic


@router.callback_query(lambda c: c.data.startswith("_inactive_kick_by_period_"))
async def kick_inactive_by_period(query: CallbackQuery):
    pass  # TODO: Commercial logic


@router.callback_query(F.data.startswith("inactive_kick_limit_"))
async def kick_inactive_with_limit(query: CallbackQuery):
    pass  # TODO: Commercial logic
