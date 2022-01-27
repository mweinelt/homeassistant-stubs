from .const import CONF_TRACKED_ASSET_PAIRS as CONF_TRACKED_ASSET_PAIRS, DEFAULT_SCAN_INTERVAL as DEFAULT_SCAN_INTERVAL, DEFAULT_TRACKED_ASSET_PAIR as DEFAULT_TRACKED_ASSET_PAIR, DISPATCH_CONFIG_UPDATED as DISPATCH_CONFIG_UPDATED, DOMAIN as DOMAIN, KrakenResponse as KrakenResponse
from .utils import get_tradable_asset_pairs as get_tradable_asset_pairs
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_SCAN_INTERVAL as CONF_SCAN_INTERVAL, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import Any

CALL_RATE_LIMIT_SLEEP: int
PLATFORMS: Any
_LOGGER: Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool: ...

class KrakenData:
    _hass: Any
    _config_entry: Any
    _api: Any
    tradable_asset_pairs: Any
    coordinator: Any
    def __init__(self, hass: HomeAssistant, config_entry: ConfigEntry) -> None: ...
    async def async_update(self) -> Union[KrakenResponse, None]: ...
    def _get_kraken_data(self) -> KrakenResponse: ...
    async def _async_refresh_tradable_asset_pairs(self) -> None: ...
    async def async_setup(self) -> None: ...
    def _get_websocket_name_asset_pairs(self) -> str: ...
    def set_update_interval(self, update_interval: int) -> None: ...

async def async_options_updated(hass: HomeAssistant, config_entry: ConfigEntry) -> None: ...
