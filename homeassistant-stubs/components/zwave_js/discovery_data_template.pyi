from .const import ENTITY_DESC_KEY_BATTERY as ENTITY_DESC_KEY_BATTERY, ENTITY_DESC_KEY_CO as ENTITY_DESC_KEY_CO, ENTITY_DESC_KEY_CO2 as ENTITY_DESC_KEY_CO2, ENTITY_DESC_KEY_CURRENT as ENTITY_DESC_KEY_CURRENT, ENTITY_DESC_KEY_ENERGY_MEASUREMENT as ENTITY_DESC_KEY_ENERGY_MEASUREMENT, ENTITY_DESC_KEY_ENERGY_TOTAL_INCREASING as ENTITY_DESC_KEY_ENERGY_TOTAL_INCREASING, ENTITY_DESC_KEY_HUMIDITY as ENTITY_DESC_KEY_HUMIDITY, ENTITY_DESC_KEY_ILLUMINANCE as ENTITY_DESC_KEY_ILLUMINANCE, ENTITY_DESC_KEY_MEASUREMENT as ENTITY_DESC_KEY_MEASUREMENT, ENTITY_DESC_KEY_POWER as ENTITY_DESC_KEY_POWER, ENTITY_DESC_KEY_POWER_FACTOR as ENTITY_DESC_KEY_POWER_FACTOR, ENTITY_DESC_KEY_PRESSURE as ENTITY_DESC_KEY_PRESSURE, ENTITY_DESC_KEY_SIGNAL_STRENGTH as ENTITY_DESC_KEY_SIGNAL_STRENGTH, ENTITY_DESC_KEY_TARGET_TEMPERATURE as ENTITY_DESC_KEY_TARGET_TEMPERATURE, ENTITY_DESC_KEY_TEMPERATURE as ENTITY_DESC_KEY_TEMPERATURE, ENTITY_DESC_KEY_TOTAL_INCREASING as ENTITY_DESC_KEY_TOTAL_INCREASING, ENTITY_DESC_KEY_VOLTAGE as ENTITY_DESC_KEY_VOLTAGE
from collections.abc import Iterable
from homeassistant.const import CONCENTRATION_MICROGRAMS_PER_CUBIC_METER as CONCENTRATION_MICROGRAMS_PER_CUBIC_METER, CONCENTRATION_PARTS_PER_MILLION as CONCENTRATION_PARTS_PER_MILLION, DEGREE as DEGREE, ELECTRIC_CURRENT_AMPERE as ELECTRIC_CURRENT_AMPERE, ELECTRIC_CURRENT_MILLIAMPERE as ELECTRIC_CURRENT_MILLIAMPERE, ELECTRIC_POTENTIAL_MILLIVOLT as ELECTRIC_POTENTIAL_MILLIVOLT, ELECTRIC_POTENTIAL_VOLT as ELECTRIC_POTENTIAL_VOLT, ENERGY_KILO_WATT_HOUR as ENERGY_KILO_WATT_HOUR, FREQUENCY_HERTZ as FREQUENCY_HERTZ, FREQUENCY_KILOHERTZ as FREQUENCY_KILOHERTZ, IRRADIATION_WATTS_PER_SQUARE_METER as IRRADIATION_WATTS_PER_SQUARE_METER, LENGTH_CENTIMETERS as LENGTH_CENTIMETERS, LENGTH_FEET as LENGTH_FEET, LENGTH_METERS as LENGTH_METERS, LIGHT_LUX as LIGHT_LUX, MASS_KILOGRAMS as MASS_KILOGRAMS, MASS_POUNDS as MASS_POUNDS, PERCENTAGE as PERCENTAGE, POWER_BTU_PER_HOUR as POWER_BTU_PER_HOUR, POWER_WATT as POWER_WATT, PRECIPITATION_INCHES_PER_HOUR as PRECIPITATION_INCHES_PER_HOUR, PRECIPITATION_MILLIMETERS_PER_HOUR as PRECIPITATION_MILLIMETERS_PER_HOUR, PRESSURE_INHG as PRESSURE_INHG, PRESSURE_MMHG as PRESSURE_MMHG, PRESSURE_PSI as PRESSURE_PSI, SIGNAL_STRENGTH_DECIBELS as SIGNAL_STRENGTH_DECIBELS, SIGNAL_STRENGTH_DECIBELS_MILLIWATT as SIGNAL_STRENGTH_DECIBELS_MILLIWATT, SPEED_METERS_PER_SECOND as SPEED_METERS_PER_SECOND, SPEED_MILES_PER_HOUR as SPEED_MILES_PER_HOUR, TEMP_CELSIUS as TEMP_CELSIUS, TEMP_FAHRENHEIT as TEMP_FAHRENHEIT, TIME_SECONDS as TIME_SECONDS, VOLUME_CUBIC_FEET as VOLUME_CUBIC_FEET, VOLUME_CUBIC_METERS as VOLUME_CUBIC_METERS, VOLUME_FLOW_RATE_CUBIC_FEET_PER_MINUTE as VOLUME_FLOW_RATE_CUBIC_FEET_PER_MINUTE, VOLUME_FLOW_RATE_CUBIC_METERS_PER_HOUR as VOLUME_FLOW_RATE_CUBIC_METERS_PER_HOUR, VOLUME_GALLONS as VOLUME_GALLONS, VOLUME_LITERS as VOLUME_LITERS
from typing import Any
from zwave_js_server.const.command_class.meter import MeterScaleType as MeterScaleType
from zwave_js_server.const.command_class.multilevel_sensor import MultilevelSensorScaleType as MultilevelSensorScaleType, MultilevelSensorType
from zwave_js_server.model.node import Node as ZwaveNode
from zwave_js_server.model.value import ConfigurationValue as ZwaveConfigurationValue, Value as ZwaveValue

