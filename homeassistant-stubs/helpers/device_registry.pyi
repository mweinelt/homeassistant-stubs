from . import entity_registry as entity_registry, storage as storage
from .debounce import Debouncer as Debouncer
from .frame import report as report
from .json import JSON_DUMP as JSON_DUMP, find_paths_unserializable_data as find_paths_unserializable_data
from .typing import UNDEFINED as UNDEFINED, UndefinedType as UndefinedType
from _typeshed import Incomplete
from collections import UserDict
from collections.abc import ValuesView
from homeassistant.backports.enum import StrEnum as StrEnum
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EVENT_HOMEASSISTANT_STARTED as EVENT_HOMEASSISTANT_STARTED
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, RequiredParameterMissing as RequiredParameterMissing
from homeassistant.loader import bind_hass as bind_hass
from homeassistant.util.json import format_unserializable_data as format_unserializable_data
from typing import Any, TypeVar

_LOGGER: Incomplete
DATA_REGISTRY: str
EVENT_DEVICE_REGISTRY_UPDATED: str
STORAGE_KEY: str
STORAGE_VERSION_MAJOR: int
STORAGE_VERSION_MINOR: int
SAVE_DELAY: int
CLEANUP_DELAY: int
CONNECTION_BLUETOOTH: str
CONNECTION_NETWORK_MAC: str
CONNECTION_UPNP: str
CONNECTION_ZIGBEE: str
ORPHANED_DEVICE_KEEP_SECONDS: Incomplete
RUNTIME_ONLY_ATTRS: Incomplete

class DeviceEntryDisabler(StrEnum):
    CONFIG_ENTRY: str
    INTEGRATION: str
    USER: str

DISABLED_CONFIG_ENTRY: Incomplete
DISABLED_INTEGRATION: Incomplete
DISABLED_USER: Incomplete

class DeviceEntryType(StrEnum):
    SERVICE: str

class DeviceEntry:
    area_id: Union[str, None]
    config_entries: set[str]
    configuration_url: Union[str, None]
    connections: set[tuple[str, str]]
    disabled_by: Union[DeviceEntryDisabler, None]
    entry_type: Union[DeviceEntryType, None]
    hw_version: Union[str, None]
    id: str
    identifiers: set[tuple[str, str]]
    manufacturer: Union[str, None]
    model: Union[str, None]
    name_by_user: Union[str, None]
    name: Union[str, None]
    suggested_area: Union[str, None]
    sw_version: Union[str, None]
    via_device_id: Union[str, None]
    is_new: bool
    _json_repr: Union[str, None]
    @property
    def disabled(self) -> bool: ...
    @property
    def dict_repr(self) -> dict[str, Any]: ...
    @property
    def json_repr(self) -> Union[str, None]: ...
    def __init__(self, area_id, config_entries, configuration_url, connections, disabled_by, entry_type, hw_version, id, identifiers, manufacturer, model, name_by_user, name, suggested_area, sw_version, via_device_id, is_new, json_repr) -> None: ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...

class DeletedDeviceEntry:
    config_entries: set[str]
    connections: set[tuple[str, str]]
    identifiers: set[tuple[str, str]]
    id: str
    orphaned_timestamp: Union[float, None]
    def to_device_entry(self, config_entry_id: str, connections: set[tuple[str, str]], identifiers: set[tuple[str, str]]) -> DeviceEntry: ...
    def __init__(self, config_entries, connections, identifiers, id, orphaned_timestamp) -> None: ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...

def format_mac(mac: str) -> str: ...

class DeviceRegistryStore(storage.Store[dict[str, list[dict[str, Any]]]]):
    async def _async_migrate_func(self, old_major_version: int, old_minor_version: int, old_data: dict[str, list[dict[str, Any]]]) -> dict[str, Any]: ...
_EntryTypeT = TypeVar('_EntryTypeT', DeviceEntry, DeletedDeviceEntry)

class DeviceRegistryItems(UserDict[str, _EntryTypeT]):
    _connections: Incomplete
    _identifiers: Incomplete
    def __init__(self) -> None: ...
    def values(self) -> ValuesView[_EntryTypeT]: ...
    def __setitem__(self, key: str, entry: _EntryTypeT) -> None: ...
    def __delitem__(self, key: str) -> None: ...
    def get_entry(self, identifiers: set[tuple[str, str]], connections: Union[set[tuple[str, str]], None]) -> Union[_EntryTypeT, None]: ...

