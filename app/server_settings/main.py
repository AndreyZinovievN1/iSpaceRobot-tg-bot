from aiogram import Dispatcher
from aiogram.methods import DeleteWebhook
import asyncio

from app.variables_and_funcs import my_commands, log_daily_queries, log_daily_clear, check_channel_subs
from app.db import db
from config import bot, scheduler

# ROUTERS
from app.AI import AI_router

from app.owner.owner_cmds import owner_cmds_router
from app.owner.manage_agents import manage_agents_router
from app.owner.manage_grp_cmds import manage_grp_cmds_router
from app.owner.broadcast import broadcast_router
from app.owner.global_welcome_text import global_welcome_text_router
from app.owner.antispam import antispam_router
from app.owner.banlist import banlist_router

from app.agent_of_stars.blacklists import blacklists_router
from app.agent_of_stars.agents_cmds import agents_cmds_router

from app.chat_owner.night_mode import night_mode_router
from app.chat_owner.manage_events import manage_events_router
from app.chat_owner.migration import migration_router
from app.chat_owner.kick.active_kick import active_kick_router
from app.chat_owner.kick.inactive_kick import inactive_kick_router
from app.chat_owner.kick.kick_by_none import nubs_kick_router
from app.chat_owner.kick.kick import kick_cmds_router
from app.chat_owner.chat_management import chat_management_router
from app.chat_owner.welcome_text import welcome_text_router

from app.admin.moderation import moderation_router
from app.admin.manage_rp_cmds import manage_rp_cmds_router
from app.admin.manage_settings import manage_settings_router

from app.event_handlers import events_router
from app.roulette import roulette_router
from app.tops import tops_router
from app.nav import nav_router
from app.weddings_divorces import weddings_divorces_router
from app.update_user_data import update_user_data_router

from app.user.base_cmds import base_router
from app.user.duels import duels_router
from app.user.currency_actions import currency_actions_router

from app.filters.private_filter import private_filter_router
from app.filters.group_filter import group_filter_router
from app.filters.channel_post import channel_post_router


async def on_startup(dp):
    pass  # TODO: Commercial logic

async def main():
    pass  # TODO: Commercial logic

if __name__ == "__main__":
    asyncio.run(main())
