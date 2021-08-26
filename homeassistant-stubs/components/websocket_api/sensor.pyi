from .const import DATA_CONNECTIONS as DATA_CONNECTIONS, SIGNAL_WEBSOCKET_CONNECTED as SIGNAL_WEBSOCKET_CONNECTED, SIGNAL_WEBSOCKET_DISCONNECTED as SIGNAL_WEBSOCKET_DISCONNECTED
from homeassistant.components.sensor import SensorEntity as SensorEntity
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: Union[dict[str, Any], None] = ...) -> None: ...

class APICount(SensorEntity):
    count: int
    def __init__(self) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def native_value(self) -> int: ...
    @property
    def native_unit_of_measurement(self) -> str: ...
    def _update_count(self) -> None: ...
