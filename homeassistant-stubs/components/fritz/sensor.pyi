from .common import AvmWrapper as AvmWrapper, ConnectionInfo as ConnectionInfo, FritzBoxBaseEntity as FritzBoxBaseEntity
from .const import DOMAIN as DOMAIN, DSL_CONNECTION as DSL_CONNECTION, UPTIME_DEVIATION as UPTIME_DEVIATION
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from datetime import datetime
from fritzconnection.lib.fritzstatus import FritzStatus as FritzStatus
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory, SIGNAL_STRENGTH_DECIBELS as SIGNAL_STRENGTH_DECIBELS, UnitOfDataRate as UnitOfDataRate, UnitOfInformation as UnitOfInformation
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.util.dt import utcnow as utcnow
from typing import Any

_LOGGER: Incomplete

def _uptime_calculation(seconds_uptime: float, last_value: Union[datetime, None]) -> datetime: ...
def _retrieve_device_uptime_state(status: FritzStatus, last_value: datetime) -> datetime: ...
def _retrieve_connection_uptime_state(status: FritzStatus, last_value: Union[datetime, None]) -> datetime: ...
def _retrieve_external_ip_state(status: FritzStatus, last_value: str) -> str: ...
def _retrieve_external_ipv6_state(status: FritzStatus, last_value: str) -> str: ...
def _retrieve_kb_s_sent_state(status: FritzStatus, last_value: str) -> float: ...
def _retrieve_kb_s_received_state(status: FritzStatus, last_value: str) -> float: ...
def _retrieve_max_kb_s_sent_state(status: FritzStatus, last_value: str) -> float: ...
def _retrieve_max_kb_s_received_state(status: FritzStatus, last_value: str) -> float: ...
def _retrieve_gb_sent_state(status: FritzStatus, last_value: str) -> float: ...
def _retrieve_gb_received_state(status: FritzStatus, last_value: str) -> float: ...
def _retrieve_link_kb_s_sent_state(status: FritzStatus, last_value: str) -> float: ...
def _retrieve_link_kb_s_received_state(status: FritzStatus, last_value: str) -> float: ...
def _retrieve_link_noise_margin_sent_state(status: FritzStatus, last_value: str) -> float: ...
def _retrieve_link_noise_margin_received_state(status: FritzStatus, last_value: str) -> float: ...
def _retrieve_link_attenuation_sent_state(status: FritzStatus, last_value: str) -> float: ...
def _retrieve_link_attenuation_received_state(status: FritzStatus, last_value: str) -> float: ...

class FritzRequireKeysMixin:
    value_fn: Callable[[FritzStatus, Any], Any]
    def __init__(self, value_fn) -> None: ...

class FritzSensorEntityDescription(SensorEntityDescription, FritzRequireKeysMixin):
    is_suitable: Callable[[ConnectionInfo], bool]
    def __init__(self, value_fn, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, last_reset, native_unit_of_measurement, options, state_class, suggested_display_precision, suggested_unit_of_measurement, is_suitable) -> None: ...

SENSOR_TYPES: tuple[FritzSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class FritzBoxSensor(FritzBoxBaseEntity, SensorEntity):
    entity_description: FritzSensorEntityDescription
    _last_device_value: Incomplete
    _attr_available: bool
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, avm_wrapper: AvmWrapper, device_friendly_name: str, description: FritzSensorEntityDescription) -> None: ...
    _attr_native_value: Incomplete
    def update(self) -> None: ...
