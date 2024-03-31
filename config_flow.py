from typing import Any, Dict, Optional

from homeassistant import config_entries, core
from homeassistant.core import callback
from .const import (
    DOMAIN,
    CONF_NAME,
    CONF_SUNRISE_TIME,
    CONF_SUNSET_TIME,
    CONF_SUNRISE_OFFSET,
    CONF_SUNSET_OFFSET,
)

import voluptuous as vol
import homeassistant.helpers.config_validation as cv

OPTIONS_SCHEMA = vol.Schema(
    {
        vol.Optional(CONF_SUNRISE_TIME): cv.string,
        vol.Optional(CONF_SUNRISE_OFFSET): int,
        vol.Optional(CONF_SUNSET_TIME): cv.string,
        vol.Optional(CONF_SUNSET_OFFSET): int,
        # vol.Optional(CONF_NAME): cv.string,
        # vol.Optional("add_another"): cv.boolean,
    }
)


class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Config flow."""

    # The schema version of the entries that it creates
    # Home Assistant will call your migrate method if the version changes
    VERSION = 1
    MINOR_VERSION = 1

    async def async_step_user(self, user_input: Optional[Dict[str, Any]] = None):
        if user_input is not None:
            # try:
            #     #todo: validate name (maybe)
            # except ValueError:
            #     error["base"] = "name";
            self.data = user_input
            return self.async_create_entry(title=self.data[CONF_NAME], data=self.data)

        return self.async_show_form(
            step_id="user", data_schema=vol.Schema({vol.Required(CONF_NAME): cv.string})
        )

    async def async_step_options(self, user_input: Optional[Dict[str, Any]] = None):
        errors: Dict[str, str] = {}
        if user_input is not None:
            # todo error handling
            self.data.update(user_input)
            return self.async_create_entry(title=self.data[CONF_NAME], data=self.data)

        return self.async_show_form(
            step_id="options", data_schema=OPTIONS_SCHEMA, errors=errors
        )

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        """Get the options flow for this handler."""
        return OptionsFlowHandler(config_entry)


class OptionsFlowHandler(config_entries.OptionsFlow):
    """Handles options flow for the component."""

    def __init__(self, config_entry: config_entries.ConfigEntry) -> None:
        self.config_entry = config_entry
