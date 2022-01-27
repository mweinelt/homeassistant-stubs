from .dt import as_local as as_local, utcnow as utcnow
from collections.abc import Callable as Callable, Iterable, KeysView
from datetime import timedelta
from typing import Any, TypeVar

T = TypeVar('T')
U = TypeVar('U')
RE_SANITIZE_FILENAME: Any
RE_SANITIZE_PATH: Any

def raise_if_invalid_filename(filename: str) -> None: ...
def raise_if_invalid_path(path: str) -> None: ...
def slugify(text: Union[str, None], *, separator: str = ...) -> str: ...
def repr_helper(inp: Any) -> str: ...
def convert(value: Union[T, None], to_type: Callable[[T], U], default: Union[U, None] = ...) -> Union[U, None]: ...
def ensure_unique_string(preferred_string: str, current_strings: Union[Iterable[str], KeysView[str]]) -> str: ...
def get_random_string(length: int = ...) -> str: ...

class Throttle:
    min_time: Any
    limit_no_throttle: Any
    def __init__(self, min_time: timedelta, limit_no_throttle: Union[timedelta, None] = ...) -> None: ...
    def __call__(self, method: Callable) -> Callable: ...
