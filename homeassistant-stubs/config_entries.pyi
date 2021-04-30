from collections.abc import Iterable, Mapping
from contextvars import ContextVar
from homeassistant import data_entry_flow as data_entry_flow, loader as loader
from homeassistant.const import EVENT_HOMEASSISTANT_STARTED as EVENT_HOMEASSISTANT_STARTED, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, CoreState as CoreState, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady, HomeAssistantError as HomeAssistantError
from homeassistant.helpers import device_registry as device_registry, entity_registry as entity_registry
from homeassistant.helpers.event import Event as Event
from homeassistant.helpers.typing import DiscoveryInfoType as DiscoveryInfoType, UNDEFINED as UNDEFINED, UndefinedType as UndefinedType
from homeassistant.setup import async_process_deps_reqs as async_process_deps_reqs, async_setup_component as async_setup_component
from homeassistant.util.decorator import Registry as Registry
from typing import Any

_LOGGER: Any
SOURCE_DISCOVERY: str
SOURCE_HASSIO: str
SOURCE_HOMEKIT: str
SOURCE_IMPORT: str
SOURCE_INTEGRATION_DISCOVERY: str
SOURCE_MQTT: str
SOURCE_SSDP: str
SOURCE_USER: str
SOURCE_ZEROCONF: str
SOURCE_DHCP: str
SOURCE_IGNORE: str
SOURCE_UNIGNORE: str
SOURCE_REAUTH: str
HANDLERS: Any
STORAGE_KEY: str
STORAGE_VERSION: int
PATH_CONFIG: str
SAVE_DELAY: int
ENTRY_STATE_LOADED: str
ENTRY_STATE_SETUP_ERROR: str
ENTRY_STATE_MIGRATION_ERROR: str
ENTRY_STATE_SETUP_RETRY: str
ENTRY_STATE_NOT_LOADED: str
ENTRY_STATE_FAILED_UNLOAD: str
UNRECOVERABLE_STATES: Any
DEFAULT_DISCOVERY_UNIQUE_ID: str
DISCOVERY_NOTIFICATION_ID: str
DISCOVERY_SOURCES: Any
RECONFIGURE_NOTIFICATION_ID: str
EVENT_FLOW_DISCOVERED: str
CONN_CLASS_CLOUD_PUSH: str
CONN_CLASS_CLOUD_POLL: str
CONN_CLASS_LOCAL_PUSH: str
CONN_CLASS_LOCAL_POLL: str
CONN_CLASS_ASSUMED: str
CONN_CLASS_UNKNOWN: str
DISABLED_USER: str
RELOAD_AFTER_UPDATE_DELAY: int

class ConfigError(HomeAssistantError): ...
class UnknownEntry(ConfigError): ...
class OperationNotAllowed(ConfigError): ...

UpdateListenerType: Any

class ConfigEntry:
    __slots__: Any = ...
    entry_id: Any = ...
    version: Any = ...
    domain: Any = ...
    title: Any = ...
    data: Any = ...
    options: Any = ...
    system_options: Any = ...
    source: Any = ...
    connection_class: Any = ...
    state: Any = ...
    unique_id: Any = ...
    disabled_by: Any = ...
    supports_unload: bool = ...
    update_listeners: Any = ...
    reason: Any = ...
    _async_cancel_retry_setup: Any = ...
    _on_unload: Any = ...
    def __init__(self, version: int, domain: str, title: str, data: Mapping[str, Any], source: str, connection_class: str, system_options: dict, options: Union[dict, None]=..., unique_id: Union[str, None]=..., entry_id: Union[str, None]=..., state: str=..., disabled_by: Union[str, None]=...) -> None: ...
    async def async_setup(self, hass: HomeAssistant, *, integration: Union[loader.Integration, None]=..., tries: int=...) -> None: ...
    async def async_shutdown(self) -> None: ...
    def async_cancel_retry_setup(self) -> None: ...
    async def async_unload(self, hass: HomeAssistant, *, integration: Union[loader.Integration, None]=...) -> bool: ...
    async def async_remove(self, hass: HomeAssistant) -> None: ...
    async def async_migrate(self, hass: HomeAssistant) -> bool: ...
    def add_update_listener(self, listener: UpdateListenerType) -> CALLBACK_TYPE: ...
    def as_dict(self) -> dict[str, Any]: ...
    def async_on_unload(self, func: CALLBACK_TYPE) -> None: ...
    def _async_process_on_unload(self) -> None: ...
    def async_start_reauth(self, hass: HomeAssistant) -> None: ...

current_entry: ContextVar[Union[ConfigEntry, None]]

class ConfigEntriesFlowManager(data_entry_flow.FlowManager):
    config_entries: Any = ...
    _hass_config: Any = ...
    def __init__(self, hass: HomeAssistant, config_entries: ConfigEntries, hass_config: dict) -> None: ...
    async def async_finish_flow(self, flow: data_entry_flow.FlowHandler, result: data_entry_flow.FlowResult) -> data_entry_flow.FlowResult: ...
    async def async_create_flow(self, handler_key: Any, *, context: Union[dict, None]=..., data: Any=...) -> ConfigFlow: ...
    async def async_post_init(self, flow: data_entry_flow.FlowHandler, result: data_entry_flow.FlowResult) -> None: ...

