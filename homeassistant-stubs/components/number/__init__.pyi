from .const import ATTR_MAX as ATTR_MAX, ATTR_MIN as ATTR_MIN, ATTR_STEP as ATTR_STEP, ATTR_VALUE as ATTR_VALUE, DEFAULT_MAX_VALUE as DEFAULT_MAX_VALUE, DEFAULT_MIN_VALUE as DEFAULT_MIN_VALUE, DEFAULT_STEP as DEFAULT_STEP, DOMAIN as DOMAIN, NumberDeviceClass as NumberDeviceClass, NumberMode as NumberMode
from collections.abc import Callable
from homeassistant.helpers.config_validation import PLATFORM_SCHEMA as PLATFORM_SCHEMA, PLATFORM_SCHEMA_BASE as PLATFORM_SCHEMA_BASE
from homeassistant.helpers.entity import Entity, EntityDescription
from homeassistant.helpers.restore_state import ExtraStoredData, RestoreEntity
from typing import Any
from typing_extensions import Self

class NumberEntityDescription(EntityDescription):
    device_class: NumberDeviceClass | None
    max_value: None
    min_value: None
    mode: NumberMode | None
    native_max_value: float | None
    native_min_value: float | None
    native_step: float | None
    native_unit_of_measurement: str | None
    step: None
    unit_of_measurement: None
    def __post_init__(self) -> None: ...
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, max_value, min_value, mode, native_max_value, native_min_value, native_step, native_unit_of_measurement, step) -> None: ...

class NumberEntity(Entity):
    entity_description: NumberEntityDescription
    _attr_device_class: NumberDeviceClass | None
    _attr_max_value: None
    _attr_min_value: None
    _attr_mode: NumberMode
    _attr_state: None
    _attr_step: None
    _attr_unit_of_measurement: None
    _attr_value: None
    _attr_native_max_value: float
    _attr_native_min_value: float
    _attr_native_step: float
    _attr_native_unit_of_measurement: str | None
    _attr_native_value: float | None
    _deprecated_number_entity_reported: bool
    _number_option_unit_of_measurement: str | None
    def __init_subclass__(cls, **kwargs: Any) -> None: ...
    async def async_internal_added_to_hass(self) -> None: ...
    @property
    def capability_attributes(self) -> dict[str, Any]: ...
    @property
    def device_class(self) -> NumberDeviceClass | None: ...
    @property
    def native_min_value(self) -> float: ...
    @property
    def min_value(self) -> float: ...
    @property
    def native_max_value(self) -> float: ...
    @property
    def max_value(self) -> float: ...
    @property
    def native_step(self) -> float | None: ...
    @property
    def step(self) -> float: ...
    @property
    def mode(self) -> NumberMode: ...
    @property
    def state(self) -> float | None: ...
    @property
    def native_unit_of_measurement(self) -> str | None: ...
    @property
    def unit_of_measurement(self) -> str | None: ...
    @property
    def native_value(self) -> float | None: ...
    @property
    def value(self) -> float | None: ...
    def set_native_value(self, value: float) -> None: ...
    async def async_set_native_value(self, value: float) -> None: ...
    def set_value(self, value: float) -> None: ...
    async def async_set_value(self, value: float) -> None: ...
    def _convert_to_state_value(self, value: float, method: Callable[[float, int], float]) -> float: ...
    def convert_to_native_value(self, value: float) -> float: ...
    def _report_deprecated_number_entity(self) -> None: ...
    def async_registry_entry_updated(self) -> None: ...

class NumberExtraStoredData(ExtraStoredData):
    native_max_value: float | None
    native_min_value: float | None
    native_step: float | None
    native_unit_of_measurement: str | None
    native_value: float | None
    def as_dict(self) -> dict[str, Any]: ...
    @classmethod
    def from_dict(cls, restored: dict[str, Any]) -> Self | None: ...
    def __init__(self, native_max_value, native_min_value, native_step, native_unit_of_measurement, native_value) -> None: ...

class RestoreNumber(NumberEntity, RestoreEntity):
    @property
    def extra_restore_state_data(self) -> NumberExtraStoredData: ...
    async def async_get_last_number_data(self) -> NumberExtraStoredData | None: ...
