"""
Вендорный слой TL-схемы Telegram для «подарков» (Star Gifts).

Зачем это нужно
---------------
Проект использует Pyrogram ``2.0.106`` (слой 158). В нём нет ни методов
``payments.getStarGifts`` / ``payments.getSavedStarGifts``, ни типов
``starGift`` / ``payments.starGifts`` / ``savedStarGift``, потому что «подарки
за звёзды» появились в API заметно позже. Обновлять/патчить саму библиотеку
нельзя — юзербот обслуживает всю остальную логику проекта.

Решение
-------
Здесь лежит минимальный самодостаточный набор TL-объектов (классы
``pyrogram.raw.core.TLObject`` с методами ``read``/``write``) и регистрация их
constructor-id в рантайм-реестре Pyrogram — ``pyrogram.raw.all.objects``.
Этот реестр (тот же самый dict) использует ``pyrogram.raw.core.TLObject.read``
и, соответственно, сессия Pyrogram при разборе входящих MTProto-сообщений.
Поэтому зарегистрированные типы корректно декодируются из ответов Telegram.

Схема взята из актуальной документации Telegram и сознательно «широкая»:
читаются ВСЕ поля текущего слоя, даже не нужные приложению — иначе разбор
ответа съезжает по байтам.

Но «широкая» схема не спасает от объектов, которых в ней нет вовсе: Telegram
подменяет вложенные типы объектами **своего** слоя. Пример из жизни —
``payments.getStarGifts`` под ``invokeWithLayer(225)`` возвращает
``channel#1c32b11c`` (это ``channel`` слоя 225), а реестр Pyrogram знает только
``channel#83259464`` (слой 158). ``KeyError`` на таком элементе раньше уносил
весь разбор пакета: будущее запроса не разрешалось, HTTP-запрос истекал по
таймауту и Mini App получал 502. Поэтому вспомогательные векторы в ответах
разбираются толерантно (:func:`_read_vector_tolerant`): незнакомый конструктор
больше не роняет разбор — приложение получает всё, что успело прочитаться,
а остаток ответа пропускается.

Что добавлено
-------------
Функции:

* ``payments.getStarGifts``      — каталог доступных подарков;
* ``payments.getSavedStarGifts`` — подарки, полученные аккаунтом;
* ``payments.transferStarGift``  — передача полученного подарка (в том числе
  уникального) другому пользователю;
* ``payments.getSavedStarGift``  — состояние конкретных подарков (им проверяем
  итог передачи).

Типы (ответы):

* ``payments.starGifts`` / ``payments.starGiftsNotModified`` / ``starGift`` /
  ``starGiftBackground``;
* ``payments.savedStarGifts`` / ``savedStarGift``;
* ``starGiftUnique`` — уникальный (коллекционный) подарок, вместе с его
  атрибутами: ``starGiftAttributeModel`` (модель-анимация),
  ``starGiftAttributePattern`` (узор), ``starGiftAttributeBackdrop``
  (подложка) и ``starGiftAttributeOriginalDetails`` (даритель, дата,
  подпись) + ``starGiftAttributeRarity*`` (редкость) и вложенные
  ``peerColor*`` / ``starsAmount`` / ``starsTonAmount``;
* ``inputSavedStarGiftUser`` / ``inputSavedStarGiftChat`` /
  ``inputSavedStarGiftSlug`` — ссылка на конкретный полученный подарок
  (ей адресуются передача и обмен).

Использование
-------------
    from app.user_bot import gifts_tl  # noqa: F401 (побочный эффект: регистрация)

    query = gifts_tl.PaymentsGetStarGifts(hash=0)
    payload = gifts_tl.wrap_with_layer(query, client=client)  # invokeWithLayer + initConnection
    result = await client.invoke(payload)
    for gift in result.gifts:
        print(gift.id, gift.title, gift.stars)

Никакая существующая логика юзербота не меняется: модуль только добавляет
новые конструкторы в реестр (``setdefault``-семантика, существующие id не
трогаются).
"""

from __future__ import annotations

import logging
from io import BytesIO
from typing import Any, Dict, List, Optional

from pyrogram import raw
from pyrogram.raw.all import layer as PYROGRAM_LAYER, objects as _registry
from pyrogram.raw.core import TLObject
from pyrogram.raw.core.primitives import Bool, Int, Long, String, Vector

logger = logging.getLogger(__name__)

__all__ = [
    "TL_LAYER",
    "PYROGRAM_LAYER",
    "PaymentsGetStarGifts",
    "PaymentsGetSavedStarGifts",
    "PaymentsTransferStarGift",
    "PaymentsGetSavedStarGift",
    "PaymentsStarGifts",
    "PaymentsStarGiftsNotModified",
    "PaymentsSavedStarGifts",
    "StarGift",
    "StarGiftUnique",
    "StarGiftBackground",
    "StarGiftAttributeModel",
    "StarGiftAttributePattern",
    "StarGiftAttributeBackdrop",
    "StarGiftAttributeOriginalDetails",
    "StarGiftAttributeRarity",
    "StarGiftAttributeRarityUncommon",
    "StarGiftAttributeRarityRare",
    "StarGiftAttributeRarityEpic",
    "StarGiftAttributeRarityLegendary",
    "StarsAmount",
    "StarsTonAmount",
    "PeerColor",
    "PeerColorCollectible",
    "InputPeerColorCollectible",
    "SavedStarGift",
    "InputSavedStarGiftUser",
    "InputSavedStarGiftChat",
    "InputSavedStarGiftSlug",
    "connection_params",
    "wrap_with_layer",
    "register_vendor_types",
]

