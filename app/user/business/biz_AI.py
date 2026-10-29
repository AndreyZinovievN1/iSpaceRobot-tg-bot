from aiogram import F, Router, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
import datetime
import pytz

from config import bot, logger
from app.kbs import cancel_ikb
from app.user.business.biz_kbs import choose_vip_style_ikb, BizStyleCallback
from app.crud_tables.table_biz_ai import (
    get_biz_ai_settings, update_biz_ai_description, can_update_biz_ai_prompt, 
    update_biz_ai_style, toggle_biz_ai, update_biz_ai_mode
)
from app.AI import generate_response
from app.states import BizAiSetupState

router = Router()

# Твоя функция проверки времени
def is_outside_working_hours(opening_hours):
    pass  # TODO: Commercial logic

FRIENDLY_NAMES = {
    "vip_poetic": "Поэтичный 🎭",
    "vip_science": "Научный 🧠",
    "vip_friendly": "Дружеский 💬",
    "vip_official": "Официальный 📖"
}

MODE_TEXTS = {
    "always": "🕒 Отвечать всегда",
    "work_hours": "👔 В рабочее время",
    "outside_hours": "🌙 В нерабочее время"
}

async def render_biz_settings(query: CallbackQuery, bot: Bot, user_id: int):
    """Единая точка отрисовки меню настроек"""
    pass  # TODO: Commercial logic

# Твоя функция сжатия
async def summarize_business_text(raw_text: str):
    pass  # TODO: Commercial logic

# Переключение режима
@router.callback_query(F.data == "biz_cycle_mode")
async def cycle_biz_mode_handler(query: CallbackQuery, bot: Bot):
    pass  # TODO: Commercial logic

# Смена стиля
@router.callback_query(BizStyleCallback.filter(F.action == "set"))
async def set_biz_style_handler(query: CallbackQuery, callback_data: BizStyleCallback, bot: Bot):
    pass  # TODO: Commercial logic

# Вкл/Выкл статус
@router.callback_query(F.data.startswith("biz_toggle_"))
async def toggle_biz_status_handler(query: CallbackQuery, bot: Bot):
    pass  # TODO: Commercial logic

@router.callback_query(F.data == "biz_change_prompt")
async def start_biz_desc_callback(query: CallbackQuery, state: FSMContext):
    pass  # TODO: Commercial logic

@router.message(BizAiSetupState.waiting_for_description, F.text)
async def process_biz_description(message: Message, state: FSMContext):
    pass  # TODO: Commercial logic

STYLING_MAP = {
    "vip_poetic": "Твой стиль: Поэтичный. Говори красиво, используй метафоры и изысканные обороты.",
    "vip_science": "Твой стиль: Научный. Говори строго, используй факты, термины и логику.",
    "vip_friendly": "Твой стиль: Дружеский. Говори тепло, просто, используй эмодзи и будь открытым.",
    "vip_official": "Твой стиль: Официальный. Говори сухо, по-деловому, соблюдай дистанцию и этикет."
}
