from time import monotonic

from .i18n import t
from .crud_tables.table_settings import get_settings_by_group_id

LANG_ALLOWED = {"ru", "ua", "en"}


def _norm(code: str | None) -> str | None:
    pass  # TODO: Commercial logic


def _pick(obj, key):
    pass  # TODO: Commercial logic


_SETTINGS_CACHE = {}
_SETTINGS_TTL = 300

_TR_TTL = 60.0
_TR_MAX = 50_000
_TR_CACHE: dict[tuple[str, str], tuple[str, float]] = {}

_EXCLUDE_PREFIXES = (
    "roulette.win.", "roulette.bet.",
    "roulette.log.", "roulette.cooldown.",
    "roulette.cancelled", "roulette.spin."
)


def _evict_if_needed(cache: dict, maxsize: int) -> None:
    pass  # TODO: Commercial logic


async def chat_lang(chat_id: int) -> str:
    pass  # TODO: Commercial logic


def _safe_translate(key: str, lang: str, **kwargs):
    pass  # TODO: Commercial logic


async def tr_chat(chat_id: int, key: str, **kwargs) -> str:
    pass  # TODO: Commercial logic


async def tr_msg(message, key: str, **kwargs) -> str:
    pass  # TODO: Commercial logic


async def get_tr(message):
    pass  # TODO: Commercial logic
