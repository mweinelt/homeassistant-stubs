import datetime as dt
from .const import ATTR_APP_ID as ATTR_APP_ID, ATTR_APP_NAME as ATTR_APP_NAME, ATTR_GROUP_MEMBERS as ATTR_GROUP_MEMBERS, ATTR_INPUT_SOURCE as ATTR_INPUT_SOURCE, ATTR_INPUT_SOURCE_LIST as ATTR_INPUT_SOURCE_LIST, ATTR_MEDIA_ALBUM_ARTIST as ATTR_MEDIA_ALBUM_ARTIST, ATTR_MEDIA_ALBUM_NAME as ATTR_MEDIA_ALBUM_NAME, ATTR_MEDIA_ARTIST as ATTR_MEDIA_ARTIST, ATTR_MEDIA_CHANNEL as ATTR_MEDIA_CHANNEL, ATTR_MEDIA_CONTENT_ID as ATTR_MEDIA_CONTENT_ID, ATTR_MEDIA_CONTENT_TYPE as ATTR_MEDIA_CONTENT_TYPE, ATTR_MEDIA_DURATION as ATTR_MEDIA_DURATION, ATTR_MEDIA_ENQUEUE as ATTR_MEDIA_ENQUEUE, ATTR_MEDIA_EPISODE as ATTR_MEDIA_EPISODE, ATTR_MEDIA_EXTRA as ATTR_MEDIA_EXTRA, ATTR_MEDIA_PLAYLIST as ATTR_MEDIA_PLAYLIST, ATTR_MEDIA_POSITION as ATTR_MEDIA_POSITION, ATTR_MEDIA_POSITION_UPDATED_AT as ATTR_MEDIA_POSITION_UPDATED_AT, ATTR_MEDIA_REPEAT as ATTR_MEDIA_REPEAT, ATTR_MEDIA_SEASON as ATTR_MEDIA_SEASON, ATTR_MEDIA_SEEK_POSITION as ATTR_MEDIA_SEEK_POSITION, ATTR_MEDIA_SERIES_TITLE as ATTR_MEDIA_SERIES_TITLE, ATTR_MEDIA_SHUFFLE as ATTR_MEDIA_SHUFFLE, ATTR_MEDIA_TITLE as ATTR_MEDIA_TITLE, ATTR_MEDIA_TRACK as ATTR_MEDIA_TRACK, ATTR_MEDIA_VOLUME_LEVEL as ATTR_MEDIA_VOLUME_LEVEL, ATTR_MEDIA_VOLUME_MUTED as ATTR_MEDIA_VOLUME_MUTED, ATTR_SOUND_MODE as ATTR_SOUND_MODE, ATTR_SOUND_MODE_LIST as ATTR_SOUND_MODE_LIST, DOMAIN as DOMAIN, MEDIA_CLASS_DIRECTORY as MEDIA_CLASS_DIRECTORY, REPEAT_MODES as REPEAT_MODES, SERVICE_CLEAR_PLAYLIST as SERVICE_CLEAR_PLAYLIST, SERVICE_JOIN as SERVICE_JOIN, SERVICE_PLAY_MEDIA as SERVICE_PLAY_MEDIA, SERVICE_SELECT_SOUND_MODE as SERVICE_SELECT_SOUND_MODE, SERVICE_SELECT_SOURCE as SERVICE_SELECT_SOURCE, SERVICE_UNJOIN as SERVICE_UNJOIN, SUPPORT_BROWSE_MEDIA as SUPPORT_BROWSE_MEDIA, SUPPORT_CLEAR_PLAYLIST as SUPPORT_CLEAR_PLAYLIST, SUPPORT_GROUPING as SUPPORT_GROUPING, SUPPORT_NEXT_TRACK as SUPPORT_NEXT_TRACK, SUPPORT_PAUSE as SUPPORT_PAUSE, SUPPORT_PLAY as SUPPORT_PLAY, SUPPORT_PLAY_MEDIA as SUPPORT_PLAY_MEDIA, SUPPORT_PREVIOUS_TRACK as SUPPORT_PREVIOUS_TRACK, SUPPORT_REPEAT_SET as SUPPORT_REPEAT_SET, SUPPORT_SEEK as SUPPORT_SEEK, SUPPORT_SELECT_SOUND_MODE as SUPPORT_SELECT_SOUND_MODE, SUPPORT_SELECT_SOURCE as SUPPORT_SELECT_SOURCE, SUPPORT_SHUFFLE_SET as SUPPORT_SHUFFLE_SET, SUPPORT_STOP as SUPPORT_STOP, SUPPORT_TURN_OFF as SUPPORT_TURN_OFF, SUPPORT_TURN_ON as SUPPORT_TURN_ON, SUPPORT_VOLUME_MUTE as SUPPORT_VOLUME_MUTE, SUPPORT_VOLUME_SET as SUPPORT_VOLUME_SET, SUPPORT_VOLUME_STEP as SUPPORT_VOLUME_STEP
from .errors import BrowseError as BrowseError
from aiohttp import web
from aiohttp.typedefs import LooseHeaders as LooseHeaders
from homeassistant.backports.enum import StrEnum as StrEnum
from homeassistant.components import websocket_api as websocket_api
from homeassistant.components.http import HomeAssistantView as HomeAssistantView, KEY_AUTHENTICATED as KEY_AUTHENTICATED
from homeassistant.components.websocket_api.const import ERR_NOT_FOUND as ERR_NOT_FOUND, ERR_NOT_SUPPORTED as ERR_NOT_SUPPORTED, ERR_UNKNOWN_ERROR as ERR_UNKNOWN_ERROR
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import SERVICE_MEDIA_NEXT_TRACK as SERVICE_MEDIA_NEXT_TRACK, SERVICE_MEDIA_PAUSE as SERVICE_MEDIA_PAUSE, SERVICE_MEDIA_PLAY as SERVICE_MEDIA_PLAY, SERVICE_MEDIA_PLAY_PAUSE as SERVICE_MEDIA_PLAY_PAUSE, SERVICE_MEDIA_PREVIOUS_TRACK as SERVICE_MEDIA_PREVIOUS_TRACK, SERVICE_MEDIA_SEEK as SERVICE_MEDIA_SEEK, SERVICE_MEDIA_STOP as SERVICE_MEDIA_STOP, SERVICE_REPEAT_SET as SERVICE_REPEAT_SET, SERVICE_SHUFFLE_SET as SERVICE_SHUFFLE_SET, SERVICE_TOGGLE as SERVICE_TOGGLE, SERVICE_TURN_OFF as SERVICE_TURN_OFF, SERVICE_TURN_ON as SERVICE_TURN_ON, SERVICE_VOLUME_DOWN as SERVICE_VOLUME_DOWN, SERVICE_VOLUME_MUTE as SERVICE_VOLUME_MUTE, SERVICE_VOLUME_SET as SERVICE_VOLUME_SET, SERVICE_VOLUME_UP as SERVICE_VOLUME_UP, STATE_IDLE as STATE_IDLE, STATE_OFF as STATE_OFF, STATE_PLAYING as STATE_PLAYING
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.config_validation import PLATFORM_SCHEMA as PLATFORM_SCHEMA, PLATFORM_SCHEMA_BASE as PLATFORM_SCHEMA_BASE, datetime as datetime
from homeassistant.helpers.entity import Entity as Entity, EntityDescription as EntityDescription
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.network import get_url as get_url
from homeassistant.loader import bind_hass as bind_hass
from typing import Any

