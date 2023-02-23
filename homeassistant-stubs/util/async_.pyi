import concurrent.futures
from _typeshed import Incomplete
from asyncio.events import AbstractEventLoop
from collections.abc import Callable as Callable
from typing import Any, TypeVar

_LOGGER: Incomplete
_SHUTDOWN_RUN_CALLBACK_THREADSAFE: str
_T = TypeVar('_T')
_R = TypeVar('_R')
_P: Incomplete

def run_callback_threadsafe(loop: AbstractEventLoop, callback: Callable[..., _T], *args: Any) -> concurrent.futures.Future[_T]: ...
def check_loop(func: Callable[..., Any], strict: bool = ..., advise_msg: Union[str, None] = ...) -> None: ...
def protect_loop(func: Callable[_P, _R], strict: bool = ...) -> Callable[_P, _R]: ...
async def gather_with_concurrency(limit: int, *tasks: Any, return_exceptions: bool = ...) -> Any: ...
def shutdown_run_callback_threadsafe(loop: AbstractEventLoop) -> None: ...
