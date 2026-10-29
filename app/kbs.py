from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, SwitchInlineQueryChosenChat, WebAppInfo
from random import shuffle
from math import ceil

from .crud_tables.table_settings import get_settings_by_group_id
from .crud_tables.table_events import get_events_by_group_id
from .crud_tables.table_night_mode import get_night_mode_by_group_id
from .crud_tables.table_profile_settings import get_profile_settings_by_user_id
from .crud_tables.table_daily_rewards import get_all_rewards
from .crud_tables.table_user_daily_rewards import get_user_rewards
from .crud_tables.table_subs import get_all_subscriptions
from .crud_tables.table_owner import get_admin_mode
from .variables_and_funcs import timezones, is_owner
from .lang import tr_chat

subscribe_ikb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🔔 Подписаться", url="https://t.me/joinchat/WWfMOfVYyys1noNU")],
        [InlineKeyboardButton(text="✅ Я подписался", callback_data="check_subscribe")]
    ]
)

async def create_navigation_keyboard(current_page: int, total_pages: int, chat_id: int, way: str="top_banana") -> InlineKeyboardMarkup:
    pass  # TODO: Commercial logic

async def create_navigation_keyboard_for_spamlist(current_page: int, total_pages: int, chat_id: int, way: str="top_banana") -> InlineKeyboardMarkup:
    pass  # TODO: Commercial logic

async def get_box_keyboard():
    pass  # TODO: Commercial logic

back_to_main_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="⬅️ Назад", callback_data="back_to_main_menu")]
    ]
)

BOT_ADD_URL = (
    "https://t.me/iSpaceRobot"
    "?startgroup=true"
    "&admin=delete_messages+restrict_members+invite_users+manage_video_chats+manage_chat"
)

SUPPORT_URL = "https://t.me/joinchat/SAJ-A-ieCTNyfHq1"
NEWS_URL = "https://t.me/joinchat/WWfMOfVYyys1noNU"
HELP_GUIDES = "https://t.me/+S_WgppKEKgmktZjd"

# --- Space App (Mini App) и страница документации -------------------------
BOT_USERNAME = "iSpaceRobot"
MINI_APP_URL = "https://ispacerobot.space/"
# Раздел документации внутри Mini App: фронтенд читает этот параметр (?tab=docs).
MINI_APP_DOCS_URL = f"{MINI_APP_URL}?tab=docs"
# Дип-линк на Mini App с параметром запуска — для групп, где web_app-кнопки запрещены.
MINI_APP_DOCS_DEEP_LINK = f"https://t.me/{BOT_USERNAME}?startapp=docs"
DOCS_BUTTON_TEXT = "📖 Документация"


def docs_button(private: bool) -> InlineKeyboardButton:
    """
    Кнопка «Документация» для меню /help.

    В личке открываем раздел документации сразу в Mini App (`?tab=docs`).
    В группах Telegram не разрешает web_app-кнопки, поэтому ведём по
    дип-линку на Mini App со стартовым параметром `startapp=docs`.
    """
    pass  # TODO: Commercial logic

def help_back_kb():
    pass  # TODO: Commercial logic


async def help_menu_for_private(chat_id):
    pass  # TODO: Commercial logic


async def admin_help_menu_for_private(chat_id):
    pass  # TODO: Commercial logic


async def help_menu(chat_id):
    pass  # TODO: Commercial logic


async def admin_help_menu(chat_id):
    pass  # TODO: Commercial logic
    
def coin_offers_list_ikb(offers: list, exclude_id: int | None = None, is_owner: bool = False):
    pass  # TODO: Commercial logic


def coin_offer_detail_ikb(offer_id: int, offers: list, is_owner: bool = False):
    pass  # TODO: Commercial logic

def starcoin_offers_list_ikb(offers: list, exclude_id: int | None = None, is_owner: bool = False):
    pass  # TODO: Commercial logic


def starcoin_offer_detail_ikb(offer_id: int, offers: list, is_owner: bool = False):
    pass  # TODO: Commercial logic


async def bags_ikb(winning_bag: int):
    pass  # TODO: Commercial logic

# СВАДЬБЫ
async def wedding_ikb(chat_id, wife_id):
    pass  # TODO: Commercial logic

# РАЗВОД
async def divorce_ikb(user_id: int, starcoins: int, is_vip: bool, is_owner: bool = False, is_have_wedding: bool = True):
    pass  # TODO: Commercial logic

async def donate_ikb(user_id):
    pass  # TODO: Commercial logic

async def profile_ikb(user_id, is_have_muted, user_style=None, profile_settings=None):
    pass  # TODO: Commercial logic

