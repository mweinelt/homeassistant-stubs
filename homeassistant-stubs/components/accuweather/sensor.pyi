from . import AccuWeatherDataUpdateCoordinator as AccuWeatherDataUpdateCoordinator
from .const import API_IMPERIAL as API_IMPERIAL, API_METRIC as API_METRIC, ATTRIBUTION as ATTRIBUTION, ATTR_FORECAST as ATTR_FORECAST, DOMAIN as DOMAIN, MAX_FORECAST_DAYS as MAX_FORECAST_DAYS
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONCENTRATION_PARTS_PER_CUBIC_METER as CONCENTRATION_PARTS_PER_CUBIC_METER, LENGTH_FEET as LENGTH_FEET, LENGTH_INCHES as LENGTH_INCHES, LENGTH_METERS as LENGTH_METERS, LENGTH_MILLIMETERS as LENGTH_MILLIMETERS, PERCENTAGE as PERCENTAGE, SPEED_KILOMETERS_PER_HOUR as SPEED_KILOMETERS_PER_HOUR, SPEED_MILES_PER_HOUR as SPEED_MILES_PER_HOUR, TEMP_CELSIUS as TEMP_CELSIUS, TEMP_FAHRENHEIT as TEMP_FAHRENHEIT, TIME_HOURS as TIME_HOURS, UV_INDEX as UV_INDEX
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

PARALLEL_UPDATES: int

class AccuWeatherSensorDescription(SensorEntityDescription):
    unit_metric: Union[str, None]
    unit_imperial: Union[str, None]
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, unit_of_measurement, last_reset, native_unit_of_measurement, state_class, unit_metric, unit_imperial) -> None: ...

FORECAST_SENSOR_TYPES: tuple[AccuWeatherSensorDescription, ...]
SENSOR_TYPES: tuple[AccuWeatherSensorDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AccuWeatherSensor(CoordinatorEntity[AccuWeatherDataUpdateCoordinator], SensorEntity):
    _attr_attribution: Incomplete
    _attr_has_entity_name: bool
    entity_description: AccuWeatherSensorDescription
    _sensor_data: Incomplete
    _attrs: Incomplete
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    _unit_system: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    _attr_device_info: Incomplete
    forecast_day: Incomplete
    def __init__(self, coordinator: AccuWeatherDataUpdateCoordinator, description: AccuWeatherSensorDescription, forecast_day: Union[int, None] = ...) -> None: ...
    @property
    def native_value(self) -> StateType: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
    def _handle_coordinator_update(self) -> None: ...

def _get_sensor_data(sensors: dict[str, Any], forecast_day: Union[int, None], kind: str) -> Any: ...
