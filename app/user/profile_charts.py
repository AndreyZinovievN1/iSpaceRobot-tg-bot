import json
import random
from io import BytesIO
from pathlib import Path

import matplotlib
matplotlib.use("Agg")

import matplotlib.image as mpimg
import matplotlib.patheffects as pe
import matplotlib.pyplot as plt

from ..crud_tables.table_users import get_user_by_chat_id
from ..db import db
from config import logger


BASE_DIR = Path(__file__).resolve().parent
THEMES_CONFIG_PATH = BASE_DIR / "skins" / "charts_config.json"


def load_chart_themes() -> dict:
    pass  # TODO: Commercial logic


THEMES = load_chart_themes()


async def get_user_chart_theme_key(user_id: int) -> str:
    pass  # TODO: Commercial logic


def build_activity_chart(chart_data: dict, theme: str = "space") -> bytes:
    pass  # TODO: Commercial logic