class ConfigEntries:
    hass: Any = ...
    flow: Any = ...
    options: Any = ...
    _hass_config: Any = ...
    _entries: Any = ...
    _store: Any = ...
    def __init__(self, hass: HomeAssistant, hass_config: dict) -> None: ...
    def async_domains(self, include_ignore: bool=..., include_disabled: bool=...) -> list[str]: ...
    def async_get_entry(self, entry_id: str) -> Union[ConfigEntry, None]: ...
    def async_entries(self, domain: Union[str, None]=...) -> list[ConfigEntry]: ...
    async def async_add(self, entry: ConfigEntry) -> None: ...
    async def async_remove(self, entry_id: str) -> dict[str, Any]: ...
    async def _async_shutdown(self, event: Event) -> None: ...
    async def async_initialize(self) -> None: ...
    async def async_setup(self, entry_id: str) -> bool: ...
    async def async_unload(self, entry_id: str) -> bool: ...
    async def async_reload(self, entry_id: str) -> bool: ...
    async def async_set_disabled_by(self, entry_id: str, disabled_by: Union[str, None]) -> bool: ...
    def async_update_entry(self, entry: ConfigEntry, *, unique_id: Union[str, dict, None, UndefinedType]=..., title: Union[str, dict, UndefinedType]=..., data: Union[dict, UndefinedType]=..., options: Union[Mapping[str, Any], UndefinedType]=..., system_options: Union[dict, UndefinedType]=...) -> bool: ...
    def async_setup_platforms(self, entry: ConfigEntry, platforms: Iterable[str]) -> None: ...
    async def async_forward_entry_setup(self, entry: ConfigEntry, domain: str) -> bool: ...
    async def async_unload_platforms(self, entry: ConfigEntry, platforms: Iterable[str]) -> bool: ...
    async def async_forward_entry_unload(self, entry: ConfigEntry, domain: str) -> bool: ...
    def _async_schedule_save(self) -> None: ...
    def _data_to_save(self) -> dict[str, list[dict[str, Any]]]: ...

async def _old_conf_migrator(old_config: dict[str, Any]) -> dict[str, Any]: ...

class ConfigFlow(data_entry_flow.FlowHandler):
    def __init_subclass__(cls: Any, domain: Union[str, None]=..., **kwargs: Any) -> None: ...
    CONNECTION_CLASS: Any = ...
    @property
    def unique_id(self) -> Union[str, None]: ...
    @staticmethod
    def async_get_options_flow(config_entry: ConfigEntry) -> OptionsFlow: ...
    def _abort_if_unique_id_configured(self, updates: Union[dict[Any, Any], None]=..., reload_on_update: bool=...) -> None: ...
    async def async_set_unique_id(self, unique_id: Union[str, None]=..., *, raise_on_progress: bool=...) -> Union[ConfigEntry, None]: ...
    def _set_confirm_only(self) -> None: ...
    def _async_current_entries(self, include_ignore: Union[bool, None]=...) -> list[ConfigEntry]: ...
    def _async_current_ids(self, include_ignore: bool=...) -> set[Union[str, None]]: ...
    def _async_in_progress(self, include_uninitialized: bool=...) -> list[data_entry_flow.FlowResult]: ...
    async def async_step_ignore(self, user_input: dict[str, Any]) -> data_entry_flow.FlowResult: ...
    async def async_step_unignore(self, user_input: dict[str, Any]) -> data_entry_flow.FlowResult: ...
    async def async_step_user(self, user_input: Union[dict[str, Any], None]=...) -> data_entry_flow.FlowResult: ...
    async def _async_handle_discovery_without_unique_id(self) -> None: ...
    async def async_step_discovery(self, discovery_info: DiscoveryInfoType) -> data_entry_flow.FlowResult: ...
    def async_abort(self, reason: str, *, description_placeholders: Union[dict, None]=...) -> data_entry_flow.FlowResult: ...
    async def async_step_hassio(self, discovery_info: DiscoveryInfoType) -> data_entry_flow.FlowResult: ...
    async def async_step_homekit(self, discovery_info: DiscoveryInfoType) -> data_entry_flow.FlowResult: ...
    async def async_step_mqtt(self, discovery_info: DiscoveryInfoType) -> data_entry_flow.FlowResult: ...
    async def async_step_ssdp(self, discovery_info: DiscoveryInfoType) -> data_entry_flow.FlowResult: ...
    async def async_step_zeroconf(self, discovery_info: DiscoveryInfoType) -> data_entry_flow.FlowResult: ...
    async def async_step_dhcp(self, discovery_info: DiscoveryInfoType) -> data_entry_flow.FlowResult: ...

class OptionsFlowManager(data_entry_flow.FlowManager):
    async def async_create_flow(self, handler_key: Any, *, context: Union[dict[str, Any], None]=..., data: Union[dict[str, Any], None]=...) -> OptionsFlow: ...
    async def async_finish_flow(self, flow: data_entry_flow.FlowHandler, result: data_entry_flow.FlowResult) -> data_entry_flow.FlowResult: ...

class OptionsFlow(data_entry_flow.FlowHandler):
    handler: str

class SystemOptions:
    disable_new_entities: bool = ...
    def update(self, disable_new_entities: bool) -> None: ...
    def as_dict(self) -> dict[str, Any]: ...
    def __init__(self, disable_new_entities: Any) -> None: ...
    def __lt__(self, other: Any) -> Any: ...
    def __le__(self, other: Any) -> Any: ...
    def __gt__(self, other: Any) -> Any: ...
    def __ge__(self, other: Any) -> Any: ...

class EntityRegistryDisabledHandler:
    hass: Any = ...
    registry: Any = ...
    changed: Any = ...
    _remove_call_later: Any = ...
    def __init__(self, hass: HomeAssistant) -> None: ...
    def async_setup(self) -> None: ...
    async def _handle_entry_updated(self, event: Event) -> None: ...
    async def _handle_reload(self, _now: Any) -> None: ...

def _handle_entry_updated_filter(event: Event) -> bool: ...
async def support_entry_unload(hass: HomeAssistant, domain: str) -> bool: ...
