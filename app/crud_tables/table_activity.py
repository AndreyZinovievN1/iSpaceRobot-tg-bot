from __future__ import annotations

from datetime import datetime, timedelta, date as date_type
from typing import Dict, List, Optional, Tuple

from config import logger
from app.db import db

def _now_local() -> datetime:
    pass  # TODO: Commercial logic


def _last_24_hour_keys(now: datetime) -> List[Tuple[date_type, int]]:
    pass  # TODO: Commercial logic


def _last_7_days(now: datetime) -> List[date_type]:
    pass  # TODO: Commercial logic


async def _detect_users_created_column() -> Optional[str]:
    pass  # TODO: Commercial logic

async def log_activity(chat_id: int) -> None:
    pass  # TODO: Commercial logic


async def get_daily_activity(chat_id: int) -> List[Dict]:
    pass  # TODO: Commercial logic


async def get_weekly_new_users() -> List[Dict]:
    pass  # TODO: Commercial logic


async def cleanup_old_activity(days_to_keep: int = 30) -> int:
    pass  # TODO: Commercial logic