async def profile_info_back_ikb(user_id, user_style=None):
    pass  # TODO: Commercial logic

def user_lang_menu_ikb(chat_id: int):
    pass  # TODO: Commercial logic

async def choose_vip_plan_ikb(user_id: int):
    pass  # TODO: Commercial logic

async def subs_admin_ikb():
    pass  # TODO: Commercial logic

async def profile_settings_ikb(user_id: int):
    pass  # TODO: Commercial logic

async def transactions_delete_ikb(user_id):
    pass  # TODO: Commercial logic

async def coins_store_ikb(user_id: int, is_owner: bool, price: int, offer_id: int):
    pass  # TODO: Commercial logic

async def when_users_blacklist_ikb(chat_id):
    pass  # TODO: Commercial logic

async def when_groups_blacklist_ikb(chat_id):
    pass  # TODO: Commercial logic

async def when_banlist_ikb(chat_id):
    pass  # TODO: Commercial logic

async def stats_ikb(chat_id):
    pass  # TODO: Commercial logic

# =========================
# RP CREATE WIZARD ( +рп )
# =========================

async def rp_create_choose_type_ikb() -> InlineKeyboardMarkup:
    """Шаг 0: выбор типа (обычная / 18+)."""
    pass  # TODO: Commercial logic


async def rp_wizard_gif_step_ikb(catalog_url: str) -> InlineKeyboardMarkup:
    """Шаг 3/3: GIF — строго только каталог (ID) или без GIF."""
    pass  # TODO: Commercial logic

# =========================
# RP PANELS (local + global)
# =========================

async def rp_panel_ikb(chat_id: int) -> InlineKeyboardMarkup:
    pass  # TODO: Commercial logic


async def rp_empty_my_ikb(chat_id: int) -> InlineKeyboardMarkup:
    pass  # TODO: Commercial logic


async def rp_my_list_ikb(rows_chunk, page: int, pages: int, is_adult: bool = False) -> InlineKeyboardMarkup:
    pass  # TODO: Commercial logic


async def rp_info_ikb(cmd: str, page: int, is_adult: bool = False) -> InlineKeyboardMarkup:
    pass  # TODO: Commercial logic


async def rp_edit_cancel_ikb(cmd: str, page: int, show_catalog: bool = False, is_adult: bool = False) -> InlineKeyboardMarkup:
    pass  # TODO: Commercial logic


async def global_rp_panel_ikb(user_id: int, is_adult: bool = False) -> InlineKeyboardMarkup:
    # 18+ убрано из глобальных РП. Раздел должен быть локальным (в "Мои РП").
    pass  # TODO: Commercial logic


back_to_cosmos_ikb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="⬅️ Назад", callback_data=f"cosmos")]
    ]
)


back_to_cosmos_ikb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="⬅️ Назад", callback_data=f"cosmos")]
    ]
)

async def chat_management_ikb(chat_id: int) -> InlineKeyboardMarkup:
    pass  # TODO: Commercial logic


async def back_to_chat_management_ikb(chat_id: int) -> InlineKeyboardMarkup:
    pass  # TODO: Commercial logic

migration_ikb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✅ Подтвердить", callback_data=f"agree_miration"),
            InlineKeyboardButton(text="❌ Отменить", callback_data=f"cancel_miration")
        ]
    ]
)


def chat_lang_menu_ikb(current_lang: str) -> InlineKeyboardMarkup:
    pass  # TODO: Commercial logic

# Настройки
async def settings_ikb(group_id, chat_id):
    pass  # TODO: Commercial logic

async def events_ikb(chat_id):
    # Меню настроек событий: каждая строка локализована
    # 🎛 Что записывать в канал?
    # 🔄 Изменить канал событий
    # ❌ Удалить канал событий
    # Назад / Корзина
    pass  # TODO: Commercial logic


async def shalosti_ikb(group_id: int, chat_id: int) -> InlineKeyboardMarkup:
    pass  # TODO: Commercial logic

async def events_settings_ikb(group_id, chat_id):
    pass  # TODO: Commercial logic


back_to_events_ikb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="⬅️ Назад", callback_data="events")]
    ]
)


async def night_mode_ikb(group_id, chat_id):
    pass  # TODO: Commercial logic

async def change_time_ikb(chat_id: int, start_hour: int = 22, end_hour: int = 6):
    pass  # TODO: Commercial logic

async def get_timezones_ikb() -> InlineKeyboardMarkup:

    pass  # TODO: Commercial logic


