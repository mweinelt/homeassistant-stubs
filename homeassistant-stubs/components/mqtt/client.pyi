import paho.mqtt.client as mqtt
from .const import ATTR_TOPIC as ATTR_TOPIC, CONF_BIRTH_MESSAGE as CONF_BIRTH_MESSAGE, CONF_BROKER as CONF_BROKER, CONF_CERTIFICATE as CONF_CERTIFICATE, CONF_CLIENT_CERT as CONF_CLIENT_CERT, CONF_CLIENT_KEY as CONF_CLIENT_KEY, CONF_KEEPALIVE as CONF_KEEPALIVE, CONF_TLS_INSECURE as CONF_TLS_INSECURE, CONF_TRANSPORT as CONF_TRANSPORT, CONF_WILL_MESSAGE as CONF_WILL_MESSAGE, CONF_WS_HEADERS as CONF_WS_HEADERS, CONF_WS_PATH as CONF_WS_PATH, DEFAULT_ENCODING as DEFAULT_ENCODING, DEFAULT_PROTOCOL as DEFAULT_PROTOCOL, DEFAULT_QOS as DEFAULT_QOS, DEFAULT_TRANSPORT as DEFAULT_TRANSPORT, MQTT_CONNECTED as MQTT_CONNECTED, MQTT_DISCONNECTED as MQTT_DISCONNECTED, PROTOCOL_31 as PROTOCOL_31, PROTOCOL_5 as PROTOCOL_5, TRANSPORT_WEBSOCKETS as TRANSPORT_WEBSOCKETS
from .models import AsyncMessageCallbackType as AsyncMessageCallbackType, MessageCallbackType as MessageCallbackType, PublishMessage as PublishMessage, PublishPayloadType as PublishPayloadType, ReceiveMessage as ReceiveMessage
from .util import get_file_path as get_file_path, get_mqtt_data as get_mqtt_data, mqtt_config_entry_enabled as mqtt_config_entry_enabled
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine, Iterable
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_CLIENT_ID as CONF_CLIENT_ID, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, CONF_PROTOCOL as CONF_PROTOCOL, CONF_USERNAME as CONF_USERNAME, EVENT_HOMEASSISTANT_STARTED as EVENT_HOMEASSISTANT_STARTED, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, CoreState as CoreState, Event as Event, HassJob as HassJob, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.dispatcher import dispatcher_send as dispatcher_send
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.loader import bind_hass as bind_hass
from homeassistant.util.async_ import run_callback_threadsafe as run_callback_threadsafe
from homeassistant.util.logging import catch_log_exception as catch_log_exception
from typing import Any

_LOGGER: Incomplete
DISCOVERY_COOLDOWN: int
TIMEOUT_ACK: int
SubscribePayloadType: Incomplete

def publish(hass: HomeAssistant, topic: str, payload: PublishPayloadType, qos: Union[int, None] = ..., retain: Union[bool, None] = ..., encoding: Union[str, None] = ...) -> None: ...
async def async_publish(hass: HomeAssistant, topic: str, payload: PublishPayloadType, qos: Union[int, None] = ..., retain: Union[bool, None] = ..., encoding: Union[str, None] = ...) -> None: ...
async def async_subscribe(hass: HomeAssistant, topic: str, msg_callback: Union[AsyncMessageCallbackType, MessageCallbackType], qos: int = ..., encoding: Union[str, None] = ...) -> CALLBACK_TYPE: ...
def subscribe(hass: HomeAssistant, topic: str, msg_callback: MessageCallbackType, qos: int = ..., encoding: str = ...) -> Callable[[], None]: ...

class Subscription:
    topic: str
    matcher: Any
    job: HassJob[[ReceiveMessage], Union[Coroutine[Any, Any, None], None]]
    qos: int
    encoding: Union[str, None]
    def __init__(self, topic, matcher, job, qos, encoding) -> None: ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...

class MqttClientSetup:
    _client: Incomplete
    def __init__(self, config: ConfigType) -> None: ...
    @property
    def client(self) -> mqtt.Client: ...

def _is_simple_match(topic: str) -> bool: ...

class MQTT:
    _mqttc: mqtt.Client
    _mqtt_data: Incomplete
    hass: Incomplete
    config_entry: Incomplete
    conf: Incomplete
    _simple_subscriptions: Incomplete
    _wildcard_subscriptions: Incomplete
    connected: bool
    _ha_started: Incomplete
    _last_subscribe: Incomplete
    _cleanup_on_unload: Incomplete
    _paho_lock: Incomplete
    _pending_operations: Incomplete
    _pending_operations_condition: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: ConfigEntry, conf: ConfigType) -> None: ...
    @property
    def subscriptions(self) -> list[Subscription]: ...
    def cleanup(self) -> None: ...
    def init_client(self) -> None: ...
    def _is_active_subscription(self, topic: str) -> bool: ...
    async def async_publish(self, topic: str, payload: PublishPayloadType, qos: int, retain: bool) -> None: ...
    async def async_connect(self) -> None: ...
    async def async_disconnect(self) -> None: ...
    def async_restore_tracked_subscriptions(self, subscriptions: list[Subscription]) -> None: ...
    def _async_track_subscription(self, subscription: Subscription) -> None: ...
    def _async_untrack_subscription(self, subscription: Subscription) -> None: ...
    async def async_subscribe(self, topic: str, msg_callback: Union[AsyncMessageCallbackType, MessageCallbackType], qos: int, encoding: Union[str, None] = ...) -> Callable[[], None]: ...
    async def _async_unsubscribe(self, topic: str) -> None: ...
    async def _async_perform_subscriptions(self, subscriptions: Iterable[tuple[str, int]]) -> None: ...
    def _mqtt_on_connect(self, _mqttc: mqtt.Client, _userdata: None, _flags: dict[str, int], result_code: int, properties: Union[mqtt.Properties, None] = ...) -> None: ...
    async def _async_resubscribe(self) -> None: ...
    def _mqtt_on_message(self, _mqttc: mqtt.Client, _userdata: None, msg: mqtt.MQTTMessage) -> None: ...
    def _matching_subscriptions(self, topic: str) -> list[Subscription]: ...
    def _mqtt_handle_message(self, msg: mqtt.MQTTMessage) -> None: ...
    def _mqtt_on_callback(self, _mqttc: mqtt.Client, _userdata: None, mid: int, _granted_qos_reason: Union[tuple[int, ...], mqtt.ReasonCodes, None] = ..., _properties_reason: Union[mqtt.ReasonCodes, None] = ...) -> None: ...
    async def _mqtt_handle_mid(self, mid: int) -> None: ...
    async def _register_mid(self, mid: int) -> None: ...
    def _mqtt_on_disconnect(self, _mqttc: mqtt.Client, _userdata: None, result_code: int, properties: Union[mqtt.Properties, None] = ...) -> None: ...
    async def _wait_for_mid(self, mid: int) -> None: ...
    async def _discovery_cooldown(self) -> None: ...

def _raise_on_errors(result_codes: Iterable[int]) -> None: ...
def _raise_on_error(result_code: int) -> None: ...
def _matcher_for_topic(subscription: str) -> Any: ...
