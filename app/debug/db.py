import time
import asyncpg
from .context import trace_id_var, user_id_var, chat_id_var


class MonitoredDB:
    def __init__(self, dsn: str, hub, min_size: int = 3, max_size: int = 15):
        pass  # TODO: Commercial logic

    async def connect(self):
        pass  # TODO: Commercial logic

    async def close(self):
        pass  # TODO: Commercial logic

    async def fetch(self, query: str, *args, source: str = "unknown"):
        pass  # TODO: Commercial logic

    async def fetchrow(self, query: str, *args, source: str = "unknown"):
        pass  # TODO: Commercial logic

    async def fetchval(self, query: str, *args, source: str = "unknown"):
        pass  # TODO: Commercial logic

    async def execute(self, query: str, *args, source: str = "unknown"):
        pass  # TODO: Commercial logic

    async def _run(self, method: str, query: str, *args, source: str):
        pass  # TODO: Commercial logic
