from . import GroupEntity as GroupEntity
from .util import attribute_equal as attribute_equal, reduce_attribute as reduce_attribute
from homeassistant.components.cover import ATTR_CURRENT_POSITION as ATTR_CURRENT_POSITION, ATTR_CURRENT_TILT_POSITION as ATTR_CURRENT_TILT_POSITION, ATTR_POSITION as ATTR_POSITION, ATTR_TILT_POSITION as ATTR_TILT_POSITION, CoverEntity as CoverEntity, DOMAIN as DOMAIN, PLATFORM_SCHEMA as PLATFORM_SCHEMA, SUPPORT_CLOSE as SUPPORT_CLOSE, SUPPORT_CLOSE_TILT as SUPPORT_CLOSE_TILT, SUPPORT_OPEN as SUPPORT_OPEN, SUPPORT_OPEN_TILT as SUPPORT_OPEN_TILT, SUPPORT_SET_POSITION as SUPPORT_SET_POSITION, SUPPORT_SET_TILT_POSITION as SUPPORT_SET_TILT_POSITION, SUPPORT_STOP as SUPPORT_STOP, SUPPORT_STOP_TILT as SUPPORT_STOP_TILT
from homeassistant.const import ATTR_ASSUMED_STATE as ATTR_ASSUMED_STATE, ATTR_ENTITY_ID as ATTR_ENTITY_ID, ATTR_SUPPORTED_FEATURES as ATTR_SUPPORTED_FEATURES, CONF_ENTITIES as CONF_ENTITIES, CONF_NAME as CONF_NAME, CONF_UNIQUE_ID as CONF_UNIQUE_ID, SERVICE_CLOSE_COVER as SERVICE_CLOSE_COVER, SERVICE_CLOSE_COVER_TILT as SERVICE_CLOSE_COVER_TILT, SERVICE_OPEN_COVER as SERVICE_OPEN_COVER, SERVICE_OPEN_COVER_TILT as SERVICE_OPEN_COVER_TILT, SERVICE_SET_COVER_POSITION as SERVICE_SET_COVER_POSITION, SERVICE_SET_COVER_TILT_POSITION as SERVICE_SET_COVER_TILT_POSITION, SERVICE_STOP_COVER as SERVICE_STOP_COVER, SERVICE_STOP_COVER_TILT as SERVICE_STOP_COVER_TILT, STATE_CLOSED as STATE_CLOSED, STATE_CLOSING as STATE_CLOSING, STATE_OPEN as STATE_OPEN, STATE_OPENING as STATE_OPENING
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, State as State, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.event import async_track_state_change_event as async_track_state_change_event
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

KEY_OPEN_CLOSE: str
KEY_STOP: str
KEY_POSITION: str
DEFAULT_NAME: str
PARALLEL_UPDATES: int

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: Union[DiscoveryInfoType, None] = ...) -> None: ...

class CoverGroup(GroupEntity, CoverEntity):
    _attr_is_closed: Union[bool, None]
    _attr_is_opening: Union[bool, None]
    _attr_is_closing: Union[bool, None]
    _attr_current_cover_position: Union[int, None]
    _attr_assumed_state: bool
    _entities: Any
    _covers: Any
    _tilts: Any
    _attr_name: Any
    _attr_extra_state_attributes: Any
    _attr_unique_id: Any
    def __init__(self, unique_id: Union[str, None], name: str, entities: list[str]) -> None: ...
    def _update_supported_features_event(self, event: Event) -> None: ...
    def async_update_supported_features(self, entity_id: str, new_state: Union[State, None], update_state: bool = ...) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_open_cover(self, **kwargs: Any) -> None: ...
    async def async_close_cover(self, **kwargs: Any) -> None: ...
    async def async_stop_cover(self, **kwargs: Any) -> None: ...
    async def async_set_cover_position(self, **kwargs: Any) -> None: ...
    async def async_open_cover_tilt(self, **kwargs: Any) -> None: ...
    async def async_close_cover_tilt(self, **kwargs: Any) -> None: ...
    async def async_stop_cover_tilt(self, **kwargs: Any) -> None: ...
    async def async_set_cover_tilt_position(self, **kwargs: Any) -> None: ...
    _attr_current_cover_tilt_position: Any
    _attr_supported_features: Any
    def async_update_group_state(self) -> None: ...
