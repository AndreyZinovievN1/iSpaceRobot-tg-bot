"""Доступ к «подаркам за звёзды» (Star Gifts) через юзербот.

Модуль — тонкий слой поверх вендорного TL-описания из
:mod:`app.user_bot.gifts_tl`:

* :func:`fetch_gift_catalog` — каталог подарков (``payments.getStarGifts``);
* :func:`fetch_saved_gifts` — подарки, полученные аккаунтом юзербота
  (``payments.getSavedStarGifts``, с постраничным добором), включая уникальные
  (``starGiftUnique``);
* :func:`download_gift_sticker` — Lottie-анимация подарка (``.tgs``) в кэш;
* :func:`download_unique_gift_sticker` — та же анимация, но модели уникального
  подарка (она лежит в атрибуте ``starGiftAttributeModel``, а не в ``sticker``);
* :func:`transfer_saved_gift` — передача подарка с аккаунта другому
  пользователю (``payments.transferStarGift``);
* :func:`gift_to_dict` / :func:`unique_gift_to_dict` /
  :func:`saved_gift_to_dict` — примитивный JSON для REST.

Импорт модуля ничего не запускает: юзербот поднимается лениво через
:func:`resolve_userbot_client` (роль ``gifts`` в
:mod:`app.user_bot.userbot_manager`). Благодаря этому файл проверяется офлайн,
без ``config`` и без сети — см. ``runtime_tmp/selftest_gifts_logic.py``.
"""

from __future__ import annotations

import asyncio
import gzip
import inspect
import json
import logging
import os
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Set

from pyrogram import raw
from pyrogram.errors import FloodWait, RPCError
from pyrogram.types import Document as PyrogramDocument

from app.user_bot import gifts_tl  # noqa: F401  (регистрирует конструкторы подарков)
from app.shutdown import cancel_tasks

logger = logging.getLogger(__name__)

__all__ = [
    "GiftsError",
    "GiftsUnavailable",
    "GiftsFormatError",
    "DEFAULT_CACHE_DIR",
    "resolve_userbot_client",
    "userbot_last_error",
    "stop_restore_tasks",
    "call_budget",
    "fetch_gift_catalog",
    "fetch_saved_gifts",
    "register_gifts",
    "find_gift",
    "known_gift_ids",
    "gift_to_dict",
    "unique_gift_to_dict",
    "unique_gift_model_document",
    "unique_gift_pattern_document",
    "saved_gift_to_dict",
    "peer_to_dict",
    "cache_dir",
    "gift_sticker_path",
    "gift_sticker_json_path",
    "download_gift_sticker",
    "extract_lottie_json",
    "ensure_gift_sticker",
    "unique_gift_sticker_path",
    "unique_gift_sticker_json_path",
    "download_unique_gift_sticker",
    "ensure_unique_gift_sticker",
    "unique_gift_pattern_path",
    "find_unique_gift_pattern_path",
    "download_unique_gift_pattern",
    "ensure_unique_gift_pattern",
    "pattern_extension",
    "pattern_content_type",
    "saved_gift_present",
    "transfer_saved_gift",
]

_LOG = "[GIFTS]"

# Корень проекта: .../Space 5.1/app/user_bot/gifts_logic.py -> parents[2]
PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_CACHE_DIR = PROJECT_ROOT / "gift_cache"

_RETRY_LIMIT = 3


# --------------------------------------------------------------------------- #
#                     ЧТЕНИЕ НАСТРОЕК ИЗ ОКРУЖЕНИЯ                            #
# --------------------------------------------------------------------------- #
def _env_str(name: str, default: Optional[str] = None) -> Optional[str]:
    pass  # TODO: Commercial logic


def _env_bool(name: str, default: bool) -> bool:
    pass  # TODO: Commercial logic


def _env_int(
    name: str,
    default: int,
    *,
    minimum: int = 0,
    maximum: Optional[int] = None,
) -> int:
    pass  # TODO: Commercial logic


def _env_float(name: str, default: float, *, minimum: float = 0.0) -> float:
    pass  # TODO: Commercial logic


def cache_dir() -> Path:
    """Каталог кэша Lottie-анимаций (``GIFTS_CACHE_DIR``)."""
    pass  # TODO: Commercial logic


