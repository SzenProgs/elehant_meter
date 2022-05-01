import voluptuous as vol
from homeassistant.config_entries import ConfigFlow
from .const import DOMAIN

class ElehantMeterFlowHandler(ConfigFlow, domain=DOMAIN):
	async def async_step_user(self, user_input=None):
		return self.async_show_form(step_id="user", data_schema=vol.Schema({vol.Required("password"): str}))