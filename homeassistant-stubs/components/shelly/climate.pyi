from . import BlockDeviceWrapper as BlockDeviceWrapper
from .const import AIOSHELLY_DEVICE_TIMEOUT_SEC as AIOSHELLY_DEVICE_TIMEOUT_SEC, BLOCK as BLOCK, DATA_CONFIG_ENTRY as DATA_CONFIG_ENTRY, DOMAIN as DOMAIN, SHTRV_01_TEMPERATURE_SETTINGS as SHTRV_01_TEMPERATURE_SETTINGS
from .utils import get_device_entry_gen as get_device_entry_gen
from aioshelly.block_device import Block as Block
from homeassistant.components.climate import ClimateEntity as ClimateEntity
from homeassistant.components.climate.const import CURRENT_HVAC_HEAT as CURRENT_HVAC_HEAT, CURRENT_HVAC_IDLE as CURRENT_HVAC_IDLE, CURRENT_HVAC_OFF as CURRENT_HVAC_OFF, HVAC_MODE_HEAT as HVAC_MODE_HEAT, HVAC_MODE_OFF as HVAC_MODE_OFF, PRESET_NONE as PRESET_NONE, SUPPORT_PRESET_MODE as SUPPORT_PRESET_MODE, SUPPORT_TARGET_TEMPERATURE as SUPPORT_TARGET_TEMPERATURE
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, TEMP_CELSIUS as TEMP_CELSIUS
from homeassistant.core import HomeAssistant as HomeAssistant, State as State, callback as callback
from homeassistant.helpers import device_registry as device_registry, entity_registry as entity_registry, update_coordinator as update_coordinator
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from typing import Any, Final

_LOGGER: Final[Any]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
async def async_setup_climate_entities(async_add_entities: AddEntitiesCallback, wrapper: BlockDeviceWrapper) -> None: ...
async def async_restore_climate_entities(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback, wrapper: BlockDeviceWrapper) -> None: ...

class BlockSleepingClimate(update_coordinator.CoordinatorEntity, RestoreEntity, ClimateEntity):
    _attr_hvac_modes: Any
    _attr_icon: str
    _attr_max_temp: Any
    _attr_min_temp: Any
    _attr_supported_features: int
    _attr_target_temperature_step: Any
    _attr_temperature_unit: Any
    wrapper: Any
    block: Any
    control_result: Any
    device_block: Any
    last_state: Any
    last_state_attributes: Any
    _preset_modes: Any
    _unique_id: Any
    _channel: Any
    def __init__(self, wrapper: BlockDeviceWrapper, sensor_block: Union[Block, None], device_block: Union[Block, None], entry: Union[entity_registry.RegistryEntry, None] = ...) -> None: ...
    @property
    def unique_id(self) -> str: ...
    @property
    def name(self) -> str: ...
    @property
    def target_temperature(self) -> Union[float, None]: ...
    @property
    def current_temperature(self) -> Union[float, None]: ...
    @property
    def available(self) -> bool: ...
    @property
    def hvac_mode(self) -> str: ...
    @property
    def preset_mode(self) -> Union[str, None]: ...
    @property
    def hvac_action(self) -> Union[str, None]: ...
    @property
    def preset_modes(self) -> list[str]: ...
    @property
    def device_info(self) -> DeviceInfo: ...
    def _check_is_off(self) -> bool: ...
    async def set_state_full_path(self, **kwargs: Any) -> Any: ...
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    async def async_set_hvac_mode(self, hvac_mode: str) -> None: ...
    async def async_set_preset_mode(self, preset_mode: str) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    def _handle_coordinator_update(self) -> None: ...
