from .const import CONF_ROUND_DIGITS as CONF_ROUND_DIGITS, CONF_TIME_WINDOW as CONF_TIME_WINDOW, CONF_UNIT_PREFIX as CONF_UNIT_PREFIX, CONF_UNIT_TIME as CONF_UNIT_TIME, DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.const import CONF_NAME as CONF_NAME, CONF_SOURCE as CONF_SOURCE, TIME_DAYS as TIME_DAYS, TIME_HOURS as TIME_HOURS, TIME_MINUTES as TIME_MINUTES, TIME_SECONDS as TIME_SECONDS
from homeassistant.helpers import selector as selector
from homeassistant.helpers.schema_config_entry_flow import SchemaConfigFlowHandler as SchemaConfigFlowHandler, SchemaFlowFormStep as SchemaFlowFormStep
from typing import Any

UNIT_PREFIXES: Incomplete
TIME_UNITS: Incomplete
OPTIONS_SCHEMA: Incomplete
CONFIG_SCHEMA: Incomplete
CONFIG_FLOW: Incomplete
OPTIONS_FLOW: Incomplete

class ConfigFlowHandler(SchemaConfigFlowHandler):
    config_flow: Incomplete
    options_flow: Incomplete
    def async_config_entry_title(self, options: Mapping[str, Any]) -> str: ...
