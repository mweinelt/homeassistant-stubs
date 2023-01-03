import voluptuous as vol
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Iterable
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, ATTR_SUPPORTED_FEATURES as ATTR_SUPPORTED_FEATURES
from homeassistant.core import Context as Context, HomeAssistant as HomeAssistant, State as State, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.loader import bind_hass as bind_hass
from typing import Any, TypeVar

_LOGGER: Incomplete
_SlotsType = dict[str, Any]
_T = TypeVar('_T')
INTENT_TURN_OFF: str
INTENT_TURN_ON: str
INTENT_TOGGLE: str
SLOT_SCHEMA: Incomplete
DATA_KEY: str
SPEECH_TYPE_PLAIN: str
SPEECH_TYPE_SSML: str

def async_register(hass: HomeAssistant, handler: IntentHandler) -> None: ...
async def async_handle(hass: HomeAssistant, platform: str, intent_type: str, slots: Union[_SlotsType, None] = ..., text_input: Union[str, None] = ..., context: Union[Context, None] = ...) -> IntentResponse: ...

class IntentError(HomeAssistantError): ...
class UnknownIntent(IntentError): ...
class InvalidSlotInfo(IntentError): ...
class IntentHandleError(IntentError): ...
class IntentUnexpectedError(IntentError): ...

def async_match_state(hass: HomeAssistant, name: str, states: Union[Iterable[State], None] = ...) -> State: ...
def async_test_feature(state: State, feature: int, feature_name: str) -> None: ...

class IntentHandler:
    intent_type: Union[str, None]
    slot_schema: Union[vol.Schema, None]
    _slot_schema: Union[vol.Schema, None]
    platforms: Union[Iterable[str], None]
    def async_can_handle(self, intent_obj: Intent) -> bool: ...
    def async_validate_slots(self, slots: _SlotsType) -> _SlotsType: ...
    async def async_handle(self, intent_obj: Intent) -> IntentResponse: ...
    def __repr__(self) -> str: ...

def _fuzzymatch(name: str, items: Iterable[_T], key: Callable[[_T], str]) -> Union[_T, None]: ...

class ServiceIntentHandler(IntentHandler):
    slot_schema: Incomplete
    intent_type: Incomplete
    domain: Incomplete
    service: Incomplete
    speech: Incomplete
    def __init__(self, intent_type: str, domain: str, service: str, speech: str) -> None: ...
    async def async_handle(self, intent_obj: Intent) -> IntentResponse: ...

class Intent:
    __slots__: Incomplete
    hass: Incomplete
    platform: Incomplete
    intent_type: Incomplete
    slots: Incomplete
    text_input: Incomplete
    context: Incomplete
    def __init__(self, hass: HomeAssistant, platform: str, intent_type: str, slots: _SlotsType, text_input: Union[str, None], context: Context) -> None: ...
    def create_response(self) -> IntentResponse: ...

class IntentResponse:
    intent: Incomplete
    speech: Incomplete
    reprompt: Incomplete
    card: Incomplete
    def __init__(self, intent: Union[Intent, None] = ...) -> None: ...
    def async_set_speech(self, speech: str, speech_type: str = ..., extra_data: Union[Any, None] = ...) -> None: ...
    def async_set_reprompt(self, speech: str, speech_type: str = ..., extra_data: Union[Any, None] = ...) -> None: ...
    def async_set_card(self, title: str, content: str, card_type: str = ...) -> None: ...
    def as_dict(self) -> dict[str, dict[str, dict[str, Any]]]: ...
