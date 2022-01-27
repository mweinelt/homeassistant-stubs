from .const import CONF_INSTANCE_CLIENTS as CONF_INSTANCE_CLIENTS, CONF_ON_UNLOAD as CONF_ON_UNLOAD, CONF_ROOT_CLIENT as CONF_ROOT_CLIENT, DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN, HYPERION_RELEASES_URL as HYPERION_RELEASES_URL, HYPERION_VERSION_WARN_CUTOFF as HYPERION_VERSION_WARN_CUTOFF, SIGNAL_INSTANCE_ADD as SIGNAL_INSTANCE_ADD, SIGNAL_INSTANCE_REMOVE as SIGNAL_INSTANCE_REMOVE
from collections.abc import Callable as Callable
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT, CONF_TOKEN as CONF_TOKEN, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect, async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.typing import ConfigType as ConfigType
from hyperion import client
from typing import Any

PLATFORMS: Any
_LOGGER: Any

def get_hyperion_unique_id(server_id: str, instance: int, name: str) -> str: ...
def get_hyperion_device_id(server_id: str, instance: int) -> str: ...
def split_hyperion_unique_id(unique_id: str) -> Union[tuple[str, int, str], None]: ...
def create_hyperion_client(*args: Any, **kwargs: Any) -> client.HyperionClient: ...
async def async_create_connect_hyperion_client(*args: Any, **kwargs: Any) -> Union[client.HyperionClient, None]: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
def listen_for_instance_updates(hass: HomeAssistant, config_entry: ConfigEntry, add_func: Callable, remove_func: Callable) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def _async_entry_updated(hass: HomeAssistant, config_entry: ConfigEntry) -> None: ...
async def async_unload_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool: ...
