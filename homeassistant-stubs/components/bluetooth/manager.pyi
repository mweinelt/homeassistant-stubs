from .advertisement_tracker import AdvertisementTracker as AdvertisementTracker
from .base_scanner import BaseHaScanner as BaseHaScanner
from .const import FALLBACK_MAXIMUM_STALE_ADVERTISEMENT_SECONDS as FALLBACK_MAXIMUM_STALE_ADVERTISEMENT_SECONDS, UNAVAILABLE_TRACK_SECONDS as UNAVAILABLE_TRACK_SECONDS
from .match import ADDRESS as ADDRESS, BluetoothCallbackMatcher as BluetoothCallbackMatcher, BluetoothCallbackMatcherIndex as BluetoothCallbackMatcherIndex, BluetoothCallbackMatcherWithCallback as BluetoothCallbackMatcherWithCallback, CALLBACK as CALLBACK, CONNECTABLE as CONNECTABLE, IntegrationMatcher as IntegrationMatcher, ble_device_matches as ble_device_matches
from .models import BluetoothCallback as BluetoothCallback, BluetoothChange as BluetoothChange, BluetoothServiceInfoBleak as BluetoothServiceInfoBleak
from .usage import install_multiple_bleak_catcher as install_multiple_bleak_catcher, uninstall_multiple_bleak_catcher as uninstall_multiple_bleak_catcher
from .util import async_load_history_from_system as async_load_history_from_system
from _typeshed import Incomplete
from bleak.backends.device import BLEDevice as BLEDevice
from bleak.backends.scanner import AdvertisementData as AdvertisementData, AdvertisementDataCallback as AdvertisementDataCallback
from bluetooth_adapters import AdapterDetails as AdapterDetails, BluetoothAdapters as BluetoothAdapters
from collections.abc import Callable as Callable, Iterable
from datetime import datetime
from homeassistant import config_entries as config_entries
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, Event as Event, HomeAssistant as HomeAssistant
from homeassistant.helpers import discovery_flow as discovery_flow
from homeassistant.helpers.event import async_track_time_interval as async_track_time_interval
from homeassistant.util.dt import monotonic_time_coarse as monotonic_time_coarse
from typing import Any, Final

FILTER_UUIDS: Final[str]
APPLE_MFR_ID: Final[int]
APPLE_IBEACON_START_BYTE: Final[int]
APPLE_HOMEKIT_START_BYTE: Final[int]
APPLE_DEVICE_ID_START_BYTE: Final[int]
APPLE_HOMEKIT_NOTIFY_START_BYTE: Final[int]
APPLE_START_BYTES_WANTED: Final[Incomplete]
MONOTONIC_TIME: Final[Incomplete]
_LOGGER: Incomplete

def _dispatch_bleak_callback(callback: Union[AdvertisementDataCallback, None], filters: dict[str, set[str]], device: BLEDevice, advertisement_data: AdvertisementData) -> None: ...

class BluetoothManager:
    hass: Incomplete
    _integration_matcher: Incomplete
    _cancel_unavailable_tracking: Incomplete
    _advertisement_tracker: Incomplete
    _unavailable_callbacks: Incomplete
    _connectable_unavailable_callbacks: Incomplete
    _callback_index: Incomplete
    _bleak_callbacks: Incomplete
    _all_history: Incomplete
    _connectable_history: Incomplete
    _non_connectable_scanners: Incomplete
    _connectable_scanners: Incomplete
    _adapters: Incomplete
    _sources: Incomplete
    _bluetooth_adapters: Incomplete
    def __init__(self, hass: HomeAssistant, integration_matcher: IntegrationMatcher, bluetooth_adapters: BluetoothAdapters) -> None: ...
    @property
    def supports_passive_scan(self) -> bool: ...
    def async_scanner_count(self, connectable: bool = ...) -> int: ...
    async def async_diagnostics(self) -> dict[str, Any]: ...
    def _find_adapter_by_address(self, address: str) -> Union[str, None]: ...
    def async_scanner_by_source(self, source: str) -> Union[BaseHaScanner, None]: ...
    async def async_get_bluetooth_adapters(self, cached: bool = ...) -> dict[str, AdapterDetails]: ...
    async def async_get_adapter_from_address(self, address: str) -> Union[str, None]: ...
    async def async_setup(self) -> None: ...
    def async_stop(self, event: Event) -> None: ...
    def async_get_discovered_devices_and_advertisement_data_by_address(self, address: str, connectable: bool) -> list[tuple[BLEDevice, AdvertisementData]]: ...
    def _async_all_discovered_addresses(self, connectable: bool) -> Iterable[str]: ...
    def async_discovered_devices(self, connectable: bool) -> list[BLEDevice]: ...
    def async_setup_unavailable_tracking(self) -> None: ...
    def _async_check_unavailable(self, now: datetime) -> None: ...
    def _prefer_previous_adv_from_different_source(self, old: BluetoothServiceInfoBleak, new: BluetoothServiceInfoBleak, debug: bool) -> bool: ...
    def scanner_adv_received(self, service_info: BluetoothServiceInfoBleak) -> None: ...
    def _async_describe_source(self, service_info: BluetoothServiceInfoBleak) -> str: ...
    def async_track_unavailable(self, callback: Callable[[BluetoothServiceInfoBleak], None], address: str, connectable: bool) -> Callable[[], None]: ...
    def async_register_callback(self, callback: BluetoothCallback, matcher: Union[BluetoothCallbackMatcher, None]) -> Callable[[], None]: ...
    def async_ble_device_from_address(self, address: str, connectable: bool) -> Union[BLEDevice, None]: ...
    def async_address_present(self, address: str, connectable: bool) -> bool: ...
    def async_discovered_service_info(self, connectable: bool) -> Iterable[BluetoothServiceInfoBleak]: ...
    def async_last_service_info(self, address: str, connectable: bool) -> Union[BluetoothServiceInfoBleak, None]: ...
    def async_rediscover_address(self, address: str) -> None: ...
    def _get_scanners_by_type(self, connectable: bool) -> list[BaseHaScanner]: ...
    def _get_unavailable_callbacks_by_type(self, connectable: bool) -> dict[str, list[Callable[[BluetoothServiceInfoBleak], None]]]: ...
    def _get_history_by_type(self, connectable: bool) -> dict[str, BluetoothServiceInfoBleak]: ...
    def async_register_scanner(self, scanner: BaseHaScanner, connectable: bool) -> CALLBACK_TYPE: ...
    def async_register_bleak_callback(self, callback: AdvertisementDataCallback, filters: dict[str, set[str]]) -> CALLBACK_TYPE: ...
