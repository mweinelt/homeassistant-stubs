from . import ATTR_IN_PROGRESS as ATTR_IN_PROGRESS, ATTR_RELEASE_SUMMARY as ATTR_RELEASE_SUMMARY
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback

def exclude_attributes(hass: HomeAssistant) -> set[str]: ...
