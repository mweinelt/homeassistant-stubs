from .const import BPUP_SUBS as BPUP_SUBS, DOMAIN as DOMAIN, HUB as HUB
from .entity import BondEntity as BondEntity
from .utils import BondDevice as BondDevice, BondHub as BondHub
from _typeshed import Incomplete
from bond_async import BPUPSubscriptions as BPUPSubscriptions
from homeassistant.components.cover import ATTR_POSITION as ATTR_POSITION, CoverDeviceClass as CoverDeviceClass, CoverEntity as CoverEntity, CoverEntityFeature as CoverEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

def _bond_to_hass_position(bond_position: int) -> int: ...
def _hass_to_bond_position(hass_position: int) -> int: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class BondCover(BondEntity, CoverEntity):
    _attr_device_class: Incomplete
    _attr_supported_features: Incomplete
    def __init__(self, hub: BondHub, device: BondDevice, bpup_subs: BPUPSubscriptions) -> None: ...
    _attr_is_closed: Incomplete
    _attr_current_cover_position: Incomplete
    def _apply_state(self, state: dict) -> None: ...
    async def async_set_cover_position(self, **kwargs: Any) -> None: ...
    async def async_open_cover(self, **kwargs: Any) -> None: ...
    async def async_close_cover(self, **kwargs: Any) -> None: ...
    async def async_stop_cover(self, **kwargs: Any) -> None: ...
    async def async_open_cover_tilt(self, **kwargs: Any) -> None: ...
    async def async_close_cover_tilt(self, **kwargs: Any) -> None: ...
    async def async_stop_cover_tilt(self, **kwargs: Any) -> None: ...
