import voluptuous as vol
from .const import CONF_LAST_UPDATE_SENSOR_ADD as CONF_LAST_UPDATE_SENSOR_ADD, CONF_SENSOR_INDICES as CONF_SENSOR_INDICES, DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from aiopurpleair import API
from aiopurpleair.endpoints.sensors import NearbySensorResult as NearbySensorResult
from collections.abc import Mapping
from homeassistant import config_entries as config_entries
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_LATITUDE as CONF_LATITUDE, CONF_LONGITUDE as CONF_LONGITUDE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers import aiohttp_client as aiohttp_client, device_registry as dr
from homeassistant.helpers.selector import SelectOptionDict as SelectOptionDict, SelectSelector as SelectSelector, SelectSelectorConfig as SelectSelectorConfig, SelectSelectorMode as SelectSelectorMode
from typing import Any

CONF_DISTANCE: str
CONF_NEARBY_SENSOR_OPTIONS: str
CONF_SENSOR_DEVICE_ID: str
CONF_SENSOR_INDEX: str
DEFAULT_DISTANCE: int
API_KEY_SCHEMA: Incomplete

def async_get_api(hass: HomeAssistant, api_key: str) -> API: ...
def async_get_coordinates_schema(hass: HomeAssistant) -> vol.Schema: ...
def async_get_nearby_sensors_options(nearby_sensor_results: list[NearbySensorResult]) -> list[SelectOptionDict]: ...
def async_get_nearby_sensors_schema(options: list[SelectOptionDict]) -> vol.Schema: ...
def async_get_remove_sensor_options(hass: HomeAssistant, config_entry: ConfigEntry) -> list[SelectOptionDict]: ...
def async_get_remove_sensor_schema(sensors: list[SelectOptionDict]) -> vol.Schema: ...
def async_get_sensor_index(hass: HomeAssistant, config_entry: ConfigEntry, device_entry: dr.DeviceEntry) -> int: ...
def async_remove_sensor_by_device_id(hass: HomeAssistant, config_entry: ConfigEntry, device_id: str, *, remove_device: bool = ...) -> dict[str, Any]: ...

class ValidationResult:
    data: Any
    errors: dict[str, Any]
    def __init__(self, data, errors) -> None: ...

async def async_validate_api_key(hass: HomeAssistant, api_key: str) -> ValidationResult: ...
async def async_validate_coordinates(hass: HomeAssistant, api_key: str, latitude: float, longitude: float, distance: float) -> ValidationResult: ...

class ConfigFlow(config_entries.ConfigFlow):
    VERSION: int
    _flow_data: Incomplete
    _reauth_entry: Incomplete
    def __init__(self) -> None: ...
    @staticmethod
    def async_get_options_flow(config_entry: ConfigEntry) -> PurpleAirOptionsFlowHandler: ...
    async def async_step_by_coordinates(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_choose_sensor(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> FlowResult: ...
    async def async_step_reauth_confirm(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_user(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...

class PurpleAirOptionsFlowHandler(config_entries.OptionsFlow):
    _flow_data: Incomplete
    config_entry: Incomplete
    def __init__(self, config_entry: ConfigEntry) -> None: ...
    async def async_step_add_sensor(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_choose_sensor(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_init(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_remove_sensor(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