def _call_timeout() -> float:
    pass  # TODO: Commercial logic


def _call_deadline() -> float:
    """Бюджет всего запроса к Telegram (``GIFTS_CALL_DEADLINE``).

    Бюджет считается на вызов целиком — вместе с повторами и возвратом сессии
    на родной слой, — а не на отдельную попытку. Так REST-слой успевает ответить
    раньше, чем клиент (сервер Mini App) оборвёт соединение: вместо тишины и
    «таймаута» приходит реальная причина сбоя.
    """
    pass  # TODO: Commercial logic


def _restore_timeout() -> float:
    """Сколько ждём возврат сессии на родной слой (``GIFTS_RESTORE_TIMEOUT``)."""
    pass  # TODO: Commercial logic


def call_budget() -> Dict[str, float]:
    """Текущий бюджет запроса: дедлайн вызова, таймаут попытки, возврат слоя."""
    pass  # TODO: Commercial logic


def _download_timeout() -> float:
    pass  # TODO: Commercial logic


def _use_layer() -> bool:
    """Заворачивать ли запросы в ``invokeWithLayer`` (``GIFTS_USE_LAYER``)."""
    pass  # TODO: Commercial logic


# --------------------------------------------------------------------------- #
#                                 ОШИБКИ                                      #
# --------------------------------------------------------------------------- #
class GiftsError(RuntimeError):
    """Базовая ошибка слоя подарков (её текст безопасно отдавать в REST)."""


class GiftsUnavailable(GiftsError):
    """Юзербот не поднят — подарки получить не у кого."""


class GiftsFormatError(GiftsError):
    """Полезная нагрузка пришла в неожиданном формате (например, не Lottie)."""


# --------------------------------------------------------------------------- #
#                              ЮЗЕРБОТ (PYROGRAM)                             #
# --------------------------------------------------------------------------- #
async def resolve_userbot_client() -> Optional[Any]:
    """Возвращает подключённый юзербот подарков, при необходимости поднимая его.

    Импорт менеджера юзерботов сделан внутри функции: модуль подарков должен
    импортироваться без ``config``/``aiogram`` (нужно для офлайн-тестов).
    Подарки работают со своей ролью ``gifts`` — отдельным аккаунтом Telegram,
    поэтому запросы Mini App не пересекаются с уборкой.
    """
    pass  # TODO: Commercial logic


def userbot_last_error() -> Optional[str]:
    """Последняя ошибка запуска юзербота подарков (для ``/health``), либо None."""
    pass  # TODO: Commercial logic


async def _resolve_api_id(client: Any) -> Optional[int]:
    """``api_id`` юзербота: из клиента или из его хранилища сессии.

    Своё ``initConnection`` Pyrogram отправляет именно с
    ``await client.storage.api_id()``, поэтому в хранилище заглядываем как в
    запасной вариант (юзербот из ``cleaner_logic`` обычно уже знает ``api_id``).
    """
    pass  # TODO: Commercial logic


#: Ссылки на фоновые задачи возврата слоя: без них сборщик мусора убьёт задачу.
_restore_tasks: Set[Any] = set()

#: Один клиент подарков = один TL-слой сессии. Пока запрос объявлен под нашим
#: слоем (``gifts_tl.TL_LAYER``), второй параллельный запрос с другим слоем
#: ломает разбор ответа у обоих. Поэтому все переходы слоя идут по очереди.
_LAYER_LOCK: Optional[asyncio.Lock] = None


def _layer_lock() -> asyncio.Lock:
    """Лок переходов TL-слоя (создаётся на работающем event loop)."""
    pass  # TODO: Commercial logic


def _restore_task_done(task: asyncio.Task) -> None:
    """Убирает задачу из реестра и извлекает её исключение.

    Иначе ошибка фонового возврата слоя всплывает только при сборке мусора как
    ``Task exception was never retrieved`` («Ошибка asyncio» в логах).
    """
    pass  # TODO: Commercial logic


def _schedule_restore(client: Any) -> None:
    """Возвращает слой в фоне: бюджет вызова уже израсходован.

    Ответ клиенту ждать не должен, но сессию юзербота нельзя оставлять на нашем
    слое — остальная логика бота разбирает ответы типами слоя Pyrogram.
    """
    pass  # TODO: Commercial logic