kick_ikb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="💤 Кик неактив", callback_data="kick_inactive")],
        [InlineKeyboardButton(text="🚀 Кик актив", callback_data="kick_active")],
        [InlineKeyboardButton(text="👶 Кик новичков", callback_data="kick_nubs")],
        [InlineKeyboardButton(text="🤐 Кик молчунов", callback_data="kick_silence")],
        [InlineKeyboardButton(text="⬅️ Назад", callback_data="chat_management_menu")]
    ]
)

kick_inactive_ikb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="📆 По периоду", callback_data="kick__by_period")],
        [InlineKeyboardButton(text="⬅️ Назад", callback_data="kick_menu")]
    ]
)

kick_inactive_ikb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🔢 По числу пользователей", callback_data="kick_inactive_by_count")],
        [InlineKeyboardButton(text="📆 По периоду", callback_data="kick_inactive_by_period")],
        [InlineKeyboardButton(text="🧮 По периоду и числу", callback_data="kick_inactive_mix")],
        [InlineKeyboardButton(text="⬅️ Назад", callback_data="kick_menu")]
    ]
)

back_to_kick_inactive_ikb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="⬅️ Назад", callback_data="kick_inactive")]
    ]
)

async def kick_inactive_by_count_confirmation_ikb(count):
    pass  # TODO: Commercial logic

async def kick_inactive_by_period_ikb():
    pass  # TODO: Commercial logic



kick_active_ikb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🔢 По числу пользователей", callback_data="kick_active_by_count")],
        [InlineKeyboardButton(text="📆 По периоду", callback_data="kick_active_by_period")],
        [InlineKeyboardButton(text="🧮 По периоду и числу", callback_data="kick_active_mix")],
        [InlineKeyboardButton(text="⬅️ Назад", callback_data="kick_menu")]
    ]
)

back_to_kick_active_ikb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="⬅️ Назад", callback_data="kick_active")]
    ]
)

async def kick_active_by_count_confirmation_ikb(count):
    pass  # TODO: Commercial logic

async def kick_active_by_period_ikb():
    pass  # TODO: Commercial logic



async def kick_nubs_by_period_ikb():
    pass  # TODO: Commercial logic

async def kick_silence_by_period_ikb():
    pass  # TODO: Commercial logic

# currency actions
async def choose_currency_exchange_ikb(user_id):
    pass  # TODO: Commercial logic

async def choose_currency_transfer_ikb(user_id):
    pass  # TODO: Commercial logic

async def confirm_currency_action_ikb(user_id):
    pass  # TODO: Commercial logic

# duels
async def duel_ikb(user_id, is_admin: bool = False):
    pass  # TODO: Commercial logic

async def confirm_duel_ikb(user_id):
    pass  # TODO: Commercial logic

async def started_duel_ikb(user_id):
    pass  # TODO: Commercial logic

async def delete_ikb(chat_id):
    pass  # TODO: Commercial logic

async def delete_ikb_like_back(chat_id):
    pass  # TODO: Commercial logic

async def cancel_ikb(chat_id):
    pass  # TODO: Commercial logic

async def spamlist_delete_ikb(chat_id):
    pass  # TODO: Commercial logic

async def clear_spamlist_100_per_ikb(chat_id):
    pass  # TODO: Commercial logic

cancel_generation_ikb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="⛔ Отменить", callback_data="cancel_generation")]
    ]
)


async def daily_rewards_keyboard(user_id: int, page=0, is_owner=False):
    pass  # TODO: Commercial logic



business_ikb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🧠 AI", callback_data="business_AI")],
        [InlineKeyboardButton(text="💾 База", callback_data="business_base")],
        [InlineKeyboardButton(text="📢 РП команды", callback_data="business_rp_cmds")],
        [InlineKeyboardButton(text="🔔 Напоминания", callback_data="business_reminders")],
        [InlineKeyboardButton(text="📊 Статистика", callback_data="business_statistic")],
        [InlineKeyboardButton(text="📩 Рассылка", callback_data="business_broadcast")],
    #    [InlineKeyboardButton(text="🗂️ История чата", callback_data="chat_history")],
        [InlineKeyboardButton(text="Мой VIP 💎", callback_data="vip")],
    ]
)


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

def get_history_pagination_kb(page: int, total_count: int, limit: int):
    pass  # TODO: Commercial logic

async def choose_vip_style_ikb():
    pass  # TODO: Commercial logic

async def transactions_delete_ikb(user_id: int, page: int = 1, total_pages: int = 1):
    pass  # TODO: Commercial logic

async def tops_panel_ikb(chat_id: int, owner_id: int) -> InlineKeyboardMarkup:
    """Единая панель топов. Открывается командой 'Топ'."""
    pass  # TODO: Commercial logic
