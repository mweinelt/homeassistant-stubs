from .const import DATA_AVAILABLE as DATA_AVAILABLE, DATA_VLC as DATA_VLC, DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from aiovlc.client import Client as Client
from collections.abc import Awaitable, Callable as Callable, Coroutine
from datetime import datetime
from homeassistant.components import media_source as media_source
from homeassistant.components.media_player import BrowseMedia as BrowseMedia, MediaPlayerEntity as MediaPlayerEntity, MediaPlayerEntityFeature as MediaPlayerEntityFeature, MediaPlayerState as MediaPlayerState, MediaType as MediaType, async_process_play_media_url as async_process_play_media_url
from homeassistant.config_entries import ConfigEntry as ConfigEntry, SOURCE_HASSIO as SOURCE_HASSIO
from homeassistant.const import CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any, Concatenate, TypeVar

MAX_VOLUME: int
_VlcDeviceT = TypeVar('_VlcDeviceT', bound='VlcDevice')
_P: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
def catch_vlc_errors(func: Callable[Concatenate[_VlcDeviceT, _P], Awaitable[None]]) -> Callable[Concatenate[_VlcDeviceT, _P], Coroutine[Any, Any, None]]: ...

class VlcDevice(MediaPlayerEntity):
    _attr_media_content_type: Incomplete
    _attr_supported_features: Incomplete
    _config_entry: Incomplete
    _name: Incomplete
    _volume: Incomplete
    _muted: Incomplete
    _media_position_updated_at: Incomplete
    _media_position: Incomplete
    _media_duration: Incomplete
    _vlc: Incomplete
    _available: Incomplete
    _volume_bkp: float
    _media_artist: Incomplete
    _media_title: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    _using_addon: Incomplete
    def __init__(self, config_entry: ConfigEntry, vlc: Client, name: str, available: bool) -> None: ...
    _attr_state: Incomplete
    _attr_media_album_name: Incomplete
    async def async_update(self) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def available(self) -> bool: ...
    @property
    def volume_level(self) -> Union[float, None]: ...
    @property
    def is_volume_muted(self) -> Union[bool, None]: ...
    @property
    def media_duration(self) -> Union[int, None]: ...
    @property
    def media_position(self) -> Union[int, None]: ...
    @property
    def media_position_updated_at(self) -> Union[datetime, None]: ...
    @property
    def media_title(self) -> Union[str, None]: ...
    @property
    def media_artist(self) -> Union[str, None]: ...
    async def async_media_seek(self, position: float) -> None: ...
    async def async_mute_volume(self, mute: bool) -> None: ...
    async def async_set_volume_level(self, volume: float) -> None: ...
    async def async_media_play(self) -> None: ...
    async def async_media_pause(self) -> None: ...
    async def async_media_stop(self) -> None: ...
    async def async_play_media(self, media_type: Union[MediaType, str], media_id: str, **kwargs: Any) -> None: ...
    async def async_media_previous_track(self) -> None: ...
    async def async_media_next_track(self) -> None: ...
    async def async_clear_playlist(self) -> None: ...
    async def async_set_shuffle(self, shuffle: bool) -> None: ...
    async def async_browse_media(self, media_content_type: Union[MediaType, str, None] = ..., media_content_id: Union[str, None] = ...) -> BrowseMedia: ...
