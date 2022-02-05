from homeassistant.components.light import ATTR_TRANSITION as ATTR_TRANSITION
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_PLATFORM as CONF_PLATFORM, SERVICE_TURN_ON as SERVICE_TURN_ON
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

DOMAIN: str
STATES: str

def _hass_domain_validator(config): ...
def _platform_validator(config): ...

PLATFORM_SCHEMA: Any

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class Scene(RestoreEntity):
    _attr_should_poll: bool
    __last_activated: Union[str, None]
    @property
    def state(self) -> Union[str, None]: ...
    async def _async_activate(self, **kwargs: Any) -> None: ...
    async def async_internal_added_to_hass(self) -> None: ...
    def activate(self, **kwargs: Any) -> None: ...
    async def async_activate(self, **kwargs: Any) -> None: ...
