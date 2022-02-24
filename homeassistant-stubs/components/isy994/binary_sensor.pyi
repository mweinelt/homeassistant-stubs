from .const import BINARY_SENSOR_DEVICE_TYPES_ISY as BINARY_SENSOR_DEVICE_TYPES_ISY, BINARY_SENSOR_DEVICE_TYPES_ZWAVE as BINARY_SENSOR_DEVICE_TYPES_ZWAVE, ISY994_NODES as ISY994_NODES, ISY994_PROGRAMS as ISY994_PROGRAMS, SUBNODE_CLIMATE_COOL as SUBNODE_CLIMATE_COOL, SUBNODE_CLIMATE_HEAT as SUBNODE_CLIMATE_HEAT, SUBNODE_DUSK_DAWN as SUBNODE_DUSK_DAWN, SUBNODE_HEARTBEAT as SUBNODE_HEARTBEAT, SUBNODE_LOW_BATTERY as SUBNODE_LOW_BATTERY, SUBNODE_MOTION_DISABLED as SUBNODE_MOTION_DISABLED, SUBNODE_NEGATIVE as SUBNODE_NEGATIVE, SUBNODE_TAMPER as SUBNODE_TAMPER, TYPE_CATEGORY_CLIMATE as TYPE_CATEGORY_CLIMATE, TYPE_INSTEON_MOTION as TYPE_INSTEON_MOTION, _LOGGER as _LOGGER
from .entity import ISYNodeEntity as ISYNodeEntity, ISYProgramEntity as ISYProgramEntity
from .helpers import migrate_old_unique_ids as migrate_old_unique_ids
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.event import async_track_point_in_utc_time as async_track_point_in_utc_time
from pyisy.helpers import NodeProperty as NodeProperty
from pyisy.nodes import Group as Group, Node
from typing import Any

DEVICE_PARENT_REQUIRED: Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
def _detect_device_type_and_class(node: Union[Group, Node]) -> tuple[Union[str, None], Union[str, None]]: ...

class ISYBinarySensorEntity(ISYNodeEntity, BinarySensorEntity):
    _device_class: Any
    def __init__(self, node: Node, force_device_class: Union[str, None] = ..., unknown_state: Union[bool, None] = ...) -> None: ...
    @property
    def is_on(self) -> Union[bool, None]: ...
    @property
    def device_class(self) -> Union[str, None]: ...

class ISYInsteonBinarySensorEntity(ISYBinarySensorEntity):
    _negative_node: Any
    _heartbeat_device: Any
    _computed_state: Any
    _status_was_unknown: bool
    def __init__(self, node: Node, force_device_class: Union[str, None] = ..., unknown_state: Union[bool, None] = ...) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    def add_heartbeat_device(self, entity: Union[ISYBinarySensorHeartbeat, None]) -> None: ...
    def _async_heartbeat(self) -> None: ...
    def add_negative_node(self, child: Node) -> None: ...
    def _async_negative_node_control_handler(self, event: NodeProperty) -> None: ...
    def _async_positive_node_control_handler(self, event: NodeProperty) -> None: ...
    def async_on_update(self, event: NodeProperty) -> None: ...
    @property
    def is_on(self) -> Union[bool, None]: ...

class ISYBinarySensorHeartbeat(ISYNodeEntity, BinarySensorEntity):
    _parent_device: Any
    _heartbeat_timer: Any
    _computed_state: Any
    def __init__(self, node: Node, parent_device: Union[ISYInsteonBinarySensorEntity, ISYBinarySensorEntity, ISYBinarySensorHeartbeat, ISYBinarySensorProgramEntity]) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    def _heartbeat_node_control_handler(self, event: NodeProperty) -> None: ...
    def async_heartbeat(self) -> None: ...
    def _restart_timer(self) -> None: ...
    def async_on_update(self, event: object) -> None: ...
    @property
    def is_on(self) -> bool: ...
    @property
    def device_class(self) -> str: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...

class ISYBinarySensorProgramEntity(ISYProgramEntity, BinarySensorEntity):
    @property
    def is_on(self) -> bool: ...