#: Слой, который объявляется серверу для запросов подарков. Если заявленный
#: слой выше серверного, Telegram использует свой максимум — это безопасно.
#: Объявлять слой нужно только через :func:`wrap_with_layer`: он вкладывает
#: запрос в ``initConnection``, без которого Telegram отвечает
#: ``400 CONNECTION_LAYER_INVALID``.
#:
#: Держим ровно 225 — это слой, из документации которого собраны здешние типы
#: (``starGift#313a9547``, ``savedStarGift#41df43fc``, ``payments.starGifts#2ed82995``).
#: Слой нельзя занижать: ответ приходит в формате **заявленного** слоя, и на
#: слое 200 сервер прислал бы другой вариант тех же объектов — с чужими
#: constructor-id, которые не разберёт ни наш модуль, ни Pyrogram.
TL_LAYER = 225


def register_vendor_types() -> List[int]:
    """Регистрирует вендорные конструкторы в рантайм-реестре Pyrogram.

    Возвращает список constructor-id, которые реально были добавлены.
    Существующие конструкторы не перезаписываются.
    """
    pass  # TODO: Commercial logic


def _read_bool(data: BytesIO) -> bool:
    """``Bool`` — это либо ``boolTrue``, либо ``boolFalse`` (4 байта)."""
    pass  # TODO: Commercial logic


#: Конструктор любого TL-вектора: ``vector#1cb5c415 {t:Type} # [t] = Vector t``.
VECTOR_ID = 0x1CB5C415


def _read_vector(data: BytesIO, element_reader: Any = None) -> list:
    """Точно читает ``Vector<T>``: constructor-id + count + элементы.

    Pyrogram умеет читать векторы через ``TLObject.read``, но там включается
    эвристика ``Vector.read_bare`` (размер элемента = остаток/количество),
    которая ошибается, когда вектор — не последнее поле записи. Здесь вектор
    разбирается однозначно.

    ``element_reader(data)`` вызывается для каждого элемента; по умолчанию —
    ``TLObject.read`` (разбор по constructor-id).
    """
    pass  # TODO: Commercial logic


def _at_end(data: BytesIO) -> bool:
    """Остались ли в теле ответа непрочитанные байты."""
    pass  # TODO: Commercial logic


def _read_vector_tolerant(data: BytesIO, label: str = "") -> list:
    """Читает ``Vector<T>``, не роняя разбор ответа на незнакомом конструкторе.

    Telegram отвечает объектами **своего** слоя: в ``payments.starGifts``
    приходит, например, ``channel#1c32b11c`` (это ``channel`` слоя 225), а
    реестр Pyrogram знает только ``channel#83259464`` (слой 158). Длину такого
    элемента узнать неоткуда, поэтому разбираем всё, что успели, и съедаем
    остаток тела: иначе разбор «съедет» и ``KeyError`` прилетит уже на
    следующем поле, а исключение из обработчика пакета не разрешает будущее
    запроса — вызывающий код получает таймаут (и 502 в Mini App).

    Возвращает прочитанный префикс вектора; о проблеме пишет в лог.
    """
    pass  # TODO: Commercial logic


# --------------------------------------------------------------------------- #
#                          ТИПЫ: КАТАЛОГ ПОДАРКОВ                             #
# --------------------------------------------------------------------------- #


class StarGiftBackground(TLObject):  # type: ignore[misc]
    """``starGiftBackground`` — цвета подложки карточки подарка.

    TL: ``starGiftBackground#aff56398 center_color:int edge_color:int
    text_color:int = StarGiftBackground``
    """

    __slots__: List[str] = ["center_color", "edge_color", "text_color"]

    ID = 0xAFF56398
    QUALNAME = "types.StarGiftBackground"

    def __init__(self, *, center_color: int, edge_color: int, text_color: int) -> None:
        pass  # TODO: Commercial logic

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "StarGiftBackground":
        pass  # TODO: Commercial logic

    def write(self, *args: Any) -> bytes:
        pass  # TODO: Commercial logic


