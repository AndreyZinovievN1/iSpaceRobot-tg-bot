"""Configuration contract for iSpaceRobot.

Every value is injected through the environment (see ``.env.example``).
No tokens, API keys or database credentials live in the repository.
Runtime singletons (Telegram bot, scheduler) are created by the entry point.
"""
from __future__ import annotations

import logging
import os
from typing import Any

from aiogram.types import BotCommand
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)

# --- Telegram ---------------------------------------------------------------
TOKEN: str = os.getenv("TOKEN", "")
API_ID: int = int(os.getenv("API_ID", "0") or 0)
API_HASH: str = os.getenv("API_HASH", "")
OWNER_ID: int = int(os.getenv("OWNER_ID", "0") or 0)

# --- LLM providers: rotating pool of keys -----------------------------------
API_KEYS: list[str] = [
    key for key in (os.getenv(f"API_KEY_{index}") for index in (1, 2, 3)) if key
]

# --- PostgreSQL -------------------------------------------------------------
DB_USER: str = os.getenv("DB_USER", "")
DB_PASSWORD: str = os.getenv("DB_PASSWORD", "")
DB_NAME: str = os.getenv("DB_NAME", "")
DB_HOST: str = os.getenv("DB_HOST", "localhost")
DB_PORT: int = int(os.getenv("DB_PORT", "5432") or 5432)

DATABASE_URL: str = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    if DB_USER and DB_NAME
    else ""
)

# --- Redis: FSM cache, rate limits, hot counters ----------------------------
REDIS_HOST: str = os.getenv("REDIS_HOST", "127.0.0.1")
REDIS_PORT: int = int(os.getenv("REDIS_PORT", "6379") or 6379)
REDIS_DB: int = int(os.getenv("REDIS_DB", "0") or 0)
REDIS_PASSWORD: str | None = os.getenv("REDIS_PASSWORD") or None

# --- Runtime singletons (wired up in main.py) -------------------------------
bot: Any = None
scheduler: Any = None

# --- UI contract: the command menu Telegram shows to users ------------------
my_commands: list[BotCommand] = [
    BotCommand(command="help", description="All commands"),
    BotCommand(command="inv", description="Open inventory"),
    BotCommand(command="donate", description="Support the project"),
    BotCommand(command="id", description="Show chat ID"),
    BotCommand(command="business", description="Business tools"),
    BotCommand(command="report", description="Report a message"),
]
