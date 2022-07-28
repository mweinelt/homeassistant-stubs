import logging
from . import BluetoothCallbackMatcher as BluetoothCallbackMatcher, BluetoothChange as BluetoothChange, async_register_callback as async_register_callback, async_track_unavailable as async_track_unavailable
from _typeshed import Incomplete
from home_assistant_bluetooth import BluetoothServiceInfo as BluetoothServiceInfo
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, callback as callback

class BasePassiveBluetoothCoordinator:
    hass: Incomplete
    logger: Incomplete
    name: Incomplete
    address: Incomplete
    _cancel_track_unavailable: Incomplete
    _cancel_bluetooth_advertisements: Incomplete
    _present: bool
    last_seen: float
    def __init__(self, hass: HomeAssistant, logger: logging.Logger, address: str) -> None: ...
    def async_start(self) -> CALLBACK_TYPE: ...
    @property
    def available(self) -> bool: ...
    def _async_start(self) -> None: ...
    def _async_stop(self) -> None: ...
    def _async_handle_unavailable(self, address: str) -> None: ...
    def _async_handle_bluetooth_event(self, service_info: BluetoothServiceInfo, change: BluetoothChange) -> None: ...
