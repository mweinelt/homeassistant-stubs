from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import CONCENTRATION_MICROGRAMS_PER_CUBIC_METER as CONCENTRATION_MICROGRAMS_PER_CUBIC_METER, CONCENTRATION_PARTS_PER_MILLION as CONCENTRATION_PARTS_PER_MILLION, PERCENTAGE as PERCENTAGE, PRESSURE_HPA as PRESSURE_HPA, SIGNAL_STRENGTH_DECIBELS_MILLIWATT as SIGNAL_STRENGTH_DECIBELS_MILLIWATT, TEMP_CELSIUS as TEMP_CELSIUS
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from typing import Any, Final

SUFFIX_P0: Final[str]
SUFFIX_P1: Final[str]
SUFFIX_P2: Final[str]
SUFFIX_P4: Final[str]
ATTR_BME280_HUMIDITY: Final[str]
ATTR_BME280_PRESSURE: Final[str]
ATTR_BME280_TEMPERATURE: Final[str]
ATTR_BMP180_PRESSURE: Final[str]
ATTR_BMP180_TEMPERATURE: Final[str]
ATTR_BMP280_PRESSURE: Final[str]
ATTR_BMP280_TEMPERATURE: Final[str]
ATTR_DHT22_HUMIDITY: Final[str]
ATTR_DHT22_TEMPERATURE: Final[str]
ATTR_HECA_HUMIDITY: Final[str]
ATTR_HECA_TEMPERATURE: Final[str]
ATTR_MHZ14A_CARBON_DIOXIDE: Final[str]
ATTR_SDS011: Final[str]
ATTR_SDS011_P1: Final[Any]
ATTR_SDS011_P2: Final[Any]
ATTR_SHT3X_HUMIDITY: Final[str]
ATTR_SHT3X_TEMPERATURE: Final[str]
ATTR_SIGNAL_STRENGTH: Final[str]
ATTR_SPS30: Final[str]
ATTR_SPS30_P0: Final[Any]
ATTR_SPS30_P1: Final[Any]
ATTR_SPS30_P2: Final[Any]
ATTR_SPS30_P4: Final[Any]
ATTR_UPTIME: Final[str]
DEFAULT_NAME: Final[str]
DEFAULT_UPDATE_INTERVAL: Final[Any]
DOMAIN: Final[str]
MANUFACTURER: Final[str]
MIGRATION_SENSORS: Final[Any]
SENSORS: Final[tuple[SensorEntityDescription, ...]]
