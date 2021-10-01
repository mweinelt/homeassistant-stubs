from .const import CONF_DIM_MODE as CONF_DIM_MODE, CONF_SK_NUM_TRIES as CONF_SK_NUM_TRIES, CONNECTION as CONNECTION, DOMAIN as DOMAIN, PLATFORMS as PLATFORMS
from .helpers import DeviceConnectionType as DeviceConnectionType, InputType as InputType, generate_unique_id as generate_unique_id, import_lcn_config as import_lcn_config
from .schemas import CONFIG_SCHEMA as CONFIG_SCHEMA
from .services import SERVICES as SERVICES
from collections.abc import Callable as Callable
from homeassistant import config_entries as config_entries
from homeassistant.const import CONF_IP_ADDRESS as CONF_IP_ADDRESS, CONF_NAME as CONF_NAME, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, CONF_RESOURCE as CONF_RESOURCE, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

_LOGGER: Any

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: config_entries.ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, config_entry: config_entries.ConfigEntry) -> bool: ...

class LcnEntity(Entity):
    config: Any
    entry_id: Any
    device_connection: Any
    _unregister_for_inputs: Any
    _name: Any
    def __init__(self, config: ConfigType, entry_id: str, device_connection: DeviceConnectionType) -> None: ...
    @property
    def unique_id(self) -> str: ...
    @property
    def should_poll(self) -> bool: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    @property
    def name(self) -> str: ...
    def input_received(self, input_obj: InputType) -> None: ...
