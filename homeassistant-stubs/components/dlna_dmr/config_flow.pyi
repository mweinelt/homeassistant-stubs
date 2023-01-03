from .const import CONF_BROWSE_UNFILTERED as CONF_BROWSE_UNFILTERED, CONF_CALLBACK_URL_OVERRIDE as CONF_CALLBACK_URL_OVERRIDE, CONF_LISTEN_PORT as CONF_LISTEN_PORT, CONF_POLL_AVAILABILITY as CONF_POLL_AVAILABILITY, DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN
from .data import get_domain_data as get_domain_data
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Mapping
from homeassistant import config_entries as config_entries
from homeassistant.components import ssdp as ssdp
from homeassistant.const import CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_HOST as CONF_HOST, CONF_TYPE as CONF_TYPE, CONF_URL as CONF_URL
from homeassistant.core import callback as callback
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.exceptions import IntegrationError as IntegrationError
from typing import Any, Optional

LOGGER: Incomplete
FlowInput = Optional[Mapping[str, Any]]

class ConnectError(IntegrationError): ...

class DlnaDmrFlowHandler(config_entries.ConfigFlow):
    VERSION: int
    _discoveries: Incomplete
    _location: Incomplete
    _udn: Incomplete
    _device_type: Incomplete
    _name: Incomplete
    _options: Incomplete
    def __init__(self) -> None: ...
    @staticmethod
    def async_get_options_flow(config_entry: config_entries.ConfigEntry) -> config_entries.OptionsFlow: ...
    async def async_step_user(self, user_input: FlowInput = ...) -> FlowResult: ...
    async def async_step_manual(self, user_input: FlowInput = ...) -> FlowResult: ...
    async def async_step_ssdp(self, discovery_info: ssdp.SsdpServiceInfo) -> FlowResult: ...
    async def async_step_unignore(self, user_input: Mapping[str, Any]) -> FlowResult: ...
    async def async_step_confirm(self, user_input: FlowInput = ...) -> FlowResult: ...
    async def _async_connect(self) -> None: ...
    def _create_entry(self) -> FlowResult: ...
    async def _async_set_info_from_discovery(self, discovery_info: ssdp.SsdpServiceInfo, abort_if_configured: bool = ...) -> None: ...
    async def _async_get_discoveries(self) -> list[ssdp.SsdpServiceInfo]: ...

class DlnaDmrOptionsFlowHandler(config_entries.OptionsFlow):
    config_entry: Incomplete
    def __init__(self, config_entry: config_entries.ConfigEntry) -> None: ...
    async def async_step_init(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...

def _is_ignored_device(discovery_info: ssdp.SsdpServiceInfo) -> bool: ...