class StarGift(TLObject):  # type: ignore[misc]
    """``starGift`` — один подарок из каталога.

    TL (актуальный слой)::

        starGift#313a9547 flags:# limited:flags.0?true sold_out:flags.1?true
            birthday:flags.2?true require_premium:flags.7?true
            limited_per_user:flags.8?true peer_color_available:flags.10?true
            auction:flags.11?true id:long sticker:Document stars:long
            availability_remains:flags.0?int availability_total:flags.0?int
            availability_resale:flags.4?long convert_stars:long
            first_sale_date:flags.1?date last_sale_date:flags.1?date
            upgrade_stars:flags.3?long resell_min_stars:flags.4?long
            title:flags.5?string released_by:flags.6?Peer
            per_user_total:flags.8?int per_user_remains:flags.8?int
            locked_until_date:flags.9?date auction_slug:flags.11?string
            gifts_per_round:flags.11?int auction_start_date:flags.11?date
            upgrade_variants:flags.12?int background:flags.13?StarGiftBackground
            = StarGift

    Приложению нужны ``id``, ``title``, ``stars``, ``convert_stars`` и
    ``sticker`` (Lottie-анимация). Читаются, тем не менее, все поля — иначе
    разбор ответа съедет по байтам.
    """

    __slots__: List[str] = [
        "flags",
        "limited",
        "sold_out",
        "birthday",
        "require_premium",
        "limited_per_user",
        "peer_color_available",
        "auction",
        "id",
        "sticker",
        "stars",
        "availability_remains",
        "availability_total",
        "availability_resale",
        "convert_stars",
        "first_sale_date",
        "last_sale_date",
        "upgrade_stars",
        "resell_min_stars",
        "title",
        "released_by",
        "per_user_total",
        "per_user_remains",
        "locked_until_date",
        "auction_slug",
        "gifts_per_round",
        "auction_start_date",
        "upgrade_variants",
        "background",
    ]

    ID = 0x313A9547
    #: ``StarGift`` — союз ``starGift`` | ``starGiftUnique``. Поддержан только
    #: обычный подарок (каталог + полученные с ``exclude_unique=True``).
    QUALNAME = "types.StarGift"

    def __init__(
        self,
        *,
        flags: int = 0,
        limited: Optional[bool] = None,
        sold_out: Optional[bool] = None,
        birthday: Optional[bool] = None,
        require_premium: Optional[bool] = None,
        limited_per_user: Optional[bool] = None,
        peer_color_available: Optional[bool] = None,
        auction: Optional[bool] = None,
        id: Optional[int] = None,  # noqa: A002 - имя поля из TL
        sticker: Any = None,
        stars: Optional[int] = None,
        availability_remains: Optional[int] = None,
        availability_total: Optional[int] = None,
        availability_resale: Optional[int] = None,
        convert_stars: Optional[int] = None,
        first_sale_date: Optional[int] = None,
        last_sale_date: Optional[int] = None,
        upgrade_stars: Optional[int] = None,
        resell_min_stars: Optional[int] = None,
        title: Optional[str] = None,
        released_by: Any = None,
        per_user_total: Optional[int] = None,
        per_user_remains: Optional[int] = None,
        locked_until_date: Optional[int] = None,
        auction_slug: Optional[str] = None,
        gifts_per_round: Optional[int] = None,
        auction_start_date: Optional[int] = None,
        upgrade_variants: Optional[int] = None,
        background: Any = None,
    ) -> None:
        pass  # TODO: Commercial logic

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "StarGift":
        pass  # TODO: Commercial logic

    def write(self, *args: Any) -> bytes:
        pass  # TODO: Commercial logic


# --------------------------------------------------------------------------- #
#              ТИПЫ: УНИКАЛЬНЫЕ (КОЛЛЕКЦИОННЫЕ) ПОДАРКИ                        #
# --------------------------------------------------------------------------- #
# Уникальный подарок — это «прокачанная» версия обычного, у Telegram у него
# отдельный тип (``starGiftUnique``). Его картинка собирается из атрибутов:
# модель (``starGiftAttributeModel``), узор (``starGiftAttributePattern``) и
# подложка (``starGiftAttributeBackdrop``); фон и анимация лежат НЕ в
# ``sticker``, как у обычного подарка.
#
# Pyrogram слоя 158 не знает ни одного из этих типов, поэтому
# ``payments.getSavedStarGifts`` с ``exclude_unique=False`` раньше ломал бы
# разбор ответа: сначала на самом ``starGiftUnique``, затем на вложенных
# ``peerColor*`` / ``starsAmount`` / ``starGiftAttributeRarity*``.
# Все они собраны здесь по той же схеме слоя 225, что и ``starGift``.


class PeerColor(TLObject):  # type: ignore[misc]
    """``peerColor`` — обычный (не коллекционный) цвет профиля собеседника.

    TL: ``peerColor#b54b5acf flags:# color:flags.0?int
    background_emoji_id:flags.1?long = PeerColor``

    Читается как вложенное поле ``starGiftUnique`` (``theme_peer`` /
    ``peer_color``): без него разбор уникального подарка съедет по байтам.
    """

    __slots__: List[str] = ["flags", "color", "background_emoji_id"]

    ID = 0xB54B5ACF
    QUALNAME = "types.PeerColor"

    def __init__(
        self,
        *,
        flags: int = 0,
        color: Optional[int] = None,
        background_emoji_id: Optional[int] = None,
    ) -> None:
        pass  # TODO: Commercial logic

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "PeerColor":
        pass  # TODO: Commercial logic

    def write(self, *args: Any) -> bytes:
        pass  # TODO: Commercial logic


class PeerColorCollectible(TLObject):  # type: ignore[misc]
    """``peerColorCollectible`` — коллекционный цвет профиля.

    TL: ``peerColorCollectible#b9c0639a flags:# collectible_id:long
    gift_emoji_id:long background_emoji_id:long accent_color:int
    colors:Vector<int> dark_accent_color:flags.0?int
    dark_colors:flags.1?Vector<int> = PeerColor``
    """

    __slots__: List[str] = [
        "flags",
        "collectible_id",
        "gift_emoji_id",
        "background_emoji_id",
        "accent_color",
        "colors",
        "dark_accent_color",
        "dark_colors",
    ]

    ID = 0xB9C0639A
    QUALNAME = "types.PeerColor"

    def __init__(self, **kwargs: Any) -> None:
        pass  # TODO: Commercial logic

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "PeerColorCollectible":
        pass  # TODO: Commercial logic

    def write(self, *args: Any) -> bytes:
        pass  # TODO: Commercial logic


