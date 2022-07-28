from .const import MESSAGE_RETRIES as MESSAGE_RETRIES, MESSAGE_TIMEOUT as MESSAGE_TIMEOUT, TARGET_ANY as TARGET_ANY, UNAVAILABLE_GRACE as UNAVAILABLE_GRACE, _LOGGER as _LOGGER
from .util import async_execute_lifx as async_execute_lifx, get_real_mac_addr as get_real_mac_addr, lifx_features as lifx_features
from _typeshed import Incomplete
from aiolifx.aiolifx import Light as Light
from aiolifx_connection import LIFXConnection as LIFXConnection
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.debounce import Debouncer as Debouncer
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

REQUEST_REFRESH_DELAY: float

class LIFXUpdateCoordinator(DataUpdateCoordinator):
    connection: Incomplete
    device: Incomplete
    lock: Incomplete
    def __init__(self, hass: HomeAssistant, connection: LIFXConnection, title: str) -> None: ...
    def async_setup(self) -> None: ...
    @property
    def serial_number(self) -> str: ...
    @property
    def mac_address(self) -> str: ...
    async def _async_update_data(self) -> None: ...
    async def async_update_color_zones(self) -> None: ...
    async def async_get_color(self) -> None: ...
    async def async_set_power(self, state: bool, duration: Union[int, None]) -> None: ...
    async def async_set_color(self, hsbk: list[Union[float, int, None]], duration: Union[int, None]) -> None: ...
    async def async_set_color_zones(self, start_index: int, end_index: int, hsbk: list[Union[float, int, None]], duration: Union[int, None], apply: int) -> None: ...