METER_DEVICE_CLASS_MAP: dict[str, set[MeterScaleType]]
MULTILEVEL_SENSOR_DEVICE_CLASS_MAP: dict[str, set[MultilevelSensorType]]
METER_UNIT_MAP: dict[str, set[MeterScaleType]]
MULTILEVEL_SENSOR_UNIT_MAP: dict[str, set[MultilevelSensorScaleType]]
_LOGGER: Any

class ZwaveValueID:
    property_: Union[str, int]
    command_class: int
    endpoint: Union[int, None]
    property_key: Union[str, int, None]
    def __init__(self, property_, command_class, endpoint, property_key) -> None: ...

class BaseDiscoverySchemaDataTemplate:
    static_data: Union[Any, None]
    def resolve_data(self, value: ZwaveValue) -> Any: ...
    def values_to_watch(self, resolved_data: Any) -> Iterable[ZwaveValue]: ...
    def value_ids_to_watch(self, resolved_data: Any) -> set[str]: ...
    @staticmethod
    def _get_value_from_id(node: ZwaveNode, value_id_obj: ZwaveValueID) -> Union[ZwaveValue, None]: ...
    def __init__(self, static_data) -> None: ...

class DynamicCurrentTempClimateDataTemplate(BaseDiscoverySchemaDataTemplate):
    lookup_table: dict[Union[str, int], ZwaveValueID]
    dependent_value: Union[ZwaveValueID, None]
    def resolve_data(self, value: ZwaveValue) -> dict[str, Any]: ...
    def values_to_watch(self, resolved_data: dict[str, Any]) -> Iterable[ZwaveValue]: ...
    @staticmethod
    def current_temperature_value(resolved_data: dict[str, Any]) -> Union[ZwaveValue, None]: ...
    def __init__(self, static_data, lookup_table, dependent_value) -> None: ...

class NumericSensorDataTemplateData:
    entity_description_key: Union[str, None]
    unit_of_measurement: Union[str, None]
    def __init__(self, entity_description_key, unit_of_measurement) -> None: ...

class NumericSensorDataTemplate(BaseDiscoverySchemaDataTemplate):
    @staticmethod
    def find_key_from_matching_set(enum_value: Union[MultilevelSensorType, MultilevelSensorScaleType, MeterScaleType], set_map: dict[str, set[Union[MultilevelSensorType, MultilevelSensorScaleType, MeterScaleType]]]) -> Union[str, None]: ...
    def resolve_data(self, value: ZwaveValue) -> NumericSensorDataTemplateData: ...

class TiltValueMix:
    tilt_value_id: ZwaveValueID
    def __init__(self, tilt_value_id) -> None: ...

class CoverTiltDataTemplate(BaseDiscoverySchemaDataTemplate, TiltValueMix):
    def resolve_data(self, value: ZwaveValue) -> dict[str, Any]: ...
    def values_to_watch(self, resolved_data: dict[str, Any]) -> Iterable[ZwaveValue]: ...
    @staticmethod
    def current_tilt_value(resolved_data: dict[str, Any]) -> Union[ZwaveValue, None]: ...
    def __init__(self, tilt_value_id, static_data) -> None: ...

class FanSpeedDataTemplate:
    def get_speed_config(self, resolved_data: dict[str, Any]) -> Union[list[int], None]: ...

class ConfigurableFanSpeedValueMix:
    configuration_option: ZwaveValueID
    configuration_value_to_speeds: dict[int, list[int]]
    def __post_init__(self) -> None: ...
    def __init__(self, configuration_option, configuration_value_to_speeds) -> None: ...

class ConfigurableFanSpeedDataTemplate(BaseDiscoverySchemaDataTemplate, FanSpeedDataTemplate, ConfigurableFanSpeedValueMix):
    def resolve_data(self, value: ZwaveValue) -> dict[str, ZwaveConfigurationValue]: ...
    def values_to_watch(self, resolved_data: dict[str, Any]) -> Iterable[ZwaveValue]: ...
    def get_speed_config(self, resolved_data: dict[str, ZwaveConfigurationValue]) -> Union[list[int], None]: ...
    def __init__(self, configuration_option, configuration_value_to_speeds, static_data) -> None: ...

class FixedFanSpeedValueMix:
    speeds: list[int]
    def __post_init__(self) -> None: ...
    def __init__(self, speeds) -> None: ...

class FixedFanSpeedDataTemplate(BaseDiscoverySchemaDataTemplate, FanSpeedDataTemplate, FixedFanSpeedValueMix):
    def get_speed_config(self, resolved_data: dict[str, ZwaveConfigurationValue]) -> list[int]: ...
    def __init__(self, speeds, static_data) -> None: ...
