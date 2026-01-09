
from __future__ import annotations
import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import HomeAssistant
from .const import DOMAIN

DATA_SCHEMA = vol.Schema({
    vol.Required("name", default="My Example"): str,
})

class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for My Example."""

    async def async_step_user(self, user_input=None):
        if user_input is None:
            return self.async_show_form(step_id="user", data_schema=DATA_SCHEMA)

        # Validate input (e.g., connectivity) here if needed
        return self.async_create_entry(title=user_input["name"], data=user_input)
