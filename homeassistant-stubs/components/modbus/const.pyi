from _typeshed import Incomplete
from enum import Enum
from homeassistant.const import CONF_ADDRESS as CONF_ADDRESS, CONF_BINARY_SENSORS as CONF_BINARY_SENSORS, CONF_COVERS as CONF_COVERS, CONF_LIGHTS as CONF_LIGHTS, CONF_SENSORS as CONF_SENSORS, CONF_SWITCHES as CONF_SWITCHES, Platform as Platform

CONF_BAUDRATE: str
CONF_BYTESIZE: str
CONF_CLIMATES: str
CONF_CLOSE_COMM_ON_ERROR: str
CONF_DATA_TYPE: str
CONF_FANS: str
CONF_INPUT_TYPE: str
CONF_LAZY_ERROR: str
CONF_MAX_TEMP: str
CONF_MAX_VALUE: str
CONF_MIN_TEMP: str
CONF_MIN_VALUE: str
CONF_MSG_WAIT: str
CONF_NAN_VALUE: str
CONF_PARITY: str
CONF_RETRIES: str
CONF_RETRY_ON_EMPTY: str
CONF_PRECISION: str
CONF_SCALE: str
CONF_SLAVE_COUNT: str
CONF_STATE_CLOSED: str
CONF_STATE_CLOSING: str
CONF_STATE_OFF: str
CONF_STATE_ON: str
CONF_STATE_OPEN: str
CONF_STATE_OPENING: str
CONF_STATUS_REGISTER: str
CONF_STATUS_REGISTER_TYPE: str
CONF_STEP: str
CONF_STOPBITS: str
CONF_SWAP: str
CONF_SWAP_BYTE: str
CONF_SWAP_NONE: str
CONF_SWAP_WORD: str
CONF_SWAP_WORD_BYTE: str
CONF_TARGET_TEMP: str
CONF_TARGET_TEMP_WRITE_REGISTERS: str
CONF_HVAC_MODE_REGISTER: str
CONF_HVAC_MODE_VALUES: str
CONF_HVAC_ONOFF_REGISTER: str
CONF_HVAC_MODE_OFF: str
CONF_HVAC_MODE_HEAT: str
CONF_HVAC_MODE_COOL: str
CONF_HVAC_MODE_HEAT_COOL: str
CONF_HVAC_MODE_AUTO: str
CONF_HVAC_MODE_DRY: str
CONF_HVAC_MODE_FAN_ONLY: str
CONF_WRITE_REGISTERS: str
CONF_VERIFY: str
CONF_WRITE_TYPE: str
CONF_ZERO_SUPPRESS: str
RTUOVERTCP: str
SERIAL: str
TCP: str
UDP: str
ATTR_ADDRESS = CONF_ADDRESS
ATTR_HUB: str
ATTR_UNIT: str
ATTR_SLAVE: str
ATTR_VALUE: str

class DataType(str, Enum):
    CUSTOM: str
    STRING: str
    INT8: str
    INT16: str
    INT32: str
    INT64: str
    UINT8: str
    UINT16: str
    UINT32: str
    UINT64: str
    FLOAT16: str
    FLOAT32: str
    FLOAT64: str

CALL_TYPE_COIL: str
CALL_TYPE_DISCRETE: str
CALL_TYPE_REGISTER_HOLDING: str
CALL_TYPE_REGISTER_INPUT: str
CALL_TYPE_WRITE_COIL: str
CALL_TYPE_WRITE_COILS: str
CALL_TYPE_WRITE_REGISTER: str
CALL_TYPE_WRITE_REGISTERS: str
CALL_TYPE_X_COILS: str
CALL_TYPE_X_REGISTER_HOLDINGS: str
SERVICE_WRITE_COIL: str
SERVICE_WRITE_REGISTER: str
SERVICE_STOP: str
SERVICE_RESTART: str
SIGNAL_STOP_ENTITY: str
SIGNAL_START_ENTITY: str
DEFAULT_HUB: str
DEFAULT_SCAN_INTERVAL: int
DEFAULT_SLAVE: int
DEFAULT_STRUCTURE_PREFIX: str
DEFAULT_TEMP_UNIT: str
MODBUS_DOMAIN: str
ACTIVE_SCAN_INTERVAL: int
PLATFORMS: Incomplete
