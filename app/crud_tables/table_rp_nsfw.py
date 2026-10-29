from config import logger
from app.db import db # Подключаем твой пул

TABLE = "public.rp_cmds_nsfw"

def _norm_cmd(cmd: str) -> str:
    """Нормализация текста команды."""
    pass  # TODO: Commercial logic

async def create_adult_rp_cmd(cmd: str, text: str, gif_id: str | None, group_id: int, author_id: int | None = None):
    """Добавить 18+ РП-команду с поддержкой новых колонок."""
    pass  # TODO: Commercial logic

async def get_adult_rp_cmds_by_group_id(group_id: int):
    """Вернуть список всех 18+ команд чата."""
    pass  # TODO: Commercial logic

async def adult_rp_cmd_exists(cmd: str, group_id: int) -> bool:
    pass  # TODO: Commercial logic

async def remove_adult_rp_cmd(cmd: str, group_id: int):
    pass  # TODO: Commercial logic

async def get_adult_rp_cmd_by_group_and_cmd(group_id: int, cmd: str):
    """Получить данные одной конкретной команды."""
    pass  # TODO: Commercial logic

async def update_adult_rp_cmd_text(cmd: str, group_id: int, new_text: str):
    pass  # TODO: Commercial logic

async def update_adult_rp_cmd_gif(cmd: str, group_id: int, gif_id: str | None):
    pass  # TODO: Commercial logic

async def rename_adult_rp_cmd(old_cmd: str, new_cmd: str, group_id: int):
    pass  # TODO: Commercial logic

async def get_all_adult_rp_cmds():
    pass  # TODO: Commercial logic
