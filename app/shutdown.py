"""Аккуратная остановка фоновых задач при выходе из бота.

Fire-and-forget задачи, которые спят в ``asyncio.sleep`` или ждут сеть, при
закрытии event loop остаются pending. Python печатает для них
``Task was destroyed but it is pending!``, а обработчик asyncio превращает это
в сообщение «Ошибка asyncio». Поэтому перед закрытием loop такие задачи нужно
отменить и дать им завершиться.
"""
from __future__ import annotations

import asyncio
import functools
import logging
from typing import Any, Callable, Iterable

logger = logging.getLogger(__name__)


def quiet_job_cancellation(func: Callable[..., Any]) -> Callable[..., Any]:
    """Прячет отмену job планировщика от логгера APScheduler.

    ``AsyncIOScheduler.shutdown()`` отменяет future запущенной задачи. APScheduler
    3.11 ловит ``CancelledError`` в ``run_coroutine_job`` и пишет его как ошибку
    job вместе с traceback — при остановке бота это лишний шум. Обёртка ловит
    отмену на границе job и завершает его штатно.
    """
    pass  # TODO: Commercial logic


async def cancel_tasks(
    tasks: Iterable[asyncio.Future],
    *,
    label: str,
    timeout: float = 3.0,
) -> int:
    """Отменяет задачи и ждёт их завершения.

    Возвращает количество задач, которые были отменены. Исключения задач
    забираются, чтобы Python не напечатал ``Task exception was never retrieved``
    уже после остановки бота. ``timeout`` защищает выключение от задач, которые
    игнорируют отмену: по истечении таймаута они отменяются повторно.
    """
    pass  # TODO: Commercial logic


def scheduler_tasks(scheduler) -> list[asyncio.Future]:
    """Возвращает задачи, которые уже запущены исполнителями APScheduler.

    ``AsyncIOScheduler.shutdown()`` лишь планирует остановку через
    ``call_soon_threadsafe`` и отменяет future, не дожидаясь их завершения.
    Если loop закроется раньше, asyncio напечатает «Task was destroyed but it is
    pending!». Поэтому забираем ссылки до остановки планировщика, чтобы потом
    отменить и дождаться их сами.
    """
    pass  # TODO: Commercial logic


async def cancel_update_tasks(dp, *, timeout: float = 3.0) -> int:
    """Отменяет handler-задачи aiogram, оставшиеся после остановки polling.

    ``Dispatcher`` хранит их в приватном множестве ``_handle_update_tasks`` и не
    отменяет при остановке. Долгие хендлеры (ответ AI, удаление сообщений,
    рулетка) иначе остаются pending и шумят при закрытии loop.
    """
    pass  # TODO: Commercial logic
