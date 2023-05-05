from .const import ATTR_REMAINING as ATTR_REMAINING, DEFAULT_ATTEMPTS as DEFAULT_ATTEMPTS, DOMAIN as DOMAIN, IDENTIFY_WAVEFORM as IDENTIFY_WAVEFORM, MAX_ATTEMPTS_PER_UPDATE_REQUEST_MESSAGE as MAX_ATTEMPTS_PER_UPDATE_REQUEST_MESSAGE, MAX_UPDATE_TIME as MAX_UPDATE_TIME, MESSAGE_RETRIES as MESSAGE_RETRIES, MESSAGE_TIMEOUT as MESSAGE_TIMEOUT, OVERALL_TIMEOUT as OVERALL_TIMEOUT, TARGET_ANY as TARGET_ANY, UNAVAILABLE_GRACE as UNAVAILABLE_GRACE, _LOGGER as _LOGGER
from .util import async_execute_lifx as async_execute_lifx, async_multi_execute_lifx_with_retries as async_multi_execute_lifx_with_retries, get_real_mac_addr as get_real_mac_addr, infrared_brightness_option_to_value as infrared_brightness_option_to_value, infrared_brightness_value_to_option as infrared_brightness_value_to_option, lifx_features as lifx_features
from _typeshed import Incomplete
from aiolifx.aiolifx import Light as Light
from aiolifx.connection import LIFXConnection as LIFXConnection
from collections.abc import Callable as Callable
from enum import IntEnum
from homeassistant.const import Platform as Platform, SIGNAL_STRENGTH_DECIBELS as SIGNAL_STRENGTH_DECIBELS, SIGNAL_STRENGTH_DECIBELS_MILLIWATT as SIGNAL_STRENGTH_DECIBELS_MILLIWATT
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.debounce import Debouncer as Debouncer
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from typing import Any

LIGHT_UPDATE_INTERVAL: int
REQUEST_REFRESH_DELAY: float
LIFX_IDENTIFY_DELAY: float
RSSI_DBM_FW: Incomplete

class FirmwareEffect(IntEnum):
    OFF: int
    MOVE: int
    MORPH: int
    FLAME: int

class LIFXUpdateCoordinator(DataUpdateCoordinator[None]):
    connection: Incomplete
    device: Incomplete
    lock: Incomplete
    active_effect: Incomplete
    _update_rssi: bool
    _rssi: int
    last_used_theme: str
    def __init__(self, hass: HomeAssistant, connection: LIFXConnection, title: str) -> None: ...
    def async_setup(self) -> None: ...
    @property
    def rssi(self) -> int: ...
    @property
    def rssi_uom(self) -> str: ...
    @property
    def current_infrared_brightness(self) -> str | None: ...
    @property
    def serial_number(self) -> str: ...
    @property
    def mac_address(self) -> str: ...
    @property
    def label(self) -> str: ...
    async def diagnostics(self) -> dict[str, Any]: ...
    def async_get_entity_id(self, platform: Platform, key: str) -> str | None: ...
    async def _async_populate_device_info(self) -> None: ...
    def get_number_of_zones(self) -> int: ...
    def _async_build_color_zones_update_requests(self) -> list[Callable]: ...
    async def _async_update_data(self) -> None: ...
    async def async_get_color_zones(self) -> None: ...
    async def async_get_extended_color_zones(self) -> None: ...
    async def async_set_waveform_optional(self, value: dict[str, Any], rapid: bool = ...) -> None: ...
    async def async_get_color(self) -> None: ...
    async def async_set_power(self, state: bool, duration: int | None) -> None: ...
    async def async_set_color(self, hsbk: list[float | int | None], duration: int | None) -> None: ...
    async def async_set_color_zones(self, start_index: int, end_index: int, hsbk: list[float | int | None], duration: int | None, apply: int) -> None: ...
    async def async_set_extended_color_zones(self, colors: list[tuple[int | float, int | float, int | float, int | float]], colors_count: int | None = ..., duration: int = ..., apply: int = ...) -> None: ...
    async def async_set_multizone_effect(self, effect: str, speed: float = ..., direction: str = ..., theme_name: str | None = ..., power_on: bool = ...) -> None: ...
    async def async_set_matrix_effect(self, effect: str, palette: list[tuple[int, int, int, int]] | None = ..., speed: float = ..., power_on: bool = ...) -> None: ...
    def async_get_active_effect(self) -> int: ...
    async def async_set_infrared_brightness(self, option: str) -> None: ...
    async def async_identify_bulb(self) -> None: ...
    def async_enable_rssi_updates(self) -> Callable[[], None]: ...
    def async_get_hev_cycle_state(self) -> bool | None: ...
    async def async_set_hev_cycle_state(self, enable: bool, duration: int = ...) -> None: ...
    async def async_apply_theme(self, theme_name: str) -> None: ...
