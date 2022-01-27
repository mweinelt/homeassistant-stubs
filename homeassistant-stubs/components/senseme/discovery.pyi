from .const import DISCOVERY as DISCOVERY, DOMAIN as DOMAIN
from aiosenseme import SensemeDevice as SensemeDevice
from homeassistant import config_entries as config_entries
from homeassistant.const import CONF_ID as CONF_ID
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback

def async_start_discovery(hass: HomeAssistant) -> bool: ...
def async_get_discovered_device(hass: HomeAssistant, uuid: str) -> SensemeDevice: ...
async def async_discover(hass: HomeAssistant, timeout: float) -> list[SensemeDevice]: ...
def async_trigger_discovery(hass: HomeAssistant, discovered_devices: list[SensemeDevice]) -> None: ...
