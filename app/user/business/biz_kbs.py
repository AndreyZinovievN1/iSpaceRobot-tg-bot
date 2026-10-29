from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters.callback_data import CallbackData

from app.lang import tr_chat


class BizStyleCallback(CallbackData, prefix="biz_sty"):
    action: str  # Например: "set"
    style: str   # Например: "poetic", "science" и т.д.

class ClientsCallback(CallbackData, prefix="cls"):
    page: int

class HistoryCallback(CallbackData, prefix="hist"):
    user_id: int
    page: int

async def get_business_ikb(user_id: int):
    pass  # TODO: Commercial logic

business_back_ikb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="⬅️ Назад", callback_data="business")]
    ]
)

def get_history_kb(current_page: int, total_pages: int):
    pass  # TODO: Commercial logic

# reminders_ikb = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [InlineKeyboardButton(text="", callback_data="business_AI")],
#         [InlineKeyboardButton(text="💾 База", callback_data="business_base")],
#         [InlineKeyboardButton(text="📢 РП команды", callback_data="business_rp_cmds")],
#         [InlineKeyboardButton(text="🔔 Напоминания", callback_data="business_reminders")],
#         [InlineKeyboardButton(text="📊 Статистика", callback_data="business_statistic")],
#         [InlineKeyboardButton(text="📩 Рассылка", callback_data="business_broadcast")],
#         [InlineKeyboardButton(text="🗂️ История чата", callback_data="chat_history")],
#         [InlineKeyboardButton(text="Мой VIP 💎", callback_data="vip")],
#     ]
# )
# Список клиентов

def get_clients_kb(clients, page: int, total_pages: int):
    pass  # TODO: Commercial logic

# История конкретного чата
def get_history_kb(user_id: int, page: int, total_pages: int):
    pass  # TODO: Commercial logic

async def choose_vip_style_ikb(is_active: bool, response_mode: str = "outside_hours"):
    pass  # TODO: Commercial logic