class InputPeerColorCollectible(TLObject):  # type: ignore[misc]
    """``inputPeerColorCollectible`` — ссылка на коллекционный цвет профиля.

    TL: ``inputPeerColorCollectible#b8ea86a9 collectible_id:long = PeerColor``

    Тип «входной», но объявлен членом союза ``PeerColor`` — регистрируем на
    случай, если сервер пришлёт его в ответе (иначе разбор ответа упадёт).
    """

    __slots__: List[str] = ["collectible_id"]

    ID = 0xB8EA86A9
    QUALNAME = "types.PeerColor"

    def __init__(self, *, collectible_id: int) -> None:
        pass  # TODO: Commercial logic

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "InputPeerColorCollectible":
        pass  # TODO: Commercial logic

    def write(self, *args: Any) -> bytes:
        pass  # TODO: Commercial logic


class StarsAmount(TLObject):  # type: ignore[misc]
    """``starsAmount`` — сумма в звёздах с «наночастью».

    TL: ``starsAmount#bbb6b4a3 amount:long nanos:int = StarsAmount``

    Встречается внутри ``starGiftUnique`` (``resell_amount``).
    """

    __slots__: List[str] = ["amount", "nanos"]

    ID = 0xBBB6B4A3
    QUALNAME = "types.StarsAmount"

    def __init__(self, *, amount: int, nanos: int) -> None:
        pass  # TODO: Commercial logic

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "StarsAmount":
        pass  # TODO: Commercial logic

    def write(self, *args: Any) -> bytes:
        pass  # TODO: Commercial logic


class StarsTonAmount(TLObject):  # type: ignore[misc]
    """``starsTonAmount`` — сумма в TON.

    TL: ``starsTonAmount#74aee3e0 amount:long = StarsAmount``
    """

    __slots__: List[str] = ["amount"]

    ID = 0x74AEE3E0
    QUALNAME = "types.StarsAmount"

    def __init__(self, *, amount: int) -> None:
        pass  # TODO: Commercial logic

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "StarsTonAmount":
        pass  # TODO: Commercial logic

    def write(self, *args: Any) -> bytes:
        pass  # TODO: Commercial logic


class StarGiftUnique(TLObject):  # type: ignore[misc]
    """``starGiftUnique`` — уникальный (коллекционный) подарок.

    TL (слой 225):::

        starGiftUnique#85f0a9cd flags:# require_premium:flags.6?true
            resale_ton_only:flags.7?true theme_available:flags.9?true
            burned:flags.14?true crafted:flags.15?true id:long gift_id:long
            title:string slug:string num:int owner_id:flags.0?Peer
            owner_name:flags.1?string owner_address:flags.2?string
            attributes:Vector<StarGiftAttribute> availability_issued:int
            availability_total:int gift_address:flags.3?string
            resell_amount:flags.4?Vector<StarsAmount> released_by:flags.5?Peer
            value_amount:flags.8?long value_currency:flags.8?string
            value_usd_amount:flags.8?long theme_peer:flags.10?Peer
            peer_color:flags.11?PeerColor host_id:flags.12?Peer
            offer_min_stars:flags.13?int craft_chance_permille:flags.16?int
            = StarGift

    Чем отличается от обычного ``starGift``:

    * ``id`` — id **экземпляра** (свой у каждого владельца), а не каталога:
      по нему нельзя ни купить подарок, ни запросить анимацию из каталога;
    * ``gift_id`` — id «родителя» в каталоге (отсюда подарок «вырос»);
    * ``num`` — номер экземпляра (то самое ``#35 651``);
    * ``slug`` — ссылка на подарок в клиентах (t.me/nft/...);
    * ``sticker`` нет — картинка собирается из ``attributes``
      (модель + узор + подложка).

    ``write`` не поддержан: тип только разбирается (мы его никогда не
    отправляем — для запросов есть ``InputSavedStarGift*``).
    """

    __slots__: List[str] = [
        "flags",
        "require_premium",
        "resale_ton_only",
        "theme_available",
        "burned",
        "crafted",
        "id",
        "gift_id",
        "title",
        "slug",
        "num",
        "owner_id",
        "owner_name",
        "owner_address",
        "attributes",
        "availability_issued",
        "availability_total",
        "gift_address",
        "resell_amount",
        "released_by",
        "value_amount",
        "value_currency",
        "value_usd_amount",
        "theme_peer",
        "peer_color",
        "host_id",
        "offer_min_stars",
        "craft_chance_permille",
    ]

    ID = 0x85F0A9CD
    QUALNAME = "types.StarGift"

    def __init__(self, **kwargs: Any) -> None:
        pass  # TODO: Commercial logic

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "StarGiftUnique":
        pass  # TODO: Commercial logic

    def write(self, *args: Any) -> bytes:
        pass  # TODO: Commercial logic


