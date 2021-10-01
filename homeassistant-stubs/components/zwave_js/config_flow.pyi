import abc
import voluptuous as vol
from . import disconnect_client as disconnect_client
from .addon import AddonError as AddonError, AddonInfo as AddonInfo, AddonManager as AddonManager, AddonState as AddonState, get_addon_manager as get_addon_manager
from .const import CONF_ADDON_DEVICE as CONF_ADDON_DEVICE, CONF_ADDON_EMULATE_HARDWARE as CONF_ADDON_EMULATE_HARDWARE, CONF_ADDON_LOG_LEVEL as CONF_ADDON_LOG_LEVEL, CONF_ADDON_NETWORK_KEY as CONF_ADDON_NETWORK_KEY, CONF_ADDON_S0_LEGACY_KEY as CONF_ADDON_S0_LEGACY_KEY, CONF_ADDON_S2_ACCESS_CONTROL_KEY as CONF_ADDON_S2_ACCESS_CONTROL_KEY, CONF_ADDON_S2_AUTHENTICATED_KEY as CONF_ADDON_S2_AUTHENTICATED_KEY, CONF_ADDON_S2_UNAUTHENTICATED_KEY as CONF_ADDON_S2_UNAUTHENTICATED_KEY, CONF_INTEGRATION_CREATED_ADDON as CONF_INTEGRATION_CREATED_ADDON, CONF_S0_LEGACY_KEY as CONF_S0_LEGACY_KEY, CONF_S2_ACCESS_CONTROL_KEY as CONF_S2_ACCESS_CONTROL_KEY, CONF_S2_AUTHENTICATED_KEY as CONF_S2_AUTHENTICATED_KEY, CONF_S2_UNAUTHENTICATED_KEY as CONF_S2_UNAUTHENTICATED_KEY, CONF_USB_PATH as CONF_USB_PATH, CONF_USE_ADDON as CONF_USE_ADDON, DOMAIN as DOMAIN
from abc import abstractmethod
from homeassistant import config_entries as config_entries, exceptions as exceptions
from homeassistant.components import usb as usb
from homeassistant.components.hassio import is_hassio as is_hassio
from homeassistant.const import CONF_NAME as CONF_NAME, CONF_URL as CONF_URL
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.data_entry_flow import AbortFlow as AbortFlow, FlowHandler as FlowHandler, FlowManager as FlowManager, FlowResult as FlowResult
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from typing import Any
from zwave_js_server.version import VersionInfo as VersionInfo

_LOGGER: Any
DEFAULT_URL: str
TITLE: str
ADDON_SETUP_TIMEOUT: int
ADDON_SETUP_TIMEOUT_ROUNDS: int
CONF_EMULATE_HARDWARE: str
CONF_LOG_LEVEL: str
SERVER_VERSION_TIMEOUT: int
ADDON_LOG_LEVELS: Any
ADDON_USER_INPUT_MAP: Any
ON_SUPERVISOR_SCHEMA: Any

def get_manual_schema(user_input: dict[str, Any]) -> vol.Schema: ...
def get_on_supervisor_schema(user_input: dict[str, Any]) -> vol.Schema: ...
async def validate_input(hass: HomeAssistant, user_input: dict) -> VersionInfo: ...
async def async_get_version_info(hass: HomeAssistant, ws_address: str) -> VersionInfo: ...

class BaseZwaveJSFlow(FlowHandler, metaclass=abc.ABCMeta):
    s0_legacy_key: Any
    s2_access_control_key: Any
    s2_authenticated_key: Any
    s2_unauthenticated_key: Any
    usb_path: Any
    ws_address: Any
    restart_addon: bool
    integration_created_addon: bool
    install_task: Any
    start_task: Any
    version_info: Any
    def __init__(self) -> None: ...
    @property
    @abstractmethod
    def flow_manager(self) -> FlowManager: ...
    async def async_step_install_addon(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_install_failed(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_start_addon(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_start_failed(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def _async_start_addon(self) -> None: ...
    @abstractmethod
    async def async_step_configure_addon(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    @abstractmethod
    async def async_step_finish_addon_setup(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def _async_get_addon_info(self) -> AddonInfo: ...
    async def _async_set_addon_config(self, config: dict) -> None: ...
    async def _async_install_addon(self) -> None: ...
    async def _async_get_addon_discovery_info(self) -> dict: ...

class ConfigFlow(BaseZwaveJSFlow, config_entries.ConfigFlow):
    VERSION: int
    use_addon: bool
    _title: Any
    def __init__(self) -> None: ...
    @property
    def flow_manager(self) -> config_entries.ConfigEntriesFlowManager: ...
    @staticmethod
    def async_get_options_flow(config_entry: config_entries.ConfigEntry) -> OptionsFlowHandler: ...
    s0_legacy_key: Any
    usb_path: Any
    async def async_step_import(self, data: dict[str, Any]) -> FlowResult: ...
    async def async_step_user(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_usb(self, discovery_info: dict[str, str]) -> FlowResult: ...
    async def async_step_usb_confirm(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    ws_address: Any
    async def async_step_manual(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_hassio(self, discovery_info: dict[str, Any]) -> FlowResult: ...
    async def async_step_hassio_confirm(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    s2_access_control_key: Any
    s2_authenticated_key: Any
    s2_unauthenticated_key: Any
    async def async_step_on_supervisor(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_configure_addon(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    version_info: Any
    async def async_step_finish_addon_setup(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    def _async_create_entry_from_vars(self) -> FlowResult: ...

class OptionsFlowHandler(BaseZwaveJSFlow, config_entries.OptionsFlow):
    config_entry: Any
    original_addon_config: Any
    revert_reason: Any
    def __init__(self, config_entry: config_entries.ConfigEntry) -> None: ...
    @property
    def flow_manager(self) -> config_entries.OptionsFlowManager: ...
    def _async_update_entry(self, data: dict[str, Any]) -> None: ...
    async def async_step_init(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_manual(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_on_supervisor(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    s0_legacy_key: Any
    s2_access_control_key: Any
    s2_authenticated_key: Any
    s2_unauthenticated_key: Any
    usb_path: Any
    restart_addon: bool
    async def async_step_configure_addon(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_start_failed(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    ws_address: Any
    version_info: Any
    async def async_step_finish_addon_setup(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_revert_addon_config(self, reason: str) -> FlowResult: ...

class CannotConnect(exceptions.HomeAssistantError): ...

class InvalidInput(exceptions.HomeAssistantError):
    error: Any
    def __init__(self, error: str) -> None: ...
