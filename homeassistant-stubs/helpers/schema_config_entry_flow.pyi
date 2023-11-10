import abc
import voluptuous as vol
from . import selector as selector
from .typing import UNDEFINED as UNDEFINED, UndefinedType as UndefinedType
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from collections.abc import Callable as Callable, Coroutine, Mapping
from dataclasses import dataclass
from homeassistant import config_entries as config_entries
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback, split_entity_id as split_entity_id
from homeassistant.data_entry_flow import FlowResult as FlowResult, UnknownHandler as UnknownHandler
from typing import Any

class SchemaFlowError(Exception): ...
@dataclass
class SchemaFlowStep: ...

@dataclass(slots=True)
class SchemaFlowFormStep(SchemaFlowStep):
    schema: vol.Schema | Callable[[SchemaCommonFlowHandler], Coroutine[Any, Any, vol.Schema | None]] | None = ...
    validate_user_input: Callable[[SchemaCommonFlowHandler, dict[str, Any]], Coroutine[Any, Any, dict[str, Any]]] | None = ...
    next_step: Callable[[dict[str, Any]], Coroutine[Any, Any, str | None]] | str | None = ...
    suggested_values: Callable[[SchemaCommonFlowHandler], Coroutine[Any, Any, dict[str, Any]]] | None | UndefinedType = ...
    preview: str | None = ...
    def __init__(self, schema, validate_user_input, next_step, suggested_values, preview) -> None: ...

@dataclass(slots=True)
class SchemaFlowMenuStep(SchemaFlowStep):
    options: list[str] | dict[str, str]
    def __init__(self, options) -> None: ...

class SchemaCommonFlowHandler:
    _flow: Incomplete
    _handler: Incomplete
    _options: Incomplete
    _flow_state: Incomplete
    def __init__(self, handler: SchemaConfigFlowHandler | SchemaOptionsFlowHandler, flow: Mapping[str, SchemaFlowStep], options: dict[str, Any] | None) -> None: ...
    @property
    def parent_handler(self) -> SchemaConfigFlowHandler | SchemaOptionsFlowHandler: ...
    @property
    def options(self) -> dict[str, Any]: ...
    @property
    def flow_state(self) -> dict[str, Any]: ...
    async def async_step(self, step_id: str, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def _get_schema(self, form_step: SchemaFlowFormStep) -> vol.Schema | None: ...
    async def _async_form_step(self, step_id: str, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    def _update_and_remove_omitted_optional_keys(self, values: dict[str, Any], user_input: dict[str, Any], data_schema: vol.Schema | None) -> None: ...
    async def _show_next_step_or_create_entry(self, form_step: SchemaFlowFormStep) -> FlowResult: ...
    async def _show_next_step(self, next_step_id: str, error: SchemaFlowError | None = ..., user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def _async_menu_step(self, step_id: str, user_input: dict[str, Any] | None = ...) -> FlowResult: ...

class SchemaConfigFlowHandler(config_entries.ConfigFlow, ABC, metaclass=abc.ABCMeta):
    config_flow: Mapping[str, SchemaFlowStep]
    options_flow: Mapping[str, SchemaFlowStep] | None
    VERSION: int
    def __init_subclass__(cls, **kwargs: Any) -> None: ...
    _common_handler: Incomplete
    def __init__(self) -> None: ...
    @staticmethod
    async def async_setup_preview(hass: HomeAssistant) -> None: ...
    @classmethod
    def async_supports_options_flow(cls, config_entry: config_entries.ConfigEntry) -> bool: ...
    @staticmethod
    def _async_step(step_id: str) -> Callable: ...
    @abstractmethod
    def async_config_entry_title(self, options: Mapping[str, Any]) -> str: ...
    def async_config_flow_finished(self, options: Mapping[str, Any]) -> None: ...
    @staticmethod
    def async_options_flow_finished(hass: HomeAssistant, options: Mapping[str, Any]) -> None: ...
    def async_create_entry(self, data: Mapping[str, Any], **kwargs: Any) -> FlowResult: ...

class SchemaOptionsFlowHandler(config_entries.OptionsFlowWithConfigEntry):
    _common_handler: Incomplete
    _async_options_flow_finished: Incomplete
    def __init__(self, config_entry: config_entries.ConfigEntry, options_flow: Mapping[str, SchemaFlowStep], async_options_flow_finished: Callable[[HomeAssistant, Mapping[str, Any]], None] | None = ..., async_setup_preview: Callable[[HomeAssistant], Coroutine[Any, Any, None]] | None = ...) -> None: ...
    @staticmethod
    def _async_step(step_id: str) -> Callable: ...
    def async_create_entry(self, data: Mapping[str, Any], **kwargs: Any) -> FlowResult: ...

def wrapped_entity_config_entry_title(hass: HomeAssistant, entity_id_or_uuid: str) -> str: ...
def entity_selector_without_own_entities(handler: SchemaOptionsFlowHandler, entity_selector_config: selector.EntitySelectorConfig) -> vol.Schema: ...