class StarGiftAttributeModel(TLObject):  # type: ignore[misc]
    """``starGiftAttributeModel`` — атрибут «модель» (анимация подарка).

    TL: ``starGiftAttributeModel#565251e2 flags:# crafted:flags.0?true
    name:string document:Document rarity:StarGiftAttributeRarity
    = StarGiftAttribute``

    ``document`` — та самая Lottie-анимация «прокачанного» подарка: именно её
    показывает клиент Telegram. У обычного подарка анимация лежит в
    ``starGift.sticker``, у уникального — здесь.
    """

    __slots__: List[str] = ["flags", "crafted", "name", "document", "rarity"]

    ID = 0x565251E2
    QUALNAME = "types.StarGiftAttribute"

    def __init__(self, **kwargs: Any) -> None:
        pass  # TODO: Commercial logic

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "StarGiftAttributeModel":
        pass  # TODO: Commercial logic

    def write(self, *args: Any) -> bytes:
        pass  # TODO: Commercial logic


class StarGiftAttributePattern(TLObject):  # type: ignore[misc]
    """``starGiftAttributePattern`` — атрибут «узор» (фоновая анимация).

    TL: ``starGiftAttributePattern#4e7085ea name:string document:Document
    rarity:StarGiftAttributeRarity = StarGiftAttribute``
    """

    __slots__: List[str] = ["name", "document", "rarity"]

    ID = 0x4E7085EA
    QUALNAME = "types.StarGiftAttribute"

    def __init__(self, **kwargs: Any) -> None:
        pass  # TODO: Commercial logic

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "StarGiftAttributePattern":
        pass  # TODO: Commercial logic

    def write(self, *args: Any) -> bytes:
        pass  # TODO: Commercial logic


class StarGiftAttributeBackdrop(TLObject):  # type: ignore[misc]
    """``starGiftAttributeBackdrop`` — атрибут «подложка» (цвета карточки).

    TL: ``starGiftAttributeBackdrop#9f2504e4 name:string backdrop_id:int
    center_color:int edge_color:int pattern_color:int text_color:int
    rarity:StarGiftAttributeRarity = StarGiftAttribute``

    Цвета — те же три, что у ``starGiftBackground`` обычного подарка, плюс
    ``pattern_color`` для узора. Приложению нужны, чтобы нарисовать карточку
    уникального подарка в пикере (у обычных это делают по ``background``).
    """

    __slots__: List[str] = [
        "name",
        "backdrop_id",
        "center_color",
        "edge_color",
        "pattern_color",
        "text_color",
        "rarity",
    ]

    ID = 0x9F2504E4
    QUALNAME = "types.StarGiftAttribute"

    def __init__(self, **kwargs: Any) -> None:
        pass  # TODO: Commercial logic

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "StarGiftAttributeBackdrop":
        pass  # TODO: Commercial logic

    def write(self, *args: Any) -> bytes:
        pass  # TODO: Commercial logic


class StarGiftAttributeOriginalDetails(TLObject):  # type: ignore[misc]
    """``starGiftAttributeOriginalDetails`` — «память» о первом вручении.

    TL: ``starGiftAttributeOriginalDetails#e0bff26c flags:#
    sender_id:flags.0?Peer recipient_id:Peer date:int
    message:flags.1?TextWithEntities = StarGiftAttribute``

    Уникальный подарок можно «переплавить» — тогда от исходного вручения
    остаётся только этот атрибут.
    """

    __slots__: List[str] = [
        "flags",
        "sender_id",
        "recipient_id",
        "date",
        "message",
    ]

    ID = 0xE0BFF26C
    QUALNAME = "types.StarGiftAttribute"

    def __init__(self, **kwargs: Any) -> None:
        pass  # TODO: Commercial logic

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "StarGiftAttributeOriginalDetails":
        pass  # TODO: Commercial logic

    def write(self, *args: Any) -> bytes:
        pass  # TODO: Commercial logic


class StarGiftAttributeRarity(TLObject):  # type: ignore[misc]
    """``starGiftAttributeRarity#36437737 permille:int`` — точная редкость.

    ``permille`` — сколько таких атрибутов выпадает на тысячу подарков.
    """

    __slots__: List[str] = ["permille"]

    ID = 0x36437737
    QUALNAME = "types.StarGiftAttributeRarity"

    def __init__(self, *, permille: int) -> None:
        pass  # TODO: Commercial logic

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "StarGiftAttributeRarity":
        pass  # TODO: Commercial logic

    def write(self, *args: Any) -> bytes:
        pass  # TODO: Commercial logic


class StarGiftAttributeRarityUncommon(TLObject):  # type: ignore[misc]
    """``starGiftAttributeRarityUncommon#dbce6389`` — редкость «необычная»."""

    __slots__: List[str] = []

    ID = 0xDBCE6389
    QUALNAME = "types.StarGiftAttributeRarity"

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "StarGiftAttributeRarityUncommon":
        pass  # TODO: Commercial logic

    def write(self, *args: Any) -> bytes:
        pass  # TODO: Commercial logic


class StarGiftAttributeRarityRare(TLObject):  # type: ignore[misc]
    """``starGiftAttributeRarityRare#f08d516b`` — редкость «редкая»."""

    __slots__: List[str] = []

    ID = 0xF08D516B
    QUALNAME = "types.StarGiftAttributeRarity"

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "StarGiftAttributeRarityRare":
        pass  # TODO: Commercial logic

    def write(self, *args: Any) -> bytes:
        pass  # TODO: Commercial logic


