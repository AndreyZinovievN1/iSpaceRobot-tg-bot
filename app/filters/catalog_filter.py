import os
from typing import Any, Union, Dict

from aiogram.filters import Filter
from aiogram.types import Message

# Chat IDs are injected through the environment in production.
PUBLIC_CATALOG_CHAT_ID = int(os.getenv("PUBLIC_CATALOG_CHAT_ID", "0") or 0)
PRIVATE_CATALOG_CHAT_ID = int(os.getenv("PRIVATE_CATALOG_CHAT_ID", "0") or 0)

OWNER_ID = int(os.getenv("OWNER_ID", "0") or 0)

class IsCatalogManager(Filter):
    async def __call__(self, message: Message, db: Any) -> Union[bool, Dict[str, Any]]:
        # Разрешаем только 2 каталога
        pass  # TODO: Commercial logic
