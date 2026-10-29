import time
import inspect
import asyncpg
from config import DB_USER, DB_PASSWORD, DB_NAME, DB_HOST, DB_PORT
from app.debug.context import trace_id_var, user_id_var, chat_id_var


class Database:
    def __init__(self):
        pass  # TODO: Commercial logic

    def set_debug_hub(self, hub):
        pass  # TODO: Commercial logic

    def _detect_source(self) -> str:
        """
        Пытаемся определить, из какой функции/модуля пришёл SQL,
        если source не передали руками.
        """
        pass  # TODO: Commercial logic

    async def connect(self):
        """Создает один пул для всего бота"""
        pass  # TODO: Commercial logic

    async def disconnect(self):
        pass  # TODO: Commercial logic

    async def _run(self, method_name, query, *args, source="unknown"):
        pass  # TODO: Commercial logic

    async def fetch(self, query, *args, source="unknown"):
        pass  # TODO: Commercial logic

    async def fetchrow(self, query, *args, source="unknown"):
        pass  # TODO: Commercial logic

    async def fetchval(self, query, *args, source="unknown"):
        pass  # TODO: Commercial logic

    async def execute(self, query, *args, source="unknown"):
        pass  # TODO: Commercial logic

    async def fetch_users(self):
        pass  # TODO: Commercial logic
        
    async def fetch_users_in_private(self):
        pass  # TODO: Commercial logic
        
    async def fetch_admins(self):
        pass  # TODO: Commercial logic
        
    async def fetch_weddings(self):
        pass  # TODO: Commercial logic
        
    async def fetch_stops(self):
        pass  # TODO: Commercial logic

    async def fetch_marriages(self):
        pass  # TODO: Commercial logic
        
    async def fetch_stats(self):
        pass  # TODO: Commercial logic
        
    async def fetch_forbidden_words(self):
        pass  # TODO: Commercial logic
        
    async def fetch_gifs_topics(self):
        pass  # TODO: Commercial logic
        
    async def fetch_catalog_gifs(self):
        pass  # TODO: Commercial logic
        
    async def fetch_owner(self):
        pass  # TODO: Commercial logic
        
    async def fetch_ad_group(self):
        pass  # TODO: Commercial logic
        
    async def fetch_log_group(self):
        pass  # TODO: Commercial logic
        
    async def fetch_channels_to_control(self):
        pass  # TODO: Commercial logic
        
    async def fetch_global_rp_cmds(self):
        pass  # TODO: Commercial logic
        
    async def fetch_adult_global_rp_cmds(self):
        pass  # TODO: Commercial logic

    async def fetch_rp_cmds(self):
        pass  # TODO: Commercial logic
        
    async def fetch_adult_rp_cmds(self):
        pass  # TODO: Commercial logic
        
    async def fetch_settings(self):
        pass  # TODO: Commercial logic

    async def fetch_banlist(self):
        pass  # TODO: Commercial logic
        
    async def fetch_spamlist(self):
        pass  # TODO: Commercial logic
        
    async def fetch_users_blacklist(self):
        pass  # TODO: Commercial logic
        
    async def fetch_groups_blacklist(self):
        pass  # TODO: Commercial logic
        
    async def fetch_night_mode(self):
        pass  # TODO: Commercial logic

    async def fetch_texts(self):
        pass  # TODO: Commercial logic

    async def fetch_kbs(self):
        pass  # TODO: Commercial logic

    async def fetch_user_name_history(self):
        pass  # TODO: Commercial logic

    async def fetch_user_seen_chats(self):
        pass  # TODO: Commercial logic

    async def fetch_profile_settings(self):
        pass  # TODO: Commercial logic


db = Database()
