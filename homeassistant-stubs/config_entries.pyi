from . import data_entry_flow as data_entry_flow, loader as loader
from .backports.enum import StrEnum as StrEnum
from .components import persistent_notification as persistent_notification
from .components.dhcp import DhcpServiceInfo as DhcpServiceInfo
from .components.hassio import HassioServiceInfo as HassioServiceInfo
from .components.mqtt import MqttServiceInfo as MqttServiceInfo
from .components.ssdp import SsdpServiceInfo as SsdpServiceInfo
from .components.usb import UsbServiceInfo as UsbServiceInfo
from .components.zeroconf import ZeroconfServiceInfo as ZeroconfServiceInfo
from .const import EVENT_HOMEASSISTANT_STARTED as EVENT_HOMEASSISTANT_STARTED, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, Platform as Platform
from .core import CALLBACK_TYPE as CALLBACK_TYPE, CoreState as CoreState, Event as Event, HomeAssistant as HomeAssistant, callback as callback
from .exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady, HomeAssistantError as HomeAssistantError
from .helpers import device_registry as device_registry, entity_registry as entity_registry
from .helpers.event import async_call_later as async_call_later
from .helpers.frame import report as report
from .helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType, UNDEFINED as UNDEFINED, UndefinedType as UndefinedType
from .setup import async_process_deps_reqs as async_process_deps_reqs, async_setup_component as async_setup_component
from .util.decorator import Registry as Registry
from collections.abc import Iterable, Mapping
from contextvars import ContextVar
from enum import Enum
from typing import Any, TypeVar

_LOGGER: Any
SOURCE_DHCP: str
SOURCE_DISCOVERY: str
SOURCE_HASSIO: str
SOURCE_HOMEKIT: str
SOURCE_IMPORT: str
SOURCE_INTEGRATION_DISCOVERY: str
SOURCE_MQTT: str
SOURCE_SSDP: str
SOURCE_USB: str
SOURCE_USER: str
SOURCE_ZEROCONF: str
SOURCE_IGNORE: str
SOURCE_UNIGNORE: str
SOURCE_REAUTH: str
HANDLERS: Registry[str, type[ConfigFlow]]
STORAGE_KEY: str
STORAGE_VERSION: int
PATH_CONFIG: str
SAVE_DELAY: int
_T = TypeVar('_T', bound='ConfigEntryState')

class ConfigEntryState(Enum):
    LOADED: Any
    SETUP_ERROR: Any
    MIGRATION_ERROR: Any
    SETUP_RETRY: Any
    NOT_LOADED: Any
    FAILED_UNLOAD: Any
    _recoverable: bool
    def __new__(cls, value: str, recoverable: bool) -> _T: ...
    @property
    def recoverable(self) -> bool: ...

DEFAULT_DISCOVERY_UNIQUE_ID: str
DISCOVERY_NOTIFICATION_ID: str
DISCOVERY_SOURCES: Any
RECONFIGURE_NOTIFICATION_ID: str
EVENT_FLOW_DISCOVERED: str

class ConfigEntryDisabler(StrEnum):
    USER: str

DISABLED_USER: Any
RELOAD_AFTER_UPDATE_DELAY: int
CONN_CLASS_CLOUD_PUSH: str
CONN_CLASS_CLOUD_POLL: str
CONN_CLASS_LOCAL_PUSH: str
CONN_CLASS_LOCAL_POLL: str
CONN_CLASS_ASSUMED: str
CONN_CLASS_UNKNOWN: str

class ConfigError(HomeAssistantError): ...
class UnknownEntry(ConfigError): ...
class OperationNotAllowed(ConfigError): ...

UpdateListenerType: Any

