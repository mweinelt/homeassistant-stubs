from .const import BLEScannerMode as BLEScannerMode, BLE_MIN_VERSION as BLE_MIN_VERSION, CONF_BLE_SCANNER_MODE as CONF_BLE_SCANNER_MODE, CONF_SLEEP_PERIOD as CONF_SLEEP_PERIOD, DOMAIN as DOMAIN, LOGGER as LOGGER
from .coordinator import async_reconnect_soon as async_reconnect_soon, get_entry_data as get_entry_data
from .utils import get_block_device_sleep_period as get_block_device_sleep_period, get_coap_context as get_coap_context, get_info_auth as get_info_auth, get_info_gen as get_info_gen, get_model_name as get_model_name, get_rpc_device_sleep_period as get_rpc_device_sleep_period, get_ws_context as get_ws_context, mac_address_from_name as mac_address_from_name
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.components.zeroconf import ZeroconfServiceInfo as ZeroconfServiceInfo
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, OptionsFlow as OptionsFlow
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.selector import SelectSelector as SelectSelector, SelectSelectorConfig as SelectSelectorConfig
from typing import Any, Final

HOST_SCHEMA: Final[Incomplete]
BLE_SCANNER_OPTIONS: Incomplete
INTERNAL_WIFI_AP_IP: str

async def validate_input(hass: HomeAssistant, host: str, info: dict[str, Any], data: dict[str, Any]) -> dict[str, Any]: ...

class ShellyConfigFlow(ConfigFlow):
    VERSION: int
    host: str
    info: dict[str, Any]
    device_info: dict[str, Any]
    entry: Union[ConfigEntry, None]
    async def async_step_user(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_credentials(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def _async_discovered_mac(self, mac: str, host: str) -> None: ...
    async def async_step_zeroconf(self, discovery_info: ZeroconfServiceInfo) -> FlowResult: ...
    async def async_step_confirm_discovery(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> FlowResult: ...
    async def async_step_reauth_confirm(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def _async_get_info(self, host: str) -> dict[str, Any]: ...
    @staticmethod
    def async_get_options_flow(config_entry: ConfigEntry) -> OptionsFlowHandler: ...
    @classmethod
    def async_supports_options_flow(cls, config_entry: ConfigEntry) -> bool: ...

class OptionsFlowHandler(OptionsFlow):
    config_entry: Incomplete
    def __init__(self, config_entry: ConfigEntry) -> None: ...
    async def async_step_init(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
