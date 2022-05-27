from .const import BRIDGE_MAKE as BRIDGE_MAKE
from _typeshed import Incomplete
from bond_async import Bond as Bond
from homeassistant.util.async_ import gather_with_concurrency as gather_with_concurrency
from typing import Any

MAX_REQUESTS: int
_LOGGER: Incomplete

class BondDevice:
    device_id: Incomplete
    props: Incomplete
    _attrs: Incomplete
    _supported_actions: Incomplete
    def __init__(self, device_id: str, attrs: dict[str, Any], props: dict[str, Any]) -> None: ...
    def __repr__(self) -> str: ...
    @property
    def name(self) -> str: ...
    @property
    def type(self) -> str: ...
    @property
    def location(self) -> Union[str, None]: ...
    @property
    def template(self) -> Union[str, None]: ...
    @property
    def branding_profile(self) -> Union[str, None]: ...
    @property
    def trust_state(self) -> bool: ...
    def has_action(self, action: str) -> bool: ...
    def _has_any_action(self, actions: set[str]) -> bool: ...
    def supports_speed(self) -> bool: ...
    def supports_direction(self) -> bool: ...
    def supports_set_position(self) -> bool: ...
    def supports_open(self) -> bool: ...
    def supports_close(self) -> bool: ...
    def supports_tilt_open(self) -> bool: ...
    def supports_tilt_close(self) -> bool: ...
    def supports_hold(self) -> bool: ...
    def supports_light(self) -> bool: ...
    def supports_up_light(self) -> bool: ...
    def supports_down_light(self) -> bool: ...
    def supports_set_brightness(self) -> bool: ...

class BondHub:
    bond: Incomplete
    host: Incomplete
    _bridge: Incomplete
    _version: Incomplete
    _devices: Incomplete
    def __init__(self, bond: Bond, host: str) -> None: ...
    async def setup(self, max_devices: Union[int, None] = ...) -> None: ...
    @property
    def bond_id(self) -> Union[str, None]: ...
    @property
    def target(self) -> Union[str, None]: ...
    @property
    def model(self) -> Union[str, None]: ...
    @property
    def make(self) -> str: ...
    @property
    def name(self) -> str: ...
    @property
    def location(self) -> Union[str, None]: ...
    @property
    def fw_ver(self) -> Union[str, None]: ...
    @property
    def mcu_ver(self) -> Union[str, None]: ...
    @property
    def devices(self) -> list[BondDevice]: ...
    @property
    def is_bridge(self) -> bool: ...
