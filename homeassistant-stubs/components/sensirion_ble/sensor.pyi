from .const import DOMAIN as DOMAIN
from homeassistant import config_entries as config_entries, const as const
from homeassistant.components.bluetooth.passive_update_processor import PassiveBluetoothDataProcessor as PassiveBluetoothDataProcessor, PassiveBluetoothDataUpdate as PassiveBluetoothDataUpdate, PassiveBluetoothEntityKey as PassiveBluetoothEntityKey, PassiveBluetoothProcessorCoordinator as PassiveBluetoothProcessorCoordinator, PassiveBluetoothProcessorEntity as PassiveBluetoothProcessorEntity
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.sensor import sensor_device_info_to_hass_device_info as sensor_device_info_to_hass_device_info
from sensor_state_data import DeviceKey as DeviceKey, SensorDescription as SensorDescription, SensorDeviceClass as SSDSensorDeviceClass, SensorUpdate as SensorUpdate, Units
from typing import Optional, Union

SENSOR_DESCRIPTIONS: dict[tuple[SSDSensorDeviceClass, Union[Units, None]], SensorEntityDescription]

def _device_key_to_bluetooth_entity_key(device_key: DeviceKey) -> PassiveBluetoothEntityKey: ...
def _to_sensor_key(description: SensorDescription) -> tuple[SSDSensorDeviceClass, Union[Units, None]]: ...
def sensor_update_to_bluetooth_data_update(sensor_update: SensorUpdate) -> PassiveBluetoothDataUpdate: ...
async def async_setup_entry(hass: HomeAssistant, entry: config_entries.ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SensirionBluetoothSensorEntity(PassiveBluetoothProcessorEntity[PassiveBluetoothDataProcessor[Optional[Union[float, int]]]], SensorEntity):
    @property
    def native_value(self) -> Union[int, float, None]: ...
