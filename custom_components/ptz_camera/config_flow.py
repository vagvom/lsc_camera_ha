import voluptuous as vol
from homeassistant import config_entries

from .const import DOMAIN

class LSCConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        errors = {}

        if user_input is not None:
            return self.async_create_entry(
                title=user_input.get("device_name", "LSC Camera"),
                data=user_input
            )

        data_schema = vol.Schema({
            vol.Required("ip_address"): str,
            vol.Required("username"): str,
            vol.Required("password"): str,
            vol.Optional("device_name", default="LSC Camera"): str,
            vol.Optional("is_360", default=False): bool,
        })

        return self.async_show_form(step_id="user", data_schema=data_schema, errors=errors)         
