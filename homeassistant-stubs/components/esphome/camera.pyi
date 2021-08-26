from . import EsphomeEntity as EsphomeEntity, platform_async_setup_entry as platform_async_setup_entry
from aioesphomeapi import CameraInfo, CameraState
from aiohttp import web as web
from homeassistant.components import camera as camera
from homeassistant.components.camera import Camera as Camera
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class EsphomeCamera(Camera, EsphomeEntity[CameraInfo, CameraState]):
    _image_cond: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def _on_state_update(self) -> None: ...
    async def _on_state_update_coro(self) -> None: ...
    async def async_camera_image(self, width: Union[int, None] = ..., height: Union[int, None] = ...) -> Union[bytes, None]: ...
    async def _async_camera_stream_image(self) -> Union[bytes, None]: ...
    async def handle_async_mjpeg_stream(self, request: web.Request) -> web.StreamResponse: ...
