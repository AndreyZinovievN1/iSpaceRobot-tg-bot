import asyncio
import sys
import logging
import os

import pysqlite3

sys.modules["sqlite3"] = pysqlite3

import aiogram
from aiogram import Dispatcher
from aiogram.methods import DeleteWebhook
from aiogram.fsm.storage.memory import MemoryStorage
from pyrogram import Client

from app.chat_owner.night_mode import sync_all_night_modes
from app.logs.daily_logs import log_daily_queries
from app.user_bot.cleaner_logic import run_daily_clean
from app.user_bot.gifts_api import start_gifts_api, stop_gifts_api
from app.user_bot.userbot_manager import stop_all_userbots
from app.db import db
from config import bot, scheduler, API_ID, API_HASH, my_commands
from redis_client import redis

from app.debug import setup_debug, stop_debug

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

# user_app = Client("my_service_account", api_id=API_ID, api_hash=API_HASH)

from app import i18n

i18n.set_locales_path(os.path.join(os.path.dirname(__file__), "app", "locales"))

print(f"DEBUG: Версия aiogram = {aiogram.__version__}")

# --- ИМПОРТЫ РОУТЕРОВ ---

from app.middlewares.stats_middleware import StatsMiddleware
from app.middlewares.updates_middleware import UpdateUserMiddleware
from app.middlewares.night_mode_middleware import NightModeMiddleware
from app.middlewares.activity_middleware import ActivityMiddleware

from app.chat_owner.migration import router as migration_router
from app.owner.catalog.catalog import router as catalog_router
from app.AI import AI_router, stop_ai_tasks

from app.owner.owner_cmds import router as owner_cmds_router, stop_clean_tasks
from app.owner.economy import router as economy_router
from app.owner.system.service import router as service_router
from app.owner.system.main_mgmt import router as main_mgmt_router
from app.owner.protection.blacklist import router as blacklist_router
from app.owner.admin_tools.manage_agents import router as manage_agents_router
from app.owner.admin_tools.manage_grp_cmds import router as manage_grp_cmds_router
from app.owner.system.broadcast import router as broadcast_router
from app.owner.system.global_welcome_text import router as global_welcome_text_router
from app.owner.protection.antispam import router as antispam_router
from app.owner.protection.banlist import router as banlist_router
from app.owner.admin_tools.subs import router as subs_router
from app.owner.custom_emoji_handler import router as custom_emoji_router
from app.owner.emoji_saver import router as emoji_saver_router
from app.owner.categories_manager import router as manage_categories_router
from app.owner.panel import router as owner_panel_router
from app.owner.nsfw_alerts import router as nsfw_alerts_router

from app.agent_of_stars.blacklists import router as blacklists_router
from app.agent_of_stars.scammers import router as scam_router
from app.agent_of_stars.reports import router as reports_router
from app.agent_of_stars.agents_cmds import router as agents_cmds_router
from app.agent_of_stars.panel import router as agent_panel_router

from app.chat_owner.night_mode import router as night_mode_router
from app.chat_owner.manage_events import router as manage_events_router
from app.chat_owner.kick.active_kick import router as active_kick_router
from app.chat_owner.kick.inactive_kick import router as inactive_kick_router
from app.chat_owner.kick.kick_by_none import router as nubs_kick_router
from app.chat_owner.kick.kick import router as kick_cmds_router
from app.chat_owner.chat_management import router as chat_management_router
from app.chat_owner.welcome_text import router as welcome_text_router

from app.admin.moderation import router as moderation_router
from app.admin.manage_rp_cmds import router as manage_rp_cmds_router
from app.admin.group_settings.manage_settings import router as manage_settings_router
from app.admin.group_settings.antiforward import router as antiforward_router

from app.event_handlers import router as events_router
from app.user.tops.tops import router as tops_router
from app.user.tops.nav import router as nav_router
from app.user.rp_commands import router as rp_commands_router
from app.weddings_divorces import router as weddings_divorces_router

from app.user.business.reminders import router as reminders_router
from app.user.business.statistics import router as statistics_router
from app.user.business.biz_broadcast import router as business_broadcast_router
from app.user.business.chat_history import router as chat_history_router
from app.user.business.biz_rp_cmds import router as biz_rp_cmds_router
from app.user.business.form import router as form_router
from app.user.business.business import router as business_router
from app.user.business.business_events import router as business_events_router
from app.user.business.biz_AI import router as biz_AI_router

from app.user.base_cmds import router as base_router
from app.user.duels import router as duels_router
from app.user.profile import router as profile_router
from app.user.stats import router as stats_router
from app.user.rp_cmds import router as rp_cmds_router
from app.help_system.help_handlers import router as help_router
from app.user.inventory import router as inventory_router

from app.user.donate.currency_actions import router as currency_actions_router
from app.user.donate.coin_offers import router as coin_offers_router
from app.user.donate.starcoin_offers import router as starcoin_offers_router
from app.user.donate.reward import router as reward_router
from app.user.donate.donate import router as donate_router
from app.user.donate.vip import router as vip_router
from app.user.donate.categories import router as category_router, stop_chart_warmup_tasks

from app.roulette.roulette import router as roulette_router
from app.roulette.handler import router as roulette_handler_router
from app.roulette.functions import begin_roulette_shutdown, stop_roulette_tasks

from app.channel_mgmt import router as channel_mgmt_router, check_channel_subs
from app.private_msgs import router as private_filter_router
from app.group_msgs import router as group_filter_router, stop_background_delete_tasks
from app.shutdown import cancel_tasks, cancel_update_tasks, scheduler_tasks

# SPACE AI v2
from app.ai_chat.activity_service import space_idle_tick
from app.ai_chat.maintenance_service import run_ai_chat_maintenance
from app.ai_chat.nsfw_config import nsfw_scan_enabled
from app.ai_chat.nsfw_worker import run_once as run_nsfw_scan_once


print("✅ Роутеры успешно импортированы")


def _env_int(name: str, default: int, *, min_value: int = 1) -> int:
    pass  # TODO: Commercial logic


async def _run_nsfw_scan_job() -> None:
    pass  # TODO: Commercial logic


def _env_bool(name: str, default: bool) -> bool:
    pass  # TODO: Commercial logic


async def _run_daily_clean_job() -> None:
    """Плановая уборка мёртвых чатов и удалённых аккаунтов (отчёт — в лог-чат)."""
    pass  # TODO: Commercial logic


async def on_startup():
    pass  # TODO: Commercial logic


async def main():
    pass  # TODO: Commercial logic


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("👋 Бот остановлен")
