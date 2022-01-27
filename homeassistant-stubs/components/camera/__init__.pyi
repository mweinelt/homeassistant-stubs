from .const import CAMERA_IMAGE_TIMEOUT as CAMERA_IMAGE_TIMEOUT, CAMERA_STREAM_SOURCE_TIMEOUT as CAMERA_STREAM_SOURCE_TIMEOUT, CONF_DURATION as CONF_DURATION, CONF_LOOKBACK as CONF_LOOKBACK, DATA_CAMERA_PREFS as DATA_CAMERA_PREFS, DATA_RTSP_TO_WEB_RTC as DATA_RTSP_TO_WEB_RTC, DOMAIN as DOMAIN, SERVICE_RECORD as SERVICE_RECORD, STREAM_TYPE_HLS as STREAM_TYPE_HLS, STREAM_TYPE_WEB_RTC as STREAM_TYPE_WEB_RTC
from .img_util import scale_jpeg_camera_image as scale_jpeg_camera_image
from .prefs import CameraPreferences as CameraPreferences
from aiohttp import web
from collections.abc import Awaitable, Callable, Iterable
from homeassistant.components import websocket_api as websocket_api
from homeassistant.components.http import HomeAssistantView as HomeAssistantView, KEY_AUTHENTICATED as KEY_AUTHENTICATED
from homeassistant.components.media_player.const import ATTR_MEDIA_CONTENT_ID as ATTR_MEDIA_CONTENT_ID, ATTR_MEDIA_CONTENT_TYPE as ATTR_MEDIA_CONTENT_TYPE, ATTR_MEDIA_EXTRA as ATTR_MEDIA_EXTRA, SERVICE_PLAY_MEDIA as SERVICE_PLAY_MEDIA
from homeassistant.components.stream import Stream as Stream, create_stream as create_stream
from homeassistant.components.stream.const import FORMAT_CONTENT_TYPE as FORMAT_CONTENT_TYPE, OUTPUT_FORMATS as OUTPUT_FORMATS
from homeassistant.components.websocket_api import ActiveConnection as ActiveConnection
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, CONF_FILENAME as CONF_FILENAME, CONTENT_TYPE_MULTIPART as CONTENT_TYPE_MULTIPART, EVENT_HOMEASSISTANT_START as EVENT_HOMEASSISTANT_START, SERVICE_TURN_OFF as SERVICE_TURN_OFF, SERVICE_TURN_ON as SERVICE_TURN_ON
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.config_validation import PLATFORM_SCHEMA as PLATFORM_SCHEMA, PLATFORM_SCHEMA_BASE as PLATFORM_SCHEMA_BASE
from homeassistant.helpers.entity import Entity as Entity, EntityDescription as EntityDescription, entity_sources as entity_sources
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.network import get_url as get_url
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.loader import bind_hass as bind_hass
from typing import Any, Final, Optional

_LOGGER: Any
SERVICE_ENABLE_MOTION: Final[str]
SERVICE_DISABLE_MOTION: Final[str]
SERVICE_SNAPSHOT: Final[str]
SERVICE_PLAY_STREAM: Final[str]
SCAN_INTERVAL: Final[Any]
ENTITY_ID_FORMAT: Final[Any]
ATTR_FILENAME: Final[str]
ATTR_MEDIA_PLAYER: Final[str]
ATTR_FORMAT: Final[str]
STATE_RECORDING: Final[str]
STATE_STREAMING: Final[str]
STATE_IDLE: Final[str]
SUPPORT_ON_OFF: Final[int]
SUPPORT_STREAM: Final[int]
RTSP_PREFIXES: Any
DEFAULT_CONTENT_TYPE: Final[str]
ENTITY_IMAGE_URL: Final[str]
TOKEN_CHANGE_INTERVAL: Final[Any]
_RND: Final[Any]
MIN_STREAM_INTERVAL: Final[float]
CAMERA_SERVICE_SNAPSHOT: Final[Any]
CAMERA_SERVICE_PLAY_STREAM: Final[Any]
CAMERA_SERVICE_RECORD: Final[Any]
WS_TYPE_CAMERA_THUMBNAIL: Final[str]
SCHEMA_WS_CAMERA_THUMBNAIL: Final[Any]

class CameraEntityDescription(EntityDescription):
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, force_update, icon, name, unit_of_measurement) -> None: ...

class Image:
    content_type: str
    content: bytes
    def __init__(self, content_type, content) -> None: ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...

async def async_request_stream(hass: HomeAssistant, entity_id: str, fmt: str) -> str: ...
async def _async_get_image(camera: Camera, timeout: int = ..., width: Union[int, None] = ..., height: Union[int, None] = ...) -> Image: ...
async def async_get_image(hass: HomeAssistant, entity_id: str, timeout: int = ..., width: Union[int, None] = ..., height: Union[int, None] = ...) -> Image: ...
async def async_get_stream_source(hass: HomeAssistant, entity_id: str) -> Union[str, None]: ...
async def async_get_mjpeg_stream(hass: HomeAssistant, request: web.Request, entity_id: str) -> Union[web.StreamResponse, None]: ...
async def async_get_still_stream(request: web.Request, image_cb: Callable[[], Awaitable[Union[bytes, None]]], content_type: str, interval: float) -> web.StreamResponse: ...
def _get_camera_from_entity_id(hass: HomeAssistant, entity_id: str) -> Camera: ...
RtspToWebRtcProviderType = Callable[[str, str, str], Awaitable[Optional[str]]]