class StarGiftAttributeRarityEpic(TLObject):  # type: ignore[misc]
    """``starGiftAttributeRarityEpic#78fbf3a8`` — редкость «эпическая»."""

    __slots__: List[str] = []

    ID = 0x78FBF3A8
    QUALNAME = "types.StarGiftAttributeRarity"

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "StarGiftAttributeRarityEpic":
        pass  # TODO: Commercial logic

    def write(self, *args: Any) -> bytes:
        pass  # TODO: Commercial logic


class StarGiftAttributeRarityLegendary(TLObject):  # type: ignore[misc]
    """``starGiftAttributeRarityLegendary#cef7e7a8`` — редкость «легендарная»."""

    __slots__: List[str] = []

    ID = 0xCEF7E7A8
    QUALNAME = "types.StarGiftAttributeRarity"

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "StarGiftAttributeRarityLegendary":
        pass  # TODO: Commercial logic

    def write(self, *args: Any) -> bytes:
        pass  # TODO: Commercial logic


class PaymentsStarGifts(TLObject):  # type: ignore[misc]
    """``payments.starGifts`` — ответ ``payments.getStarGifts``.

    TL: ``payments.starGifts#2ed82995 hash:int gifts:Vector<StarGift>
    chats:Vector<Chat> users:Vector<User> = payments.StarGifts``

    ``gifts`` разбираются точно, ``chats``/``users`` — «по возможности»: Telegram
    кладёт туда объекты своего слоя (``channel#1c32b11c`` — слой 225), которых
    нет в реестре Pyrogram (слой 158). Потерять их не страшно (по ним только
    показываются имена отправителей), а падение разбора раньше роняло весь
    ответ целиком.
    """

    __slots__: List[str] = ["hash", "gifts", "chats", "users"]

    ID = 0x2ED82995
    QUALNAME = "types.payments.StarGifts"

    def __init__(self, *, hash: int, gifts: list, chats: list, users: list) -> None:  # noqa: A002
        pass  # TODO: Commercial logic

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "PaymentsStarGifts":
        pass  # TODO: Commercial logic

    def write(self, *args: Any) -> bytes:
        pass  # TODO: Commercial logic


class PaymentsStarGiftsNotModified(TLObject):  # type: ignore[misc]
    """``payments.starGiftsNotModified`` — кэш каталога актуален.

    TL: ``payments.starGiftsNotModified#a388a368 = payments.StarGifts``.
    Мы всегда запрашиваем ``hash=0``, но тип всё равно регистрируем: иначе
    неожиданный ответ сломает разбор пакета.
    """

    __slots__: List[str] = []

    ID = 0xA388A368
    QUALNAME = "types.payments.StarGiftsNotModified"

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "PaymentsStarGiftsNotModified":
        pass  # TODO: Commercial logic

    def write(self, *args: Any) -> bytes:
        pass  # TODO: Commercial logic


# --------------------------------------------------------------------------- #
#                  ТИПЫ: ПОЛУЧЕННЫЕ (СОХРАНЁННЫЕ) ПОДАРКИ                     #
# --------------------------------------------------------------------------- #

class SavedStarGift(TLObject):  # type: ignore[misc]
    """``savedStarGift`` — полученный подарок в списке аккаунта.

    TL (актуальный слой)::

        savedStarGift#41df43fc flags:# name_hidden:flags.0?true
            unsaved:flags.5?true refunded:flags.9?true can_upgrade:flags.10?true
            pinned_to_top:flags.12?true upgrade_separate:flags.17?true
            from_id:flags.1?Peer date:date gift:StarGift
            message:flags.2?TextWithEntities msg_id:flags.3?int
            saved_id:flags.11?long convert_stars:flags.4?long
            upgrade_stars:flags.6?long can_export_at:flags.7?int
            transfer_stars:flags.8?long can_transfer_at:flags.13?int
            can_resell_at:flags.14?int collection_id:flags.15?Vector<int>
            prepaid_upgrade_hash:flags.16?string
            drop_original_details_stars:flags.18?long gift_num:flags.19?int
            can_craft_at:flags.20?int = SavedStarGift
    """

    __slots__: List[str] = [
        "flags",
        "name_hidden",
        "unsaved",
        "refunded",
        "can_upgrade",
        "pinned_to_top",
        "upgrade_separate",
        "from_id",
        "date",
        "gift",
        "message",
        "msg_id",
        "saved_id",
        "convert_stars",
        "upgrade_stars",
        "can_export_at",
        "transfer_stars",
        "can_transfer_at",
        "can_resell_at",
        "collection_id",
        "prepaid_upgrade_hash",
        "drop_original_details_stars",
        "gift_num",
        "can_craft_at",
    ]

    ID = 0x41DF43FC
    QUALNAME = "types.SavedStarGift"

    def __init__(self, **kwargs: Any) -> None:
        pass  # TODO: Commercial logic

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "SavedStarGift":
        pass  # TODO: Commercial logic

    def write(self, *args: Any) -> bytes:
        pass  # TODO: Commercial logic


