from config import logger
from app.db import db


ALLOWED_WEDDING_ROLES = {
    "husband",
    "wife",
    "registrar",
    "witness_man",
    "witness_woman",
}


async def get_wedding(group_id: int):
    pass  # TODO: Commercial logic


async def create_wedding(husband_id: int, group_id: int):
    pass  # TODO: Commercial logic


async def update_wedding_member(who: str, group_id: int, member_id: int):
    pass  # TODO: Commercial logic


async def update_guests(group_id: int, guest_id: int):
    pass  # TODO: Commercial logic


async def update_wedding_sign(who: str, group_id: int):
    pass  # TODO: Commercial logic


async def delete_wedding(group_id: int):
    pass  # TODO: Commercial logic
