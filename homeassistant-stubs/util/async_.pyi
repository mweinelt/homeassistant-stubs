import concurrent.futures
from asyncio.events import AbstractEventLoop
from collections.abc import Callable as Callable, Coroutine
from typing import Any, TypeVar

_LOGGER: Any
_SHUTDOWN_RUN_CALLBACK_THREADSAFE: str
T = TypeVar('T')

def fire_coroutine_threadsafe(coro: Coroutine, loop: AbstractEventLoop) -> None: ...
def run_callback_threadsafe(loop: AbstractEventLoop, callback: Callable[..., T], *args: Any) -> concurrent.futures.Future[T]: ...
def check_loop() -> None: ...
def protect_loop(func: Callable) -> Callable: ...
async def gather_with_concurrency(limit: int, *tasks: Any, return_exceptions: bool = ...) -> Any: ...
def shutdown_run_callback_threadsafe(loop: AbstractEventLoop) -> None: ...
