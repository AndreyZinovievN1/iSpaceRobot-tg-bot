from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from datetime import timedelta, datetime
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter

from app.kbs import daily_rewards_keyboard
from app.variables_and_funcs import is_owner
from app.crud_tables.table_users import update_starcoins, update_coins
from app.crud_tables.table_daily_rewards import get_reward_by_day, set_reward
from app.crud_tables.table_user_daily_rewards import get_user_rewards, update_user_reward

router = Router()

async def claim_daily_reward(user_id: int):
    pass  # TODO: Commercial logic


@router.message(F.text == "/gift")
async def cmd_gift(message: Message):
    pass  # TODO: Commercial logic


@router.callback_query(F.data.startswith("reward_"))
async def handle_claim_reward(query: CallbackQuery):
    pass  # TODO: Commercial logic


@router.callback_query(F.data.startswith("reward_edit_"))
async def edit_reward(query: CallbackQuery, state: FSMContext):
    pass  # TODO: Commercial logic


@router.message(StateFilter("set_reward"))
async def save_reward(message: Message, state: FSMContext):
    pass  # TODO: Commercial logic
