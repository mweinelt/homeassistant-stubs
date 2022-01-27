from .const import DOMAIN as DOMAIN, PLATFORMS as PLATFORMS
from .coordinator import PVOutputDataUpdateCoordinator as PVOutputDataUpdateCoordinator
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
