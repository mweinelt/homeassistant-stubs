import abc
from .const import CONF_DESCRIPTION as CONF_DESCRIPTION, CONF_SESSION_ID as CONF_SESSION_ID, ENCRYPTED_WEBSOCKET_PORT as ENCRYPTED_WEBSOCKET_PORT, LEGACY_PORT as LEGACY_PORT, LOGGER as LOGGER, METHOD_ENCRYPTED_WEBSOCKET as METHOD_ENCRYPTED_WEBSOCKET, METHOD_LEGACY as METHOD_LEGACY, METHOD_WEBSOCKET as METHOD_WEBSOCKET, RESULT_AUTH_MISSING as RESULT_AUTH_MISSING, RESULT_CANNOT_CONNECT as RESULT_CANNOT_CONNECT, RESULT_NOT_SUPPORTED as RESULT_NOT_SUPPORTED, RESULT_SUCCESS as RESULT_SUCCESS, SUCCESSFUL_RESULTS as SUCCESSFUL_RESULTS, TIMEOUT_REQUEST as TIMEOUT_REQUEST, TIMEOUT_WEBSOCKET as TIMEOUT_WEBSOCKET, VALUE_CONF_ID as VALUE_CONF_ID, VALUE_CONF_NAME as VALUE_CONF_NAME, WEBSOCKET_PORTS as WEBSOCKET_PORTS
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from collections.abc import Callable as Callable, Mapping
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_ID as CONF_ID, CONF_METHOD as CONF_METHOD, CONF_MODEL as CONF_MODEL, CONF_NAME as CONF_NAME, CONF_PORT as CONF_PORT, CONF_TIMEOUT as CONF_TIMEOUT, CONF_TOKEN as CONF_TOKEN
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant
from homeassistant.helpers import entity_component as entity_component
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.device_registry import format_mac as format_mac
from samsungctl import Remote
from samsungtvws.async_remote import SamsungTVWSAsyncRemote
from samsungtvws.command import SamsungTVCommand
from samsungtvws.encrypted.command import SamsungTVEncryptedCommand
from samsungtvws.encrypted.remote import SamsungTVEncryptedWSAsyncRemote
from typing import Any, TypeVar

SCAN_INTERVAL_PLUS_OFF_TIME: Incomplete
KEY_PRESS_TIMEOUT: float
ENCRYPTED_MODEL_USES_POWER_OFF: Incomplete
ENCRYPTED_MODEL_USES_POWER: Incomplete
REST_EXCEPTIONS: Incomplete
_RemoteT = TypeVar('_RemoteT', SamsungTVWSAsyncRemote, SamsungTVEncryptedWSAsyncRemote)
_CommandT = TypeVar('_CommandT', SamsungTVCommand, SamsungTVEncryptedCommand)

def mac_from_device_info(info: dict[str, Any]) -> str | None: ...
def model_requires_encryption(model: str | None) -> bool: ...
async def async_get_device_info(hass: HomeAssistant, host: str) -> tuple[str, int | None, str | None, dict[str, Any] | None]: ...

class SamsungTVBridge(ABC, metaclass=abc.ABCMeta):
    @staticmethod
    def get_bridge(hass: HomeAssistant, method: str, host: str, port: int | None = ..., entry_data: Mapping[str, Any] | None = ...) -> SamsungTVBridge: ...
    hass: Incomplete
    port: Incomplete
    method: Incomplete
    host: Incomplete
    token: Incomplete
    session_id: Incomplete
    _reauth_callback: Incomplete
    _update_config_entry: Incomplete
    _app_list_callback: Incomplete
    _end_of_power_off: Incomplete
    def __init__(self, hass: HomeAssistant, method: str, host: str, port: int | None = ...) -> None: ...
    def register_reauth_callback(self, func: CALLBACK_TYPE) -> None: ...
    def register_update_config_entry_callback(self, func: Callable[[Mapping[str, Any]], None]) -> None: ...
    def register_app_list_callback(self, func: Callable[[dict[str, str]], None]) -> None: ...
    @abstractmethod
    async def async_try_connect(self) -> str: ...
    @abstractmethod
    async def async_device_info(self) -> dict[str, Any] | None: ...
    async def async_request_app_list(self) -> None: ...
    @abstractmethod
    async def async_is_on(self) -> bool: ...
    @abstractmethod
    async def async_send_keys(self, keys: list[str]) -> None: ...
    @property
    def power_off_in_progress(self) -> bool: ...
    async def async_power_off(self) -> None: ...
    @abstractmethod
    async def _async_send_power_off(self) -> None: ...
    @abstractmethod
    async def async_close_remote(self) -> None: ...
    def _notify_reauth_callback(self) -> None: ...
    def _notify_update_config_entry(self, updates: Mapping[str, Any]) -> None: ...
    def _notify_app_list_callback(self, app_list: dict[str, str]) -> None: ...

