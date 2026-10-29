from aiogram.filters import Filter
from aiogram.types import Message
from typing import Union, Dict, Any
import time
from datetime import datetime
from pytz import timezone

from app.crud_tables.table_rp_cmds import get_rp_cmds_by_group_id
from app.crud_tables.table_rp_nsfw import get_adult_rp_cmd_by_group_and_cmd

# личные RP (из бизнес-таблицы)
from app.crud_tables.table_business_rp_cmds import get_business_rp_cmds

# VIP хранится в vip_users
from app.crud_tables.table_vip_users import get_vip_user


MSK_TZ = timezone("Europe/Moscow")

# Кэш храним прямо в модуле
# Ключ: chat_id, Значение: (время_обновления, список_команд)
_global_cache = {"data": None, "time": 0}
_local_cache = {}


class IsRPCommand(Filter):
    async def __call__(self, message: Message, db: Any) -> Union[bool, Dict[str, Any]]:
        pass  # TODO: Commercial logic
