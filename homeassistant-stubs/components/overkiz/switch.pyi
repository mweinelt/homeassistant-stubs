from . import HomeAssistantOverkizData as HomeAssistantOverkizData
from .const import DOMAIN as DOMAIN
from .entity import OverkizDescriptiveEntity as OverkizDescriptiveEntity
from collections.abc import Awaitable, Callable as Callable
from homeassistant.components.switch import SwitchDeviceClass as SwitchDeviceClass, SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pyoverkiz.types import StateType as OverkizStateType
from typing import Any

class OverkizSwitchDescriptionMixin:
    turn_on: Callable[[Callable[..., Awaitable[None]]], Awaitable[None]]
    turn_off: Callable[[Callable[..., Awaitable[None]]], Awaitable[None]]
    is_on: Callable[[Callable[[str], OverkizStateType]], bool]
    def __init__(self, turn_on, turn_off, is_on) -> None: ...

class OverkizSwitchDescription(SwitchEntityDescription, OverkizSwitchDescriptionMixin):
    def __init__(self, turn_on, turn_off, is_on, key, device_class, entity_category, entity_registry_enabled_default, force_update, icon, name, unit_of_measurement) -> None: ...

SWITCH_DESCRIPTIONS: list[OverkizSwitchDescription]
SUPPORTED_DEVICES: Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class OverkizSwitch(OverkizDescriptiveEntity, SwitchEntity):
    entity_description: OverkizSwitchDescription
    @property
    def is_on(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
