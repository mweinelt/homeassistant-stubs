from .const import DOMAIN as DOMAIN, WEMO_SUBSCRIPTION_EVENT as WEMO_SUBSCRIPTION_EVENT
from .models import async_wemo_data as async_wemo_data
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_CONFIGURATION_URL as ATTR_CONFIGURATION_URL, ATTR_IDENTIFIERS as ATTR_IDENTIFIERS, CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_NAME as CONF_NAME, CONF_PARAMS as CONF_PARAMS, CONF_TYPE as CONF_TYPE, CONF_UNIQUE_ID as CONF_UNIQUE_ID
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import CONNECTION_UPNP as CONNECTION_UPNP, DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from pywemo import WeMoDevice as WeMoDevice
from pywemo.subscribe import SubscriptionRegistry as SubscriptionRegistry

_LOGGER: Incomplete
ErrorStringKey: Incomplete
OptionsFieldKey: Incomplete

class OptionsValidationError(Exception):
    field_key: Incomplete
    error_key: Incomplete
    def __init__(self, field_key: OptionsFieldKey, error_key: ErrorStringKey, message: str) -> None: ...

class Options:
    enable_subscription: bool
    enable_long_press: bool
    def __post_init__(self) -> None: ...
    def __init__(self, enable_subscription, enable_long_press) -> None: ...

class DeviceCoordinator(DataUpdateCoordinator[None]):
    options: Options | None
    hass: Incomplete
    wemo: Incomplete
    device_id: Incomplete
    device_info: Incomplete
    supports_long_press: Incomplete
    update_lock: Incomplete
    def __init__(self, hass: HomeAssistant, wemo: WeMoDevice, device_id: str) -> None: ...
    def subscription_callback(self, _device: WeMoDevice, event_type: str, params: str) -> None: ...
    async def async_shutdown(self) -> None: ...
    async def _async_set_enable_subscription(self, enable_subscription: bool) -> None: ...
    async def _async_set_enable_long_press(self, enable_long_press: bool) -> None: ...
    async def async_set_options(self, hass: HomeAssistant, config_entry: ConfigEntry) -> None: ...
    last_exception: Incomplete
    last_update_success: bool
    async def _async_subscription_callback(self, updated: bool) -> None: ...
    @property
    def should_poll(self) -> bool: ...
    async def _async_update_data(self) -> None: ...
    async def _async_locked_update(self, force_update: bool) -> None: ...

def _create_device_info(wemo: WeMoDevice) -> DeviceInfo: ...
def _device_info(wemo: WeMoDevice) -> DeviceInfo: ...
async def async_register_device(hass: HomeAssistant, config_entry: ConfigEntry, wemo: WeMoDevice) -> DeviceCoordinator: ...
def async_get_coordinator(hass: HomeAssistant, device_id: str) -> DeviceCoordinator: ...
def _async_coordinators(hass: HomeAssistant) -> dict[str, DeviceCoordinator]: ...
def _async_registry(hass: HomeAssistant) -> SubscriptionRegistry: ...
