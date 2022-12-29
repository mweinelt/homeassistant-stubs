import voluptuous as vol
from .addon import get_addon_manager as get_addon_manager
from .const import ADDON_SLUG as ADDON_SLUG, CONF_INTEGRATION_CREATED_ADDON as CONF_INTEGRATION_CREATED_ADDON, CONF_USE_ADDON as CONF_USE_ADDON, DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from homeassistant import config_entries as config_entries
from homeassistant.components.hassio import AddonError as AddonError, AddonInfo as AddonInfo, AddonManager as AddonManager, AddonState as AddonState, HassioServiceInfo as HassioServiceInfo, is_hassio as is_hassio
from homeassistant.const import CONF_URL as CONF_URL
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.data_entry_flow import AbortFlow as AbortFlow, FlowResult as FlowResult
from homeassistant.helpers import aiohttp_client as aiohttp_client
from typing import Any

ADDON_SETUP_TIMEOUT: int
ADDON_SETUP_TIMEOUT_ROUNDS: int
DEFAULT_URL: str
DEFAULT_TITLE: str
ON_SUPERVISOR_SCHEMA: Incomplete

def get_manual_schema(user_input: dict[str, Any]) -> vol.Schema: ...
async def validate_input(hass: HomeAssistant, data: dict[str, Any]) -> None: ...
def build_ws_address(host: str, port: int) -> str: ...

class ConfigFlow(config_entries.ConfigFlow):
    VERSION: int
    ws_address: Incomplete
    integration_created_addon: bool
    install_task: Incomplete
    start_task: Incomplete
    use_addon: bool
    def __init__(self) -> None: ...
    async def async_step_install_addon(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_install_failed(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def _async_install_addon(self) -> None: ...
    async def _async_get_addon_discovery_info(self) -> dict: ...
    async def async_step_start_addon(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_start_failed(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def _async_start_addon(self) -> None: ...
    async def _async_get_addon_info(self) -> AddonInfo: ...
    async def async_step_user(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_manual(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_hassio(self, discovery_info: HassioServiceInfo) -> FlowResult: ...
    async def async_step_hassio_confirm(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_on_supervisor(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_finish_addon_setup(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def _async_create_entry_or_abort(self) -> FlowResult: ...