async def stop_restore_tasks() -> None:
    """Гасит фоновые возвраты слоя перед остановкой бота.

    Иначе при выходе остаются незавершённые задачи, и asyncio печатает
    «Task was destroyed but it is pending!» — это и есть та самая
    «Ошибка asyncio» в логах при остановке.
    """
    pass  # TODO: Commercial logic


async def _restore_session_layer(client: Any, timeout: Optional[float] = None) -> None:
    """Возвращает сессию юзербота на родной слой Pyrogram.

    ``initConnection`` объявляет слой для всей сессии, а остальная логика
    юзербота разбирает ответы типами слоя Pyrogram (158). Поэтому сразу после
    запроса под нашим слоем (``gifts_tl.TL_LAYER``) возвращаем серверу прежний
    слой — так же, как это делает сам Pyrogram при старте сессии.
    Отключается переменной ``GIFTS_RESTORE_LAYER=false``.

    ``timeout`` — остаток бюджета вызова: возврат слоя не имеет права задержать
    ответ клиенту дольше, чем он готов ждать. Если бюджета уже нет, запрос
    уходит в фон (:func:`_schedule_restore`).
    """
    pass  # TODO: Commercial logic


async def _invoke(
    client: Any,
    query: Any,
    label: str,
    *,
    use_layer: Optional[bool] = None,
    timeout: Optional[float] = None,
) -> Any:
    """Отправляет TL-запрос юзерботом: FloodWait, повторы и жёсткий дедлайн.

    ``timeout`` — бюджет всего вызова (по умолчанию ``GIFTS_CALL_DEADLINE``),
    а не таймаут одной попытки. Когда бюджет кончился, наружу уходит
    :class:`GiftsError` с причиной: REST-слой отвечает всегда, поэтому клиент
    видит реальную ошибку Telegram, а не собственный таймаут.
    """
    pass  # TODO: Commercial logic


# --------------------------------------------------------------------------- #
#                      РЕЕСТР ПОДАРКОВ (id -> TL-объект)                       #
# --------------------------------------------------------------------------- #
#: Нужен, чтобы эндпоинт ``/api/gifts/sticker/{id}`` мог скачать анимацию,
#: зная только числовой id подарка.
_gift_registry: Dict[int, Any] = {}


def register_gifts(gifts: Optional[Sequence[Any]]) -> int:
    """Кладёт подарки в реестр ``id -> starGift``. Возвращает размер реестра."""
    pass  # TODO: Commercial logic


def find_gift(gift_id: int) -> Optional[Any]:
    """Подарок из реестра (None, если он ещё не встречался)."""
    pass  # TODO: Commercial logic


def known_gift_ids() -> List[int]:
    pass  # TODO: Commercial logic


# --------------------------------------------------------------------------- #
#                              ЗАПРОСЫ TELEGRAM                               #
# --------------------------------------------------------------------------- #
async def fetch_gift_catalog(
    client: Any,
    *,
    hash: int = 0,  # noqa: A002 - имя поля из TL
    use_layer: Optional[bool] = None,
    timeout: Optional[float] = None,
) -> Dict[str, Any]:
    """Каталог подарков: ``payments.getStarGifts``.

    ``hash=0`` заставляет Telegram вернуть полный список. Если каталог уже
    закэширован аккаунтом, придёт ``payments.starGiftsNotModified`` — это не
    ошибка, отдаём флаг ``not_modified=True``.
    """
    pass  # TODO: Commercial logic


