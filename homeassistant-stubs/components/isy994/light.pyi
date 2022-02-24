from .const import CONF_RESTORE_LIGHT_STATE as CONF_RESTORE_LIGHT_STATE, ISY994_NODES as ISY994_NODES, UOM_PERCENTAGE as UOM_PERCENTAGE, _LOGGER as _LOGGER
from .entity import ISYNodeEntity as ISYNodeEntity
from .helpers import migrate_old_unique_ids as migrate_old_unique_ids
from .services import async_setup_light_services as async_setup_light_services
from homeassistant.components.light import LightEntity as LightEntity, SUPPORT_BRIGHTNESS as SUPPORT_BRIGHTNESS
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from pyisy.helpers import NodeProperty as NodeProperty
from pyisy.nodes import Node as Node
from typing import Any

ATTR_LAST_BRIGHTNESS: str

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ISYLightEntity(ISYNodeEntity, LightEntity, RestoreEntity):
    _last_brightness: Any
    _restore_light_state: Any
    def __init__(self, node: Node, restore_light_state: bool) -> None: ...
    @property
    def is_on(self) -> bool: ...
    @property
    def brightness(self) -> Union[int, None]: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    def async_on_update(self, event: NodeProperty) -> None: ...
    async def async_turn_on(self, brightness: Union[int, None] = ..., **kwargs: Any) -> None: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
    @property
    def supported_features(self) -> int: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_set_on_level(self, value: int) -> None: ...
    async def async_set_ramp_rate(self, value: int) -> None: ...
