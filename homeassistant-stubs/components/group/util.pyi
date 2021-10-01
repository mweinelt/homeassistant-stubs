from collections.abc import Callable as Callable, Iterator
from homeassistant.core import State as State
from typing import Any

def find_state_attributes(states: list[State], key: str) -> Iterator[Any]: ...
def mean_int(*args: Any) -> int: ...
def mean_tuple(*args: Any) -> tuple[Union[float, Any], ...]: ...
def attribute_equal(states: list[State], key: str) -> bool: ...
def reduce_attribute(states: list[State], key: str, default: Union[Any, None] = ..., reduce: Callable[..., Any] = ...) -> Any: ...