class PaymentsSavedStarGifts(TLObject):  # type: ignore[misc]
    """``payments.savedStarGifts`` — ответ ``payments.getSavedStarGifts``.

    TL::

        payments.savedStarGifts#95f389b1 flags:# count:int
            chat_notifications_enabled:flags.1?Bool gifts:Vector<SavedStarGift>
            next_offset:flags.0?string chats:Vector<Chat> users:Vector<User>
            = payments.SavedStarGifts

    ``gifts`` разбираются точно, ``chats``/``users`` — «по возможности»
    (см. :func:`_read_vector_tolerant`): в них могут быть объекты чужого слоя.
    """

    __slots__: List[str] = [
        "flags",
        "count",
        "chat_notifications_enabled",
        "gifts",
        "next_offset",
        "chats",
        "users",
    ]

    ID = 0x95F389B1
    QUALNAME = "types.payments.SavedStarGifts"

    def __init__(
        self,
        *,
        flags: int,
        count: int,
        chat_notifications_enabled: Optional[bool],
        gifts: list,
        next_offset: Optional[str],
        chats: list,
        users: list,
    ) -> None:
        pass  # TODO: Commercial logic

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "PaymentsSavedStarGifts":
        pass  # TODO: Commercial logic

    def write(self, *args: Any) -> bytes:
        pass  # TODO: Commercial logic

# --------------------------------------------------------------------------- #
#             ТИПЫ: ССЫЛКА НА ПОЛУЧЕННЫЙ ПОДАРК (ВХОДНЫЕ)                      #
# --------------------------------------------------------------------------- #
# Действия с подарком на аккаунте (передача, обмен на звёзды, переплавка)
# адресуются не по id каталога, а по записи о вручении — ``inputSavedStarGift*``:
# для подарка из «своих» хватает ``msg_id``, для подарка в чате — пары
# «пир + saved_id», а если известен только ``slug`` (имя уникального подарка) —
# хватает его одного.


class InputSavedStarGiftUser(TLObject):  # type: ignore[misc]
    """``inputSavedStarGiftUser#69279795 msg_id:int = InputSavedStarGift``.

    Подарок из «своих» (полученных) подарков аккаунта: ``msg_id`` — номер
    сообщения с подарком в списке ``payments.getSavedStarGifts``.
    """

    __slots__: List[str] = ["msg_id"]

    ID = 0x69279795
    QUALNAME = "types.InputSavedStarGift"

    def __init__(self, *, msg_id: int) -> None:
        pass  # TODO: Commercial logic

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "InputSavedStarGiftUser":
        pass  # TODO: Commercial logic

    def write(self, *args: Any) -> bytes:
        pass  # TODO: Commercial logic


class InputSavedStarGiftChat(TLObject):  # type: ignore[misc]
    """``inputSavedStarGiftChat#f101aa7f peer:InputPeer saved_id:long = InputSavedStarGift``.

    Подарок, который лежит в чате/канале (его ``saved_id``).
    """

    __slots__: List[str] = ["peer", "saved_id"]

    ID = 0xF101AA7F
    QUALNAME = "types.InputSavedStarGift"

    def __init__(self, *, peer: Any, saved_id: int) -> None:
        pass  # TODO: Commercial logic

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "InputSavedStarGiftChat":
        pass  # TODO: Commercial logic

    def write(self, *args: Any) -> bytes:
        pass  # TODO: Commercial logic


class InputSavedStarGiftSlug(TLObject):  # type: ignore[misc]
    """``inputSavedStarGiftSlug#2085c238 slug:string = InputSavedStarGift``.

    Подарок по имени (``slug``) — так адресуются уникальные подарки, даже если
    у записи нет ``msg_id``.
    """

    __slots__: List[str] = ["slug"]

    ID = 0x2085C238
    QUALNAME = "types.InputSavedStarGift"

    def __init__(self, *, slug: str) -> None:
        pass  # TODO: Commercial logic

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "InputSavedStarGiftSlug":
        pass  # TODO: Commercial logic

    def write(self, *args: Any) -> bytes:
        pass  # TODO: Commercial logic


# --------------------------------------------------------------------------- #
#                                  ФУНКЦИИ                                    #
# --------------------------------------------------------------------------- #


class PaymentsGetStarGifts(TLObject):  # type: ignore[misc]
    """``payments.getStarGifts`` — каталог доступных подарков.

    TL: ``payments.getStarGifts#c4563590 hash:int = payments.StarGifts``.
    ``hash=0`` всегда возвращает полный список.
    """

    __slots__: List[str] = ["hash"]

    ID = 0xC4563590
    QUALNAME = "functions.payments.GetStarGifts"

    def __init__(self, *, hash: int = 0) -> None:  # noqa: A002 - имя поля из TL
        pass  # TODO: Commercial logic

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "PaymentsGetStarGifts":
        pass  # TODO: Commercial logic

    def write(self, *args: Any) -> bytes:
        pass  # TODO: Commercial logic


