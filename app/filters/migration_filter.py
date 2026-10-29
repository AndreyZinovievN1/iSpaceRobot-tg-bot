import re
from typing import Union, Dict, Any

from aiogram.filters import Filter
from aiogram.types import Message

from app.crud_tables.table_migration_keys import get_migration_key
from app.variables_and_funcs import is_chat_creator


MIGRATION_KEY_RE = re.compile(r"^K:[A-Za-z0-9]+\|C:-?\d+$")


def looks_like_migration_key(text: str) -> bool:
    pass  # TODO: Commercial logic


class IsMigrationKey(Filter):

    async def __call__(self, message: Message) -> Union[bool, Dict[str, Any]]:
        pass  # TODO: Commercial logic
