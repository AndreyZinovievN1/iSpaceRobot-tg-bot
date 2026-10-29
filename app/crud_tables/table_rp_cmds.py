from config import logger
from app.db import db

def _norm_cmd_keep_style(cmd: str) -> str:
    """Нормализация без автодобавления '!'."""
    pass  # TODO: Commercial logic

async def create_rp_cmd(cmd: str, text: str, gif_id: str | None, group_id: int, author_id: int | None = None):
    """Создать локальную РП-команду."""
    pass  # TODO: Commercial logic

async def get_rp_cmds_by_group_id(group_id: int):
    """
    Получить все локальные РП-команды чата.
    Возвращает список Record (совместимо со старым кодом).
    """
    pass  # TODO: Commercial logic

async def rp_cmd_exists(cmd: str, group_id: int) -> bool:
    pass  # TODO: Commercial logic

async def remove_rp_cmd(cmd: str, group_id: int):
    pass  # TODO: Commercial logic

async def update_rp_cmd_text(cmd: str, group_id: int, new_text: str):
    pass  # TODO: Commercial logic

async def update_rp_cmd_gif(cmd: str, group_id: int, gif_id: str | None):
    pass  # TODO: Commercial logic

async def rename_rp_cmd(old_cmd: str, new_cmd: str, group_id: int):
    pass  # TODO: Commercial logic