class DeviceRegistry:
    devices: DeviceRegistryItems[DeviceEntry]
    deleted_devices: DeviceRegistryItems[DeletedDeviceEntry]
    hass: Incomplete
    _store: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    def async_get(self, device_id: str) -> Union[DeviceEntry, None]: ...
    def async_get_device(self, identifiers: set[tuple[str, str]], connections: Union[set[tuple[str, str]], None] = ...) -> Union[DeviceEntry, None]: ...
    def _async_get_deleted_device(self, identifiers: set[tuple[str, str]], connections: Union[set[tuple[str, str]], None]) -> Union[DeletedDeviceEntry, None]: ...
    def async_get_or_create(self, *, config_entry_id: str, configuration_url: Union[str, None, UndefinedType] = ..., connections: Union[set[tuple[str, str]], None] = ..., default_manufacturer: Union[str, None, UndefinedType] = ..., default_model: Union[str, None, UndefinedType] = ..., default_name: Union[str, None, UndefinedType] = ..., disabled_by: Union[DeviceEntryDisabler, None, UndefinedType] = ..., entry_type: Union[DeviceEntryType, None, UndefinedType] = ..., hw_version: Union[str, None, UndefinedType] = ..., identifiers: Union[set[tuple[str, str]], None] = ..., manufacturer: Union[str, None, UndefinedType] = ..., model: Union[str, None, UndefinedType] = ..., name: Union[str, None, UndefinedType] = ..., suggested_area: Union[str, None, UndefinedType] = ..., sw_version: Union[str, None, UndefinedType] = ..., via_device: Union[tuple[str, str], None] = ...) -> DeviceEntry: ...
    def async_update_device(self, device_id: str, *, add_config_entry_id: Union[str, UndefinedType] = ..., area_id: Union[str, None, UndefinedType] = ..., configuration_url: Union[str, None, UndefinedType] = ..., disabled_by: Union[DeviceEntryDisabler, None, UndefinedType] = ..., entry_type: Union[DeviceEntryType, None, UndefinedType] = ..., hw_version: Union[str, None, UndefinedType] = ..., manufacturer: Union[str, None, UndefinedType] = ..., merge_connections: Union[set[tuple[str, str]], UndefinedType] = ..., merge_identifiers: Union[set[tuple[str, str]], UndefinedType] = ..., model: Union[str, None, UndefinedType] = ..., name_by_user: Union[str, None, UndefinedType] = ..., name: Union[str, None, UndefinedType] = ..., new_identifiers: Union[set[tuple[str, str]], UndefinedType] = ..., remove_config_entry_id: Union[str, UndefinedType] = ..., suggested_area: Union[str, None, UndefinedType] = ..., sw_version: Union[str, None, UndefinedType] = ..., via_device_id: Union[str, None, UndefinedType] = ...) -> Union[DeviceEntry, None]: ...
    def async_remove_device(self, device_id: str) -> None: ...
    async def async_load(self) -> None: ...
    def async_schedule_save(self) -> None: ...
    def _data_to_save(self) -> dict[str, list[dict[str, Any]]]: ...
    def async_clear_config_entry(self, config_entry_id: str) -> None: ...
    def async_purge_expired_orphaned_devices(self) -> None: ...
    def async_clear_area_id(self, area_id: str) -> None: ...

def async_get(hass: HomeAssistant) -> DeviceRegistry: ...
async def async_load(hass: HomeAssistant) -> None: ...
async def async_get_registry(hass: HomeAssistant) -> DeviceRegistry: ...
def async_entries_for_area(registry: DeviceRegistry, area_id: str) -> list[DeviceEntry]: ...
def async_entries_for_config_entry(registry: DeviceRegistry, config_entry_id: str) -> list[DeviceEntry]: ...
def async_config_entry_disabled_by_changed(registry: DeviceRegistry, config_entry: ConfigEntry) -> None: ...
def async_cleanup(hass: HomeAssistant, dev_reg: DeviceRegistry, ent_reg: entity_registry.EntityRegistry) -> None: ...
def async_setup_cleanup(hass: HomeAssistant, dev_reg: DeviceRegistry) -> None: ...
def _normalize_connections(connections: set[tuple[str, str]]) -> set[tuple[str, str]]: ...