async def fetch_saved_gifts(
    client: Any,
    *,
    peer: Optional[Any] = None,
    offset: str = "",
    limit: Optional[int] = None,
    max_pages: Optional[int] = None,
    sort_by_value: bool = False,
    collection_id: Optional[int] = None,
    exclude_unique: bool = False,
    exclude_hosted: bool = True,
    use_layer: Optional[bool] = None,
    timeout: Optional[float] = None,
) -> Dict[str, Any]:
    """Подарки аккаунта: ``payments.getSavedStarGifts``.

    ``peer`` по умолчанию — сам аккаунт юзербота (``InputPeerSelf``).
    Уникальные (``starGiftUnique``) подарки **включаются**: их типы вендорены в
    :mod:`app.user_bot.gifts_tl`, поэтому разбор ответа не ломается, а владельцу
    видно всё, что лежит на аккаунте. «Размещённые» (hosted) подарки — те, что
    Telegram показывает на профиле, а владеет ими кошелёк TON, — приходят только
    без флага ``exclude_hosted``: по умолчанию он выставлен, и такие подарки в
    список не попадают (Mini App спрашивает ``exclude_hosted=False`` — иначе
    владелец видит на аккаунте одни обычные подарки). ``host_id`` экземпляра
    уезжает в ответе (``hosted`` в :func:`unique_gift_to_dict`).
    """
    pass  # TODO: Commercial logic


# --------------------------------------------------------------------------- #
#                        СЕРИАЛИЗАЦИЯ В JSON (ДЛЯ REST)                        #
# --------------------------------------------------------------------------- #
def _as_int(value: Any) -> Optional[int]:
    pass  # TODO: Commercial logic


def _as_bool(value: Any) -> bool:
    pass  # TODO: Commercial logic


def _iso(timestamp: Optional[int]) -> Optional[str]:
    """Unix-время Telegram -> ISO-8601 в UTC."""
    pass  # TODO: Commercial logic


def peer_to_dict(peer: Any) -> Optional[Dict[str, Any]]:
    """``PeerUser``/``PeerChat``/``PeerChannel`` -> примитивный словарь."""
    pass  # TODO: Commercial logic


def _entity_to_dict(entity: Any) -> Optional[Dict[str, Any]]:
    """``User``/``Chat``/``Channel`` из ответа -> примитивный словарь."""
    pass  # TODO: Commercial logic


def _background_to_dict(background: Any) -> Optional[Dict[str, Any]]:
    pass  # TODO: Commercial logic


def _sticker_to_dict(
    document: Any,
    gift_id: Optional[int],
    *,
    unique: bool = False,
) -> Optional[Dict[str, Any]]:
    """Документ-анимация подарка (``.tgs``) -> словарь + ссылки на REST.

    ``unique=True`` меняет только адрес: у уникального подарка анимация модели
    лежит в своей ручке (``/api/gifts/sticker/unique/<id>``), потому что id
    экземпляра и id каталога — разные пространства имён.
    """
    pass  # TODO: Commercial logic


def gift_to_dict(gift: Any) -> Dict[str, Any]:
    """``starGift`` -> JSON для Mini App (все поля TL-схемы, кроме бинарных).

    Уникальные подарки (``starGiftUnique``) описываются отдельно — у них другое
    значение ``id`` и картинка лежит в атрибутах: см. :func:`unique_gift_to_dict`.
    """
    pass  # TODO: Commercial logic


def unique_gift_model_document(gift: Any) -> Optional[Any]:
    """Документ-анимация модели уникального подарка.

    У обычного подарка анимация лежит в ``starGift.sticker``, у уникального —
    в атрибуте ``starGiftAttributeModel``: ``attributes`` — это вектор из
    модели, узора, подложки и (иногда) данных о первом вручении.
    """
    pass  # TODO: Commercial logic


def _unique_gift_pattern_attribute(gift: Any) -> Optional[Any]:
    """Атрибут-узор уникального подарка (``starGiftAttributePattern``)."""
    pass  # TODO: Commercial logic


def unique_gift_pattern_document(gift: Any) -> Optional[Any]:
    """Документ-узор уникального подарка (атрибут ``starGiftAttributePattern``).

    Узор — «стикер, который накладывается на подложку коллекционного подарка
    повторяющимся рисунком» (описание ``starGiftAttributePattern``), а цвет ему даёт
    сама подложка (``pattern_color``). Приложению нужен сам документ: оно красит
    узор цветом подложки и укладывает плиткой — так же, как клиент Telegram.
    """
    pass  # TODO: Commercial logic


def _unique_backdrop(gift: Any) -> Optional[Dict[str, Any]]:
    """Цвета подложки уникального подарка (атрибут ``Backdrop``)."""
    pass  # TODO: Commercial logic


def _attribute_to_dict(attribute: Any) -> Dict[str, Any]:
    """Атрибут уникального подарка (модель/узор/подложка/детали) -> словарь."""
    pass  # TODO: Commercial logic