_LOGGER: Any
ENTITY_ID_FORMAT: Any
CACHE_IMAGES: str
CACHE_MAXSIZE: str
CACHE_LOCK: str
CACHE_URL: str
CACHE_CONTENT: str
ENTITY_IMAGE_CACHE: Any
SCAN_INTERVAL: Any

class MediaPlayerDeviceClass(StrEnum):
    TV: str
    SPEAKER: str
    RECEIVER: str

DEVICE_CLASSES_SCHEMA: Any
DEVICE_CLASSES: Any
DEVICE_CLASS_TV: Any
DEVICE_CLASS_SPEAKER: Any
DEVICE_CLASS_RECEIVER: Any
MEDIA_PLAYER_PLAY_MEDIA_SCHEMA: Any
ATTR_TO_PROPERTY: Any

def is_on(hass, entity_id: Any | None = ...): ...
def _rename_keys(**keys): ...
async def async_setup(hass, config): ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class MediaPlayerEntityDescription(EntityDescription):
    device_class: Union[MediaPlayerDeviceClass, str, None]
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, force_update, icon, name, unit_of_measurement) -> None: ...

class MediaPlayerEntity(Entity):
    entity_description: MediaPlayerEntityDescription
    _access_token: Union[str, None]
    _attr_app_id: Union[str, None]
    _attr_app_name: Union[str, None]
    _attr_device_class: Union[MediaPlayerDeviceClass, str, None]
    _attr_group_members: Union[list[str], None]
    _attr_is_volume_muted: Union[bool, None]
    _attr_media_album_artist: Union[str, None]
    _attr_media_album_name: Union[str, None]
    _attr_media_artist: Union[str, None]
    _attr_media_channel: Union[str, None]
    _attr_media_content_id: Union[str, None]
    _attr_media_content_type: Union[str, None]
    _attr_media_duration: Union[int, None]
    _attr_media_episode: Union[str, None]
    _attr_media_image_hash: Union[str, None]
    _attr_media_image_remotely_accessible: bool
    _attr_media_image_url: Union[str, None]
    _attr_media_playlist: Union[str, None]
    _attr_media_position_updated_at: Union[dt.datetime, None]
    _attr_media_position: Union[int, None]
    _attr_media_season: Union[str, None]
    _attr_media_series_title: Union[str, None]
    _attr_media_title: Union[str, None]
    _attr_media_track: Union[int, None]
    _attr_repeat: Union[str, None]
    _attr_shuffle: Union[bool, None]
    _attr_sound_mode_list: Union[list[str], None]
    _attr_sound_mode: Union[str, None]
    _attr_source_list: Union[list[str], None]
    _attr_source: Union[str, None]
    _attr_state: Union[str, None]
    _attr_supported_features: int
    _attr_volume_level: Union[float, None]
    @property
    def device_class(self) -> Union[MediaPlayerDeviceClass, str, None]: ...
    @property
    def state(self) -> Union[str, None]: ...
    @property
    def access_token(self) -> str: ...
    @property
    def volume_level(self) -> Union[float, None]: ...
    @property
    def is_volume_muted(self) -> Union[bool, None]: ...
    @property
    def media_content_id(self) -> Union[str, None]: ...
    @property
    def media_content_type(self) -> Union[str, None]: ...
    @property
    def media_duration(self) -> Union[int, None]: ...
    @property
    def media_position(self) -> Union[int, None]: ...
    @property
    def media_position_updated_at(self) -> Union[dt.datetime, None]: ...
    @property
    def media_image_url(self) -> Union[str, None]: ...
    @property
    def media_image_remotely_accessible(self) -> bool: ...
    @property
    def media_image_hash(self) -> Union[str, None]: ...
    async def async_get_media_image(self): ...
    async def async_get_browse_image(self, media_content_type: str, media_content_id: str, media_image_id: Union[str, None] = ...) -> tuple[Union[str, None], Union[str, None]]: ...
    @property
    def media_title(self) -> Union[str, None]: ...
    @property
    def media_artist(self) -> Union[str, None]: ...
    @property
    def media_album_name(self) -> Union[str, None]: ...
    @property
    def media_album_artist(self) -> Union[str, None]: ...
    @property
    def media_track(self) -> Union[int, None]: ...
    @property
    def media_series_title(self) -> Union[str, None]: ...
    @property
    def media_season(self) -> Union[str, None]: ...
    @property
    def media_episode(self) -> Union[str, None]: ...
    @property
    def media_channel(self) -> Union[str, None]: ...
    @property
    def media_playlist(self) -> Union[str, None]: ...
    @property
    def app_id(self) -> Union[str, None]: ...
    @property
    def app_name(self) -> Union[str, None]: ...
    @property
    def source(self) -> Union[str, None]: ...
    @property
    def source_list(self) -> Union[list[str], None]: ...
    @property
    def sound_mode(self) -> Union[str, None]: ...
    @property
    def sound_mode_list(self) -> Union[list[str], None]: ...
    @property
    def shuffle(self) -> Union[bool, None]: ...
    @property
    def repeat(self) -> Union[str, None]: ...
    @property
    def group_members(self) -> Union[list[str], None]: ...
    @property
    def supported_features(self) -> int: ...
    def turn_on(self) -> None: ...
    async def async_turn_on(self) -> None: ...
    def turn_off(self) -> None: ...
    async def async_turn_off(self) -> None: ...
    def mute_volume(self, mute) -> None: ...
    async def async_mute_volume(self, mute) -> None: ...
    def set_volume_level(self, volume) -> None: ...
    async def async_set_volume_level(self, volume) -> None: ...
    def media_play(self) -> None: ...
    async def async_media_play(self) -> None: ...
    def media_pause(self) -> None: ...
    async def async_media_pause(self) -> None: ...
    def media_stop(self) -> None: ...
    async def async_media_stop(self) -> None: ...
    def media_previous_track(self) -> None: ...
    async def async_media_previous_track(self) -> None: ...
    def media_next_track(self) -> None: ...
    async def async_media_next_track(self) -> None: ...
    def media_seek(self, position) -> None: ...
    async def async_media_seek(self, position) -> None: ...
    def play_media(self, media_type, media_id, **kwargs) -> None: ...
    async def async_play_media(self, media_type, media_id, **kwargs) -> None: ...
    def select_source(self, source) -> None: ...
    async def async_select_source(self, source) -> None: ...
    def select_sound_mode(self, sound_mode) -> None: ...
    async def async_select_sound_mode(self, sound_mode) -> None: ...
    def clear_playlist(self) -> None: ...
    async def async_clear_playlist(self) -> None: ...
    def set_shuffle(self, shuffle) -> None: ...
    async def async_set_shuffle(self, shuffle) -> None: ...
    def set_repeat(self, repeat) -> None: ...
    async def async_set_repeat(self, repeat) -> None: ...
    @property
    def support_play(self): ...
    @property
    def support_pause(self): ...
    @property
    def support_stop(self): ...
    @property
    def support_seek(self): ...
    @property
    def support_volume_set(self): ...
    @property
    def support_volume_mute(self): ...
    @property
    def support_previous_track(self): ...
    @property
    def support_next_track(self): ...
    @property
    def support_play_media(self): ...
    @property
    def support_select_source(self): ...
    @property
    def support_select_sound_mode(self): ...
    @property
    def support_clear_playlist(self): ...
    @property
    def support_shuffle_set(self): ...
    @property
    def support_grouping(self): ...
    async def async_toggle(self) -> None: ...
    async def async_volume_up(self) -> None: ...
    async def async_volume_down(self) -> None: ...
    async def async_media_play_pause(self) -> None: ...
    @property
    def entity_picture(self): ...
    @property
    def media_image_local(self): ...
    @property
    def capability_attributes(self): ...
    @property
    def state_attributes(self): ...
    async def async_browse_media(self, media_content_type: Union[str, None] = ..., media_content_id: Union[str, None] = ...) -> BrowseMedia: ...
    def join_players(self, group_members) -> None: ...
    async def async_join_players(self, group_members) -> None: ...
    def unjoin_player(self) -> None: ...
    async def async_unjoin_player(self) -> None: ...
    async def _async_fetch_image_from_cache(self, url): ...
    async def _async_fetch_image(self, url): ...
    def get_browse_image_url(self, media_content_type: str, media_content_id: str, media_image_id: Union[str, None] = ...) -> str: ...

class MediaPlayerImageView(HomeAssistantView):
    requires_auth: bool
    url: str
    name: str
    extra_urls: Any
    component: Any
    def __init__(self, component) -> None: ...
    async def get(self, request: web.Request, entity_id: str, media_content_type: Union[str, None] = ..., media_content_id: Union[str, None] = ...) -> web.Response: ...

async def websocket_handle_thumbnail(hass, connection, msg) -> None: ...
async def websocket_browse_media(hass, connection, msg) -> None: ...

class MediaPlayerDevice(MediaPlayerEntity):
    def __init_subclass__(cls, **kwargs) -> None: ...

class BrowseMedia:
    media_class: Any
    media_content_id: Any
    media_content_type: Any
    title: Any
    can_play: Any
    can_expand: Any
    children: Any
    children_media_class: Any
    thumbnail: Any
    def __init__(self, media_class: str, media_content_id: str, media_content_type: str, title: str, can_play: bool, can_expand: bool, *, children: Union[list[BrowseMedia], None] = ..., children_media_class: Union[str, None] = ..., thumbnail: Union[str, None] = ...) -> None: ...
    def as_dict(self, *, parent: bool = ...) -> dict: ...
    def calculate_children_class(self) -> None: ...
