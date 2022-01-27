from . import HuaweiLteBaseEntityWithDevice as HuaweiLteBaseEntityWithDevice
from .const import DOMAIN as DOMAIN, KEY_DIALUP_MOBILE_DATASWITCH as KEY_DIALUP_MOBILE_DATASWITCH
from homeassistant.components.switch import SwitchDeviceClass as SwitchDeviceClass, SwitchEntity as SwitchEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

_LOGGER: Any

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class HuaweiLteBaseSwitch(HuaweiLteBaseEntityWithDevice, SwitchEntity):
    key: str
    item: str
    _attr_device_class: SwitchDeviceClass
    _raw_state: Union[str, None]
    def _turn(self, state: bool) -> None: ...
    def turn_on(self, **kwargs: Any) -> None: ...
    def turn_off(self, **kwargs: Any) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    _available: bool
    async def async_update(self) -> None: ...
    def __init__(self, router) -> None: ...

class HuaweiLteMobileDataSwitch(HuaweiLteBaseSwitch):
    key: Any
    item: str
    def __post_init__(self) -> None: ...
    @property
    def _entity_name(self) -> str: ...
    @property
    def _device_unique_id(self) -> str: ...
    @property
    def is_on(self) -> bool: ...
    _raw_state: Any
    def _turn(self, state: bool) -> None: ...
    @property
    def icon(self) -> str: ...
    def __init__(self, router) -> None: ...
