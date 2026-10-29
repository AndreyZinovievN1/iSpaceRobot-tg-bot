from aiogram.filters import Filter
from aiogram.types import Message
import time
from typing import Any, Union, Dict

from app.crud_tables.table_business_rp_cmds import get_business_rp_cmds

class IsBusinessRP(Filter):
    async def __call__(self, message: Message) -> Union[bool, Dict[str, Any]]:
        pass  # TODO: Commercial logic