def async_register_rtsp_to_web_rtc_provider(hass: HomeAssistant, domain: str, provider: RtspToWebRtcProviderType) -> Callable[[], None]: ...
async def _async_refresh_providers(hass: HomeAssistant) -> None: ...
def _async_get_rtsp_to_web_rtc_providers(hass: HomeAssistant) -> Iterable[RtspToWebRtcProviderType]: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class Camera(Entity):
    _attr_brand: Union[str, None]
    _attr_frame_interval: float
    _attr_frontend_stream_type: Union[str, None]
    _attr_is_on: bool
    _attr_is_recording: bool
    _attr_is_streaming: bool
    _attr_model: Union[str, None]
    _attr_motion_detection_enabled: bool
    _attr_should_poll: bool
    _attr_state: None
    _attr_supported_features: int
    stream: Any
    stream_options: Any
    content_type: Any
    access_tokens: Any
    _warned_old_signature: bool
    _create_stream_lock: Any
    _rtsp_to_webrtc: bool
    def __init__(self) -> None: ...
    @property
    def entity_picture(self) -> str: ...
    @property
    def supported_features(self) -> int: ...
    @property
    def is_recording(self) -> bool: ...
    @property
    def is_streaming(self) -> bool: ...
    @property
    def brand(self) -> Union[str, None]: ...
    @property
    def motion_detection_enabled(self) -> bool: ...
    @property
    def model(self) -> Union[str, None]: ...
    @property
    def frame_interval(self) -> float: ...
    @property
    def frontend_stream_type(self) -> Union[str, None]: ...
    @property
    def available(self) -> bool: ...
    async def async_create_stream(self) -> Union[Stream, None]: ...
    async def stream_source(self) -> Union[str, None]: ...
    async def async_handle_web_rtc_offer(self, offer_sdp: str) -> Union[str, None]: ...
    def camera_image(self, width: Union[int, None] = ..., height: Union[int, None] = ...) -> Union[bytes, None]: ...
    async def async_camera_image(self, width: Union[int, None] = ..., height: Union[int, None] = ...) -> Union[bytes, None]: ...
    def async_warn_old_async_camera_image_signature(self) -> None: ...
    async def handle_async_still_stream(self, request: web.Request, interval: float) -> web.StreamResponse: ...
    async def handle_async_mjpeg_stream(self, request: web.Request) -> Union[web.StreamResponse, None]: ...
    @property
    def state(self) -> str: ...
    @property
    def is_on(self) -> bool: ...
    def turn_off(self) -> None: ...
    async def async_turn_off(self) -> None: ...
    def turn_on(self) -> None: ...
    async def async_turn_on(self) -> None: ...
    def enable_motion_detection(self) -> None: ...
    async def async_enable_motion_detection(self) -> None: ...
    def disable_motion_detection(self) -> None: ...
    async def async_disable_motion_detection(self) -> None: ...
    @property
    def state_attributes(self) -> dict[str, Union[str, None]]: ...
    def async_update_token(self) -> None: ...
    async def async_internal_added_to_hass(self) -> None: ...
    async def async_refresh_providers(self) -> None: ...
    async def _async_use_rtsp_to_webrtc(self) -> bool: ...

class CameraView(HomeAssistantView):
    requires_auth: bool
    component: Any
    def __init__(self, component: EntityComponent) -> None: ...
    async def get(self, request: web.Request, entity_id: str) -> web.StreamResponse: ...
    async def handle(self, request: web.Request, camera: Camera) -> web.StreamResponse: ...

class CameraImageView(CameraView):
    url: str
    name: str
    async def handle(self, request: web.Request, camera: Camera) -> web.Response: ...

class CameraMjpegStream(CameraView):
    url: str
    name: str
    async def handle(self, request: web.Request, camera: Camera) -> web.StreamResponse: ...

async def websocket_camera_thumbnail(hass: HomeAssistant, connection: ActiveConnection, msg: dict) -> None: ...
async def ws_camera_stream(hass: HomeAssistant, connection: ActiveConnection, msg: dict) -> None: ...
async def ws_camera_web_rtc_offer(hass: HomeAssistant, connection: ActiveConnection, msg: dict) -> None: ...
async def websocket_get_prefs(hass: HomeAssistant, connection: ActiveConnection, msg: dict) -> None: ...
async def websocket_update_prefs(hass: HomeAssistant, connection: ActiveConnection, msg: dict) -> None: ...
async def async_handle_snapshot_service(camera: Camera, service_call: ServiceCall) -> None: ...
async def async_handle_play_stream_service(camera: Camera, service_call: ServiceCall) -> None: ...
async def _async_stream_endpoint_url(hass: HomeAssistant, camera: Camera, fmt: str) -> str: ...
async def async_handle_record_service(camera: Camera, service_call: ServiceCall) -> None: ...
