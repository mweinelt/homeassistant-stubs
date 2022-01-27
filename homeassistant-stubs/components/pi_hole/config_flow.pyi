from .const import CONF_LOCATION as CONF_LOCATION, CONF_STATISTICS_ONLY as CONF_STATISTICS_ONLY, DEFAULT_LOCATION as DEFAULT_LOCATION, DEFAULT_NAME as DEFAULT_NAME, DEFAULT_SSL as DEFAULT_SSL, DEFAULT_STATISTICS_ONLY as DEFAULT_STATISTICS_ONLY, DEFAULT_VERIFY_SSL as DEFAULT_VERIFY_SSL, DOMAIN as DOMAIN
from homeassistant import config_entries as config_entries
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_HOST as CONF_HOST, CONF_NAME as CONF_NAME, CONF_PORT as CONF_PORT, CONF_SSL as CONF_SSL, CONF_VERIFY_SSL as CONF_VERIFY_SSL
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from typing import Any

_LOGGER: Any

class PiHoleFlowHandler(config_entries.ConfigFlow):
    VERSION: int
    _config: Any
    def __init__(self) -> None: ...
    async def async_step_user(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_import(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_init(self, user_input: Union[dict[str, Any], None], is_import: bool = ...) -> FlowResult: ...
    async def async_step_api_key(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def _async_endpoint_existed(self, endpoint: str) -> bool: ...
    async def _async_try_connect(self, host: str, location: str, tls: bool, verify_tls: bool) -> None: ...