class SamsungTVLegacyBridge(SamsungTVBridge):
    config: Incomplete
    _remote: Incomplete
    def __init__(self, hass: HomeAssistant, method: str, host: str, port: int | None) -> None: ...
    async def async_is_on(self) -> bool: ...
    def _is_on(self) -> bool: ...
    async def async_try_connect(self) -> str: ...
    def _try_connect(self) -> str: ...
    async def async_device_info(self) -> None: ...
    def _get_remote(self) -> Remote: ...
    async def async_send_keys(self, keys: list[str]) -> None: ...
    def _send_key(self, key: str) -> None: ...
    async def _async_send_power_off(self) -> None: ...
    async def async_close_remote(self) -> None: ...
    def _close_remote(self) -> None: ...

class SamsungTVWSBaseBridge(SamsungTVBridge, metaclass=abc.ABCMeta):
    _remote: Incomplete
    _remote_lock: Incomplete
    def __init__(self, hass: HomeAssistant, method: str, host: str, port: int | None = ...) -> None: ...
    async def async_is_on(self) -> bool: ...
    async def _async_send_commands(self, commands: list[_CommandT]) -> None: ...
    async def _async_get_remote(self) -> _RemoteT | None: ...
    @abstractmethod
    async def _async_get_remote_under_lock(self) -> _RemoteT | None: ...
    async def async_close_remote(self) -> None: ...

class SamsungTVWSBridge(SamsungTVWSBaseBridge[SamsungTVWSAsyncRemote, SamsungTVCommand]):
    token: Incomplete
    _rest_api: Incomplete
    _device_info: Incomplete
    def __init__(self, hass: HomeAssistant, method: str, host: str, port: int | None = ..., entry_data: Mapping[str, Any] | None = ...) -> None: ...
    def _get_device_spec(self, key: str) -> Any | None: ...
    async def async_is_on(self) -> bool: ...
    async def async_try_connect(self) -> str: ...
    async def async_device_info(self, force: bool = ...) -> dict[str, Any] | None: ...
    async def async_launch_app(self, app_id: str) -> None: ...
    async def async_request_app_list(self) -> None: ...
    async def async_send_keys(self, keys: list[str]) -> None: ...
    _remote: Incomplete
    async def _async_get_remote_under_lock(self) -> SamsungTVWSAsyncRemote | None: ...
    def _remote_event(self, event: str, response: Any) -> None: ...
    async def _async_send_power_off(self) -> None: ...

class SamsungTVEncryptedBridge(SamsungTVWSBaseBridge[SamsungTVEncryptedWSAsyncRemote, SamsungTVEncryptedCommand]):
    _power_off_warning_logged: bool
    _model: Incomplete
    _short_model: Incomplete
    token: Incomplete
    session_id: Incomplete
    _rest_api_port: Incomplete
    _device_info: Incomplete
    def __init__(self, hass: HomeAssistant, method: str, host: str, port: int | None = ..., entry_data: Mapping[str, Any] | None = ...) -> None: ...
    port: Incomplete
    async def async_try_connect(self) -> str: ...
    async def async_device_info(self) -> dict[str, Any] | None: ...
    async def async_send_keys(self, keys: list[str]) -> None: ...
    _remote: Incomplete
    async def _async_get_remote_under_lock(self) -> SamsungTVEncryptedWSAsyncRemote | None: ...
    async def _async_send_power_off(self) -> None: ...