def unique_pattern_to_dict(gift: Any, unique_id: Optional[int]) -> Optional[Dict[str, Any]]:
    """Узор подложки уникального подарка -> словарь + адрес ручки.

    У узора своя ручка (``/api/gifts/sticker/unique/<id>.pattern``), как у анимации
    модели: id — это id ЭКЗЕМПЛЯРА, а не каталога. Тип содержимого едет как есть
    (``image/webp`` или ``application/x-tgsticker``): по нему приложение решает,
    можно ли наложить узор маской поверх подложки.
    """
    pass  # TODO: Commercial logic


def unique_gift_to_dict(gift: Any) -> Dict[str, Any]:
    """``starGiftUnique`` -> JSON для Mini App.

    Что важно приложению и чем это отличается от обычного подарка:

    * ``kind="unique"`` — это экземпляр, а не строка каталога;
    * ``id`` — id ЭКЗЕМПЛЯРА (по нему подарок передают), ``gift_id`` — id
      «родителя» в каталоге (по нему подарок когда-то купили);
    * ``num``/``slug``/``title`` — номер экземпляра (``#35 651``), имя и ссылка;
    * ``host_id``/``hosted`` — подарок выставлен на профиль аккаунта, а владеет им
      кошелёк TON: передать его с аккаунта нельзя, передаёт владелец кошелька;
    * ``sticker`` — анимация МОДЕЛИ из атрибутов, с адресом ручки
      ``/api/gifts/sticker/unique/<id>``;
    * ``backdrop`` — цвета подложки из атрибута (у обычных — ``background``);
    * ``stars=0``/``convert_stars=0`` — в каталоге Telegram такого экземпляра
      нет, продать его нельзя: он только «лежит на аккаунте».
    """
    pass  # TODO: Commercial logic


def saved_gift_to_dict(saved: Any) -> Dict[str, Any]:
    """``savedStarGift`` -> JSON для Mini App."""
    pass  # TODO: Commercial logic


# --------------------------------------------------------------------------- #
#                      LOTTIE-АНИМАЦИЯ ПОДАРКА (.tgs / .json)                  #
# --------------------------------------------------------------------------- #
#: Блокировки на скачивание, чтобы параллельные запросы Mini App не качали
#: один и тот же файл дважды.
_sticker_locks: Dict[int, asyncio.Lock] = {}


def _sticker_lock(gift_id: int) -> asyncio.Lock:
    pass  # TODO: Commercial logic


def gift_sticker_path(gift_id: int, *, cache_dir: Optional[Path] = None) -> Path:
    """Путь к локальной копии ``.tgs`` подарка (файл может не существовать)."""
    pass  # TODO: Commercial logic


def gift_sticker_json_path(gift_id: int, *, cache_dir: Optional[Path] = None) -> Path:
    """Путь к распакованному Lottie-JSON подарка."""
    pass  # TODO: Commercial logic


def unique_gift_sticker_path(unique_id: int, *, cache_dir: Optional[Path] = None) -> Path:
    """Путь к локальной копии анимации МОДЕЛИ уникального подарка (``.tgs``)."""
    pass  # TODO: Commercial logic


def unique_gift_sticker_json_path(
    unique_id: int,
    *,
    cache_dir: Optional[Path] = None,
) -> Path:
    """Путь к распакованному Lottie-JSON модели уникального подарка."""
    pass  # TODO: Commercial logic


#: Расширение файла узора подложки -> тип содержимого для REST.
_PATTERN_CONTENT_TYPES = {
    "webp": "image/webp",
    "png": "image/png",
    "jpg": "image/jpeg",
    "gif": "image/gif",
    "tgs": "application/x-tgsticker",
}

#: Расширения, с которыми узор кладётся в кэш (по ним же ищем готовый файл).
PATTERN_EXTENSIONS = ("webp", "png", "jpg", "gif", "tgs", "bin")


def pattern_extension(mime_type: Optional[str]) -> str:
    """Расширение файла узора по типу документа из Telegram.

    Узор — обычный документ-стикер, и тип у него бывает разным: картинка
    (``image/webp``) или Lottie (``application/x-tgsticker``). Расширение нужно и
    для имени файла в кэше, и для ответа REST: по нему приложение решает, можно ли
    красить узор маской.
    """
    pass  # TODO: Commercial logic


