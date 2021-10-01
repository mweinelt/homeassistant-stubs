from typing import Any, NamedTuple

class RGBColor(NamedTuple):
    r: int
    g: int
    b: int

COLORS: Any

class XYPoint:
    x: float
    y: float
    def __init__(self, x, y) -> None: ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...

class GamutType:
    red: XYPoint
    green: XYPoint
    blue: XYPoint
    def __init__(self, red, green, blue) -> None: ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...

def color_name_to_rgb(color_name: str) -> RGBColor: ...
def color_RGB_to_xy(iR: int, iG: int, iB: int, Gamut: Union[GamutType, None] = ...) -> tuple[float, float]: ...
def color_RGB_to_xy_brightness(iR: int, iG: int, iB: int, Gamut: Union[GamutType, None] = ...) -> tuple[float, float, int]: ...
def color_xy_to_RGB(vX: float, vY: float, Gamut: Union[GamutType, None] = ...) -> tuple[int, int, int]: ...
def color_xy_brightness_to_RGB(vX: float, vY: float, ibrightness: int, Gamut: Union[GamutType, None] = ...) -> tuple[int, int, int]: ...
def color_hsb_to_RGB(fH: float, fS: float, fB: float) -> tuple[int, int, int]: ...
def color_RGB_to_hsv(iR: float, iG: float, iB: float) -> tuple[float, float, float]: ...
def color_RGB_to_hs(iR: float, iG: float, iB: float) -> tuple[float, float]: ...
def color_hsv_to_RGB(iH: float, iS: float, iV: float) -> tuple[int, int, int]: ...
def color_hs_to_RGB(iH: float, iS: float) -> tuple[int, int, int]: ...
def color_xy_to_hs(vX: float, vY: float, Gamut: Union[GamutType, None] = ...) -> tuple[float, float]: ...
def color_hs_to_xy(iH: float, iS: float, Gamut: Union[GamutType, None] = ...) -> tuple[float, float]: ...
def _match_max_scale(input_colors: tuple[int, ...], output_colors: tuple[int, ...]) -> tuple[int, ...]: ...
def color_rgb_to_rgbw(r: int, g: int, b: int) -> tuple[int, int, int, int]: ...
def color_rgbw_to_rgb(r: int, g: int, b: int, w: int) -> tuple[int, int, int]: ...
def color_rgb_to_rgbww(r: int, g: int, b: int, min_mireds: int, max_mireds: int) -> tuple[int, int, int, int, int]: ...
def color_rgbww_to_rgb(r: int, g: int, b: int, cw: int, ww: int, min_mireds: int, max_mireds: int) -> tuple[int, int, int]: ...
def color_rgb_to_hex(r: int, g: int, b: int) -> str: ...
def rgb_hex_to_rgb_list(hex_string: str) -> list[int]: ...
def color_temperature_to_hs(color_temperature_kelvin: float) -> tuple[float, float]: ...
def color_temperature_to_rgb(color_temperature_kelvin: float) -> tuple[float, float, float]: ...
def _clamp(color_component: float, minimum: float = ..., maximum: float = ...) -> float: ...
def _get_red(temperature: float) -> float: ...
def _get_green(temperature: float) -> float: ...
def _get_blue(temperature: float) -> float: ...
def color_temperature_mired_to_kelvin(mired_temperature: float) -> int: ...
def color_temperature_kelvin_to_mired(kelvin_temperature: float) -> int: ...
def cross_product(p1: XYPoint, p2: XYPoint) -> float: ...
def get_distance_between_two_points(one: XYPoint, two: XYPoint) -> float: ...
def get_closest_point_to_line(A: XYPoint, B: XYPoint, P: XYPoint) -> XYPoint: ...
def get_closest_point_to_point(xy_tuple: tuple[float, float], Gamut: GamutType) -> tuple[float, float]: ...
def check_point_in_lamps_reach(p: tuple[float, float], Gamut: GamutType) -> bool: ...
def check_valid_gamut(Gamut: GamutType) -> bool: ...
