from .const import ATTR_EVENT_SCORE as ATTR_EVENT_SCORE, DEFAULT_ATTRIBUTION as DEFAULT_ATTRIBUTION, DEFAULT_BRAND as DEFAULT_BRAND, DOMAIN as DOMAIN
from .data import ProtectData as ProtectData
from .models import ProtectRequiredKeysMixin as ProtectRequiredKeysMixin
from .utils import get_nested_attr as get_nested_attr
from collections.abc import Sequence
from homeassistant.core import callback as callback
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, Entity as Entity, EntityDescription as EntityDescription
from pyunifiprotect.data import Event as Event, ModelType, ProtectAdoptableDeviceModel as ProtectAdoptableDeviceModel
from pyunifiprotect.data.nvr import NVR as NVR
from typing import Any

_LOGGER: Any

def _async_device_entities(data: ProtectData, klass: type[ProtectDeviceEntity], model_type: ModelType, descs: Sequence[ProtectRequiredKeysMixin]) -> list[ProtectDeviceEntity]: ...
def async_all_device_entities(data: ProtectData, klass: type[ProtectDeviceEntity], camera_descs: Union[Sequence[ProtectRequiredKeysMixin], None] = ..., light_descs: Union[Sequence[ProtectRequiredKeysMixin], None] = ..., sense_descs: Union[Sequence[ProtectRequiredKeysMixin], None] = ..., viewer_descs: Union[Sequence[ProtectRequiredKeysMixin], None] = ..., lock_descs: Union[Sequence[ProtectRequiredKeysMixin], None] = ..., all_descs: Union[Sequence[ProtectRequiredKeysMixin], None] = ...) -> list[ProtectDeviceEntity]: ...

class ProtectDeviceEntity(Entity):
    device: ProtectAdoptableDeviceModel
    _attr_should_poll: bool
    data: Any
    _attr_unique_id: Any
    _attr_name: Any
    entity_description: Any
    _attr_attribution: Any
    def __init__(self, data: ProtectData, device: ProtectAdoptableDeviceModel, description: Union[EntityDescription, None] = ...) -> None: ...
    async def async_update(self) -> None: ...
    _attr_device_info: Any
    def _async_set_device_info(self) -> None: ...
    _attr_available: Any
    def _async_update_device_from_protect(self) -> None: ...
    def _async_updated_event(self) -> None: ...
    async def async_added_to_hass(self) -> None: ...

class ProtectNVREntity(ProtectDeviceEntity):
    device: NVR
    def __init__(self, entry: ProtectData, device: NVR, description: Union[EntityDescription, None] = ...) -> None: ...
    _attr_device_info: Any
    def _async_set_device_info(self) -> None: ...
    _attr_available: Any
    def _async_update_device_from_protect(self) -> None: ...

class EventThumbnailMixin(ProtectDeviceEntity):
    _event: Any
    def __init__(self, *args: Any, **kwarg: Any) -> None: ...
    def _async_get_event(self) -> Union[Event, None]: ...
    def _async_thumbnail_extra_attrs(self) -> dict[str, Any]: ...
    _attr_extra_state_attributes: Any
    def _async_update_device_from_protect(self) -> None: ...