class ConfigEntry:
    __slots__: Any
    entry_id: Any
    version: Any
    domain: Any
    title: Any
    data: Any
    options: Any
    pref_disable_new_entities: Any
    pref_disable_polling: Any
    source: Any
    state: Any
    unique_id: Any
    disabled_by: Any
    supports_unload: bool
    supports_remove_device: bool
    update_listeners: Any
    reason: Any
    _async_cancel_retry_setup: Any
    _on_unload: Any
    def __init__(self, version: int, domain: str, title: str, data: Mapping[str, Any], source: str, pref_disable_new_entities: Union[bool, None] = ..., pref_disable_polling: Union[bool, None] = ..., options: Union[Mapping[str, Any], None] = ..., unique_id: Union[str, None] = ..., entry_id: Union[str, None] = ..., state: ConfigEntryState = ..., disabled_by: Union[ConfigEntryDisabler, None] = ...) -> None: ...
    async def async_setup(self, hass: HomeAssistant, *, integration: Union[loader.Integration, None] = ..., tries: int = ...) -> None: ...
    async def async_shutdown(self) -> None: ...
    def async_cancel_retry_setup(self) -> None: ...
    async def async_unload(self, hass: HomeAssistant, *, integration: Union[loader.Integration, None] = ...) -> bool: ...
    async def async_remove(self, hass: HomeAssistant) -> None: ...
    async def async_migrate(self, hass: HomeAssistant) -> bool: ...
    def add_update_listener(self, listener: UpdateListenerType) -> CALLBACK_TYPE: ...
    def as_dict(self) -> dict[str, Any]: ...
    def async_on_unload(self, func: CALLBACK_TYPE) -> None: ...
    def _async_process_on_unload(self) -> None: ...
    def async_start_reauth(self, hass: HomeAssistant) -> None: ...

current_entry: ContextVar[Union[ConfigEntry, None]]

class ConfigEntriesFlowManager(data_entry_flow.FlowManager):
    config_entries: Any
    _hass_config: Any
    def __init__(self, hass: HomeAssistant, config_entries: ConfigEntries, hass_config: ConfigType) -> None: ...
    def _async_has_other_discovery_flows(self, flow_id: str) -> bool: ...
    async def async_finish_flow(self, flow: data_entry_flow.FlowHandler, result: data_entry_flow.FlowResult) -> data_entry_flow.FlowResult: ...
    async def async_create_flow(self, handler_key: Any, *, context: Union[dict, None] = ..., data: Any = ...) -> ConfigFlow: ...
    async def async_post_init(self, flow: data_entry_flow.FlowHandler, result: data_entry_flow.FlowResult) -> None: ...

class ConfigEntries:
    hass: Any
    flow: Any
    options: Any
    _hass_config: Any
    _entries: Any
    _domain_index: Any
    _store: Any
    def __init__(self, hass: HomeAssistant, hass_config: ConfigType) -> None: ...
    def async_domains(self, include_ignore: bool = ..., include_disabled: bool = ...) -> list[str]: ...
    def async_get_entry(self, entry_id: str) -> Union[ConfigEntry, None]: ...
    def async_entries(self, domain: Union[str, None] = ...) -> list[ConfigEntry]: ...
    async def async_add(self, entry: ConfigEntry) -> None: ...
    async def async_remove(self, entry_id: str) -> dict[str, Any]: ...
    async def _async_shutdown(self, event: Event) -> None: ...
    async def async_initialize(self) -> None: ...
    async def async_setup(self, entry_id: str) -> bool: ...
    async def async_unload(self, entry_id: str) -> bool: ...
    async def async_reload(self, entry_id: str) -> bool: ...
    async def async_set_disabled_by(self, entry_id: str, disabled_by: Union[ConfigEntryDisabler, None]) -> bool: ...
    def async_update_entry(self, entry: ConfigEntry, *, unique_id: Union[str, None, UndefinedType] = ..., title: Union[str, UndefinedType] = ..., data: Union[Mapping[str, Any], UndefinedType] = ..., options: Union[Mapping[str, Any], UndefinedType] = ..., pref_disable_new_entities: Union[bool, UndefinedType] = ..., pref_disable_polling: Union[bool, UndefinedType] = ...) -> bool: ...
    def async_setup_platforms(self, entry: ConfigEntry, platforms: Iterable[Union[Platform, str]]) -> None: ...
    async def async_forward_entry_setup(self, entry: ConfigEntry, domain: Union[Platform, str]) -> bool: ...
    async def async_unload_platforms(self, entry: ConfigEntry, platforms: Iterable[Union[Platform, str]]) -> bool: ...
    async def async_forward_entry_unload(self, entry: ConfigEntry, domain: Union[Platform, str]) -> bool: ...
    def _async_schedule_save(self) -> None: ...
    def _data_to_save(self) -> dict[str, list[dict[str, Any]]]: ...

async def _old_conf_migrator(old_config: dict[str, Any]) -> dict[str, Any]: ...

