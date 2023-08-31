from .bluetooth import async_connect_scanner as async_connect_scanner
from .const import ATTR_CHANNEL as ATTR_CHANNEL, ATTR_CLICK_TYPE as ATTR_CLICK_TYPE, ATTR_DEVICE as ATTR_DEVICE, ATTR_GENERATION as ATTR_GENERATION, BATTERY_DEVICES_WITH_PERMANENT_CONNECTION as BATTERY_DEVICES_WITH_PERMANENT_CONNECTION, BLEScannerMode as BLEScannerMode, BLE_MIN_VERSION as BLE_MIN_VERSION, CONF_BLE_SCANNER_MODE as CONF_BLE_SCANNER_MODE, CONF_SLEEP_PERIOD as CONF_SLEEP_PERIOD, DATA_CONFIG_ENTRY as DATA_CONFIG_ENTRY, DOMAIN as DOMAIN, DUAL_MODE_LIGHT_MODELS as DUAL_MODE_LIGHT_MODELS, ENTRY_RELOAD_COOLDOWN as ENTRY_RELOAD_COOLDOWN, EVENT_SHELLY_CLICK as EVENT_SHELLY_CLICK, INPUTS_EVENTS_DICT as INPUTS_EVENTS_DICT, LOGGER as LOGGER, MAX_PUSH_UPDATE_FAILURES as MAX_PUSH_UPDATE_FAILURES, MODELS_SUPPORTING_LIGHT_EFFECTS as MODELS_SUPPORTING_LIGHT_EFFECTS, PUSH_UPDATE_ISSUE_ID as PUSH_UPDATE_ISSUE_ID, REST_SENSORS_UPDATE_INTERVAL as REST_SENSORS_UPDATE_INTERVAL, RPC_INPUTS_EVENTS_TYPES as RPC_INPUTS_EVENTS_TYPES, RPC_RECONNECT_INTERVAL as RPC_RECONNECT_INTERVAL, RPC_SENSORS_POLLING_INTERVAL as RPC_SENSORS_POLLING_INTERVAL, SHBTN_MODELS as SHBTN_MODELS, SLEEP_PERIOD_MULTIPLIER as SLEEP_PERIOD_MULTIPLIER, UPDATE_PERIOD_MULTIPLIER as UPDATE_PERIOD_MULTIPLIER
from .utils import device_update_info as device_update_info, get_rpc_device_wakeup_period as get_rpc_device_wakeup_period
from _typeshed import Incomplete
from aioshelly.block_device import BlockDevice, BlockUpdateType
from aioshelly.rpc_device import RpcDevice, RpcUpdateType
from collections.abc import Callable as Callable
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigEntryState as ConfigEntryState
from homeassistant.const import ATTR_DEVICE_ID as ATTR_DEVICE_ID, CONF_HOST as CONF_HOST, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.debounce import Debouncer as Debouncer
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import Any, Generic, TypeVar

_DeviceT = TypeVar('_DeviceT', bound='BlockDevice|RpcDevice')

class ShellyEntryData:
    block: ShellyBlockCoordinator | None
    device: BlockDevice | RpcDevice | None
    rest: ShellyRestCoordinator | None
    rpc: ShellyRpcCoordinator | None
    rpc_poll: ShellyRpcPollingCoordinator | None
    def __init__(self, block, device, rest, rpc, rpc_poll) -> None: ...

def get_entry_data(hass: HomeAssistant) -> dict[str, ShellyEntryData]: ...

class ShellyCoordinatorBase(DataUpdateCoordinator[None], Generic[_DeviceT]):
    entry: Incomplete
    device: Incomplete
    device_id: Incomplete
    _debounced_reload: Incomplete
    def __init__(self, hass: HomeAssistant, entry: ConfigEntry, device: _DeviceT, update_interval: float) -> None: ...
    @property
    def model(self) -> str: ...
    @property
    def mac(self) -> str: ...
    @property
    def sw_version(self) -> str: ...
    @property
    def sleep_period(self) -> int: ...
    def async_setup(self) -> None: ...
    async def _async_reload_entry(self) -> None: ...

class ShellyBlockCoordinator(ShellyCoordinatorBase[BlockDevice]):
    entry: Incomplete
    _last_cfg_changed: Incomplete
    _last_mode: Incomplete
    _last_effect: Incomplete
    _last_input_events_count: Incomplete
    _last_target_temp: Incomplete
    _push_update_failures: int
    def __init__(self, hass: HomeAssistant, entry: ConfigEntry, device: BlockDevice) -> None: ...
    def _async_device_updates_handler(self) -> None: ...
    async def _async_update_data(self) -> None: ...
    def _async_handle_update(self, device_: BlockDevice, update_type: BlockUpdateType) -> None: ...
    def async_setup(self) -> None: ...
    def shutdown(self) -> None: ...
    def _handle_ha_stop(self, _event: Event) -> None: ...

class ShellyRestCoordinator(ShellyCoordinatorBase[BlockDevice]):
    def __init__(self, hass: HomeAssistant, device: BlockDevice, entry: ConfigEntry) -> None: ...
    async def _async_update_data(self) -> None: ...

class ShellyRpcCoordinator(ShellyCoordinatorBase[RpcDevice]):
    entry: Incomplete
    connected: bool
    _disconnected_callbacks: Incomplete
    _connection_lock: Incomplete
    _event_listeners: Incomplete
    def __init__(self, hass: HomeAssistant, entry: ConfigEntry, device: RpcDevice) -> None: ...
    update_interval: Incomplete
    def update_sleep_period(self) -> bool: ...
    def async_subscribe_events(self, event_callback: Callable[[dict[str, Any]], None]) -> CALLBACK_TYPE: ...
    async def _async_update_listener(self, hass: HomeAssistant, entry: ConfigEntry) -> None: ...
    def _async_device_event_handler(self, event_data: dict[str, Any]) -> None: ...
    async def _async_update_data(self) -> None: ...
    async def _async_disconnected(self) -> None: ...
    def _async_run_disconnected_events(self) -> None: ...
    async def _async_connected(self) -> None: ...
    async def _async_run_connected_events(self) -> None: ...
    async def _async_connect_ble_scanner(self) -> None: ...
    def _async_handle_update(self, device_: RpcDevice, update_type: RpcUpdateType) -> None: ...
    def async_setup(self) -> None: ...
    async def shutdown(self) -> None: ...
    async def _handle_ha_stop(self, _event: Event) -> None: ...

class ShellyRpcPollingCoordinator(ShellyCoordinatorBase[RpcDevice]):
    def __init__(self, hass: HomeAssistant, entry: ConfigEntry, device: RpcDevice) -> None: ...
    async def _async_update_data(self) -> None: ...

def get_block_coordinator_by_device_id(hass: HomeAssistant, device_id: str) -> ShellyBlockCoordinator | None: ...
def get_rpc_coordinator_by_device_id(hass: HomeAssistant, device_id: str) -> ShellyRpcCoordinator | None: ...
async def async_reconnect_soon(hass: HomeAssistant, entry: ConfigEntry) -> None: ...