class PaymentsGetSavedStarGifts(TLObject):  # type: ignore[misc]
    """``payments.getSavedStarGifts`` — полученные аккаунтом подарки.

    TL::

        payments.getSavedStarGifts#a319e569 flags:#
            exclude_unsaved:flags.0?true exclude_saved:flags.1?true
            exclude_unlimited:flags.2?true exclude_unique:flags.4?true
            sort_by_value:flags.5?true exclude_upgradable:flags.7?true
            exclude_unupgradable:flags.8?true peer_color_available:flags.9?true
            exclude_hosted:flags.10?true peer:InputPeer
            collection_id:flags.6?int offset:string limit:int
            = payments.SavedStarGifts

    ``exclude_unique=True`` — берём только обычные подарки. Уникальные
    (коллекционные, ``starGiftUnique``) приходят без этого флага, и в списке
    подарков аккаунта они нужны: у них свои атрибуты (модель, узор, подложка),
    см. :func:`unique_gift_to_dict`.

    ``exclude_hosted=True`` — Telegram не отдаёт подарки, размещённые на профиле
    (``hosted``): владелец такого подарка — кошелёк TON. Список подарков аккаунта
    и анимации коллекционных подарков спрашивают без этого флага.
    """

    __slots__: List[str] = [
        "exclude_unsaved",
        "exclude_saved",
        "exclude_unlimited",
        "exclude_unique",
        "sort_by_value",
        "exclude_upgradable",
        "exclude_unupgradable",
        "peer_color_available",
        "exclude_hosted",
        "peer",
        "collection_id",
        "offset",
        "limit",
    ]

    ID = 0xA319E569
    QUALNAME = "functions.payments.GetSavedStarGifts"

    def __init__(
        self,
        *,
        peer: Any,
        offset: str = "",
        limit: int = 100,
        exclude_unique: bool = True,
        exclude_hosted: bool = True,
        collection_id: Optional[int] = None,
        exclude_unsaved: bool = False,
        exclude_saved: bool = False,
        exclude_unlimited: bool = False,
        sort_by_value: bool = False,
        exclude_upgradable: bool = False,
        exclude_unupgradable: bool = False,
        peer_color_available: bool = False,
    ) -> None:
        pass  # TODO: Commercial logic

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "PaymentsGetSavedStarGifts":
        pass  # TODO: Commercial logic

    def write(self, *args: Any) -> bytes:
        pass  # TODO: Commercial logic


class PaymentsTransferStarGift(TLObject):  # type: ignore[misc]
    """``payments.transferStarGift`` — передать полученный подарок другому.

    TL: ``payments.transferStarGift#7f18176a stargift:InputSavedStarGift
    to_id:InputPeer = Updates``

    Передать подарок может только его владелец, поэтому выдача «подарка с
    аккаунта» идёт через юзербот, а не через бота.

    Ответ — ``Updates``, и он приезжает в формате **заявленного** слоя (225):
    внутри бывают типы, которых в Pyrogram (слой 158) нет (например
    ``messageActionStarGiftUnique#7e1c1187``). Разбирать его мы не пытаемся
    (``gifts_logic.transfer_saved_gift`` проверяет результат отдельным
    запросом ``payments.getSavedStarGift``), поэтому ``read`` не поддержан.
    """

    __slots__: List[str] = ["stargift", "to_id"]

    ID = 0x7F18176A
    QUALNAME = "functions.payments.TransferStarGift"

    def __init__(self, *, stargift: TLObject, to_id: TLObject) -> None:
        pass  # TODO: Commercial logic

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "PaymentsTransferStarGift":
        pass  # TODO: Commercial logic

    def write(self, *args: Any) -> bytes:
        pass  # TODO: Commercial logic


class PaymentsGetSavedStarGift(TLObject):  # type: ignore[misc]
    """``payments.getSavedStarGift`` — записи о конкретных подарках.

    TL: ``payments.getSavedStarGift#b455a106 stargift:Vector<InputSavedStarGift>
    = payments.SavedStarGifts``

    Нужен, чтобы проверить итог передачи: подарок ушёл с аккаунта — значит,
    передача состоялась (см. ``gifts_logic.saved_gift_present``).
    """

    __slots__: List[str] = ["stargift"]

    ID = 0xB455A106
    QUALNAME = "functions.payments.GetSavedStarGift"

    def __init__(self, *, stargift: list) -> None:
        pass  # TODO: Commercial logic

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "PaymentsGetSavedStarGift":
        pass  # TODO: Commercial logic

    def write(self, *args: Any) -> bytes:
        pass  # TODO: Commercial logic


def connection_params(client: Any, api_id: Optional[int] = None) -> Dict[str, Any]:
    """Поля ``initConnection``, снятые с живого клиента Pyrogram.

    ``api_id`` можно передать явно (например, если он вычитан из хранилища
    сессии асинхронно) — иначе берём ``client.api_id``.
    """
    pass  # TODO: Commercial logic


def wrap_with_layer(
    query: TLObject,
    layer: int = TL_LAYER,
    *,
    client: Any = None,
    api_id: Optional[int] = None,
) -> TLObject:
    """Оборачивает запрос в ``invokeWithLayer``.

    Заявленный слой подсказывает Telegram, какую версию схемы мы ждём. Без
    обёртки клиент остаётся на слое 158 (слой Pyrogram) и подарки могут
    приехать в старом формате — тогда наш ``starGift`` не разберётся.

    Если передан ``client``, внутрь добавляется обязательный ``initConnection``
    с полями устройства этой сессии: голый ``invokeWithLayer`` Telegram
    отклоняет с ``400 CONNECTION_LAYER_INVALID`` («Missing InvokeWithLayer-
    InitConnection call»). Без ``client`` собирается «голая» обёртка — так
    полезную нагрузку можно проверить офлайн, без сети.

    Слой запоминается сервером для всей сессии, поэтому после запроса под нашим
    слоем его нужно вернуть (см. ``gifts_logic._restore_session_layer``).
    """
    pass  # TODO: Commercial logic


register_vendor_types()