def pattern_content_type(ext: str) -> str:
    """Тип содержимого узора по расширению файла (незнакомое — ``octet-stream``)."""
    pass  # TODO: Commercial logic


def unique_gift_pattern_path(
    unique_id: int,
    *,
    ext: str = "webp",
    cache_dir: Optional[Path] = None,
) -> Path:
    """Путь к локальной копии узора подложки уникального подарка.

    Файл называется ``<id>.pattern.<ext>``: расширение берётся у документа, иначе
    узор не отличить от анимации модели (``<id>.unique.tgs``) и анимации
    «родителя» из каталога (``<id>.tgs``).
    """
    pass  # TODO: Commercial logic


def find_unique_gift_pattern_path(
    unique_id: int,
    *,
    cache_dir: Optional[Path] = None,
) -> Optional[Path]:
    """Готовый файл узора, если он уже лежит в кэше.

    Расширение знает только сам документ из Telegram, а ручке
    ``/api/gifts/sticker/unique/<id>.pattern`` приходит один id — поэтому
    перебираем известные расширения.
    """
    pass  # TODO: Commercial logic


def cache_dir_default() -> Path:
    """Обёртка над :func:`cache_dir` (позволяет подменить кэш в тестах)."""
    pass  # TODO: Commercial logic


def _is_cached(path: Path) -> bool:
    pass  # TODO: Commercial logic


async def _cache_document(
    client: Any,
    document: Any,
    target: Path,
    key: int,
    *,
    force: bool = False,
    timeout: Optional[float] = None,
    label: str = "анимация подарка",
) -> Optional[Path]:
    """Скачивает документ-анимацию в файл ``target`` (общий код для обоих видов).

    Telegram отдаёт анимацию как обычный документ-стикер: ``.tgs`` — это
    gzip-сжатый Lottie-JSON. Для скачивания документ пересобирается в
    пирограмовский ``types.Document`` (нужен ``file_id``).
    """
    pass  # TODO: Commercial logic


async def download_gift_sticker(
    client: Any,
    gift: Any,
    *,
    cache_dir: Optional[Path] = None,
    force: bool = False,
    timeout: Optional[float] = None,
) -> Optional[Path]:
    """Скачивает Lottie-анимацию подарка в кэш и возвращает путь к ``.tgs``."""
    pass  # TODO: Commercial logic


async def download_unique_gift_sticker(
    client: Any,
    gift: Any,
    *,
    cache_dir: Optional[Path] = None,
    force: bool = False,
    timeout: Optional[float] = None,
) -> Optional[Path]:
    """Скачивает Lottie-анимацию МОДЕЛИ уникального подарка (``.unique.tgs``).

    Отличается от :func:`download_gift_sticker` двумя вещами: документ берётся
    из атрибута ``starGiftAttributeModel``, а файл кэша называется
    ``<id>.unique.tgs`` — иначе анимация модели перепуталась бы с анимацией
    «родителя» из каталога (``<id>.tgs``).
    """
    pass  # TODO: Commercial logic


async def download_unique_gift_pattern(
    client: Any,
    gift: Any,
    *,
    cache_dir: Optional[Path] = None,
    force: bool = False,
    timeout: Optional[float] = None,
) -> Optional[Path]:
    """Скачивает узор подложки уникального подарка в кэш.

    Файл называется ``<id>.pattern.<ext>``: расширение берётся у документа
    (``webp``/``png``/``tgs``), иначе узор не отличить от анимации модели
    (``<id>.unique.tgs``) и анимации «родителя» из каталога (``<id>.tgs``).
    """
    pass  # TODO: Commercial logic


def extract_lottie_json(tgs_path: Path, *, force: bool = False) -> Path:
    """Распаковывает ``.tgs`` (gzip) в ``.json`` рядом с исходником."""
    pass  # TODO: Commercial logic


