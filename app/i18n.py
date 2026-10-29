import json
import os
from functools import lru_cache

DEFAULT_LANG = "ru"
LOCALES_DIR = os.path.join(os.getcwd(), "locales")

translations = {}


def normalize_text(text: str) -> str:
    pass  # TODO: Commercial logic


def _load_locales():
    pass  # TODO: Commercial logic


def set_locales_path(path: str):
    pass  # TODO: Commercial logic


class _SafeDict(dict):
    def __missing__(self, key):
        pass  # TODO: Commercial logic


def _get_by_dot(d: dict, key: str):
    pass  # TODO: Commercial logic


@lru_cache(maxsize=4096)
def _lookup(lang: str, key: str):
    pass  # TODO: Commercial logic


def _lookup_text_key(lang: str, text_key: str):
    pass  # TODO: Commercial logic


def t(key: str, lang: str = DEFAULT_LANG, **kwargs):
    pass  # TODO: Commercial logic


def t_nofallback(key: str, lang: str, **kwargs):
    pass  # TODO: Commercial logic


_load_locales()