class ConfigFlow(data_entry_flow.FlowHandler):
    def __init_subclass__(cls, domain: Union[str, None] = ..., **kwargs: Any) -> None: ...
    @property
    def unique_id(self) -> Union[str, None]: ...
    @staticmethod
    def async_get_options_flow(config_entry: ConfigEntry) -> OptionsFlow: ...
    @classmethod
    def async_supports_options_flow(cls, config_entry: ConfigEntry) -> bool: ...
    def _async_abort_entries_match(self, match_dict: Union[dict[str, Any], None] = ...) -> None: ...
    def _abort_if_unique_id_configured(self, updates: Union[dict[Any, Any], None] = ..., reload_on_update: bool = ...) -> None: ...
    async def async_set_unique_id(self, unique_id: Union[str, None] = ..., *, raise_on_progress: bool = ...) -> Union[ConfigEntry, None]: ...
    def _set_confirm_only(self) -> None: ...
    def _async_current_entries(self, include_ignore: Union[bool, None] = ...) -> list[ConfigEntry]: ...
    def _async_current_ids(self, include_ignore: bool = ...) -> set[Union[str, None]]: ...
    def _async_in_progress(self, include_uninitialized: bool = ...) -> list[data_entry_flow.FlowResult]: ...
    async def async_step_ignore(self, user_input: dict[str, Any]) -> data_entry_flow.FlowResult: ...
    async def async_step_unignore(self, user_input: dict[str, Any]) -> data_entry_flow.FlowResult: ...
    async def async_step_user(self, user_input: Union[dict[str, Any], None] = ...) -> data_entry_flow.FlowResult: ...
    async def _async_handle_discovery_without_unique_id(self) -> None: ...
    async def async_step_discovery(self, discovery_info: DiscoveryInfoType) -> data_entry_flow.FlowResult: ...
    def async_abort(self, reason: str, *, description_placeholders: Union[dict, None] = ...) -> data_entry_flow.FlowResult: ...
    async def async_step_dhcp(self, discovery_info: DhcpServiceInfo) -> data_entry_flow.FlowResult: ...
    async def async_step_hassio(self, discovery_info: HassioServiceInfo) -> data_entry_flow.FlowResult: ...
    async def async_step_integration_discovery(self, discovery_info: DiscoveryInfoType) -> data_entry_flow.FlowResult: ...
    async def async_step_homekit(self, discovery_info: ZeroconfServiceInfo) -> data_entry_flow.FlowResult: ...
    async def async_step_mqtt(self, discovery_info: MqttServiceInfo) -> data_entry_flow.FlowResult: ...
    async def async_step_ssdp(self, discovery_info: SsdpServiceInfo) -> data_entry_flow.FlowResult: ...
    async def async_step_usb(self, discovery_info: UsbServiceInfo) -> data_entry_flow.FlowResult: ...
    async def async_step_zeroconf(self, discovery_info: ZeroconfServiceInfo) -> data_entry_flow.FlowResult: ...
    def async_create_entry(self, title: str, data: Mapping[str, Any], *, description: Union[str, None] = ..., description_placeholders: Union[dict, None] = ..., options: Union[Mapping[str, Any], None] = ...) -> data_entry_flow.FlowResult: ...

class OptionsFlowManager(data_entry_flow.FlowManager):
    async def async_create_flow(self, handler_key: Any, *, context: Union[dict[str, Any], None] = ..., data: Union[dict[str, Any], None] = ...) -> OptionsFlow: ...
    async def async_finish_flow(self, flow: data_entry_flow.FlowHandler, result: data_entry_flow.FlowResult) -> data_entry_flow.FlowResult: ...

class OptionsFlow(data_entry_flow.FlowHandler):
    handler: str

class EntityRegistryDisabledHandler:
    hass: Any
    registry: Any
    changed: Any
    _remove_call_later: Any
    def __init__(self, hass: HomeAssistant) -> None: ...
    def async_setup(self) -> None: ...
    async def _handle_entry_updated(self, event: Event) -> None: ...
    async def _handle_reload(self, _now: Any) -> None: ...

def _handle_entry_updated_filter(event: Event) -> bool: ...
async def support_entry_unload(hass: HomeAssistant, domain: str) -> bool: ...
async def support_remove_from_device(hass: HomeAssistant, domain: str) -> bool: ...