async def ensure_gift_sticker(
    client: Any,
    gift_id: int,
    *,
    cache_dir: Optional[Path] = None,
    allow_fetch: bool = True,
) -> Optional[Path]:
    """Возвращает ``.tgs`` из кэша, при необходимости скачивая его.

    Если подарка нет в реестре (каталог ещё не запрашивали) — один раз
    обновляем каталог и повторяем попытку.
    """
    pass  # TODO: Commercial logic


async def _refresh_account_gifts(client: Any) -> None:
    """Обновляет реестр подарков аккаунта — вместе с размещёнными на профиле.

    ``payments.getSavedStarGifts`` отдаёт подарки, размещённые на профиле
    (``hosted``), только без флага ``exclude_hosted``, а у :func:`fetch_saved_gifts`
    он выставлен по умолчанию. С ним коллекционный подарок, стоящий на профиле, в
    реестр не попадал, и его анимация не находилась: в сетке вместо подарка
    оставался эмодзи-значок. Юзербот старой версии может не понять параметр —
    тогда спрашиваем как раньше, без него.
    """
    pass  # TODO: Commercial logic


async def ensure_unique_gift_sticker(
    client: Any,
    unique_id: int,
    *,
    cache_dir: Optional[Path] = None,
) -> Optional[Path]:
    """Возвращает ``.unique.tgs`` из кэша, при необходимости скачивая его.

    Если подарка нет в реестре (список подарков аккаунта ещё не запрашивали) —
    один раз обновляем список (вместе с размещёнными на профиле) и повторяем
    попытку.
    """
    pass  # TODO: Commercial logic


async def ensure_unique_gift_pattern(
    client: Any,
    unique_id: int,
    *,
    cache_dir: Optional[Path] = None,
) -> Optional[Path]:
    """Возвращает файл узора подложки из кэша, при необходимости скачивая его.

    Работает как :func:`ensure_unique_gift_sticker`: подарка может не быть в
    реестре, и тогда список подарков аккаунта обновляется один раз (вместе с
    размещёнными на профиле), после чего попытка повторяется.
    """
    pass  # TODO: Commercial logic


# --------------------------------------------------------------------------- #
#                        ПЕРЕДАЧА ПОДАРКА С АККАУНТА                           #
# --------------------------------------------------------------------------- #
def _saved_gift_input(*, msg_id: Optional[int] = None, slug: Optional[str] = None) -> Any:
    """Ссылка на полученный подарок для действий с ним (``InputSavedStarGift``).

    Для «своих» подарков Telegram принимает ``msg_id``
    (``inputSavedStarGiftUser``). У уникальных подарков всегда есть ``slug`` —
    он выручает, если у записи нет номера сообщения.
    """
    pass  # TODO: Commercial logic


async def saved_gift_present(
    client: Any,
    *,
    msg_id: Optional[int] = None,
    slug: Optional[str] = None,
    use_layer: Optional[bool] = None,
    timeout: Optional[float] = None,
) -> bool:
    """Лежит ли подарок всё ещё на аккаунте (``payments.getSavedStarGift``)."""
    pass  # TODO: Commercial logic


async def transfer_saved_gift(
    client: Any,
    *,
    to_user_id: int,
    msg_id: Optional[int] = None,
    slug: Optional[str] = None,
    timeout: Optional[float] = None,
) -> Dict[str, Any]:
    """Передаёт ПОДАРОК С АККАУНТА другому пользователю.

    ``payments.transferStarGift`` умеет только владелец подарка, поэтому выдача
    «подарка с аккаунта» идёт через юзербот, а не через бота.

    Ответ — ``Updates`` в формате заявленного слоя: внутри бывают типы, которых
    нет в Pyrogram (``messageActionStarGiftUnique#7e1c1187``), поэтому разбор
    ответа может оборваться, а будущее запроса — так и не разрешиться (см.
    комментарии в :mod:`app.user_bot.gifts_tl`). Отсюда правила:

    * запрос уходит **один раз** (передача — мутация, повторы ``_invoke`` здесь
      не годятся: вторая попытка рискует отправить подарок дважды);
    * итог проверяется отдельным запросом :func:`saved_gift_present`: подарка на
      аккаунте нет — передача состоялась, что бы ни пришло в ответе. Подарок на
      месте — наружу уходит ошибка, и владелец видит, что подарок не ушёл.
    """
    pass  # TODO: Commercial logic
