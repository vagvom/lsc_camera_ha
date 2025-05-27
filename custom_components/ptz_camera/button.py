from homeassistant.components.button import ButtonEntity
from requests.auth import HTTPBasicAuth
import requests
import datetime
import telnetlib
import time
import re
import asyncio

from .const import DOMAIN

def slugify(text: str) -> str:
    return re.sub(r'[^a-z0-9]+', '_', text.lower()).strip('_')

class LscSyncTimeButton(ButtonEntity):
    def __init__(self, config):
        self._config = config
        self._device_name = config.get("device_name", config["ip_address"])
        self._device_slug = slugify(self._device_name)

        self._attr_name = f"{self._device_name} Sync Time"
        self._attr_unique_id = f"{self._device_slug}_sync_time"
        self.entity_id = f"button.{self._device_slug}_sync_time"
        self._attr_icon = "mdi:timer-sync-outline"

    @property
    def device_info(self):
        return {
            "identifiers": {(DOMAIN, self._config["ip_address"])},
            "name": self._device_name,
            "manufacturer": "LSC",
            "model": "Caméra IP",
            "connections": {("ipv4", self._config["ip_address"])},
        }

    def press(self) -> None:
        try:
            HOST = self._config["ip_address"]
            PORT = 24
            PROMPT = b"$"
            now = datetime.datetime.now()
            cmd = f'date -s "{now.strftime("%Y-%m-%d %H:%M:%S")}"\n'

            tn = telnetlib.Telnet(HOST, PORT, timeout=3)
            tn.read_until(PROMPT, timeout=3)
            tn.write(cmd.encode('ascii'))
            time.sleep(1)
            tn.write(b"exit\n")
            time.sleep(1)
            tn.close()
        except Exception:
            pass

class LscMoveButton(ButtonEntity):
    def __init__(self, config, direction):
        self._config = config
        self._direction = direction
        self._device_name = config.get("device_name", config["ip_address"])
        self._device_slug = slugify(self._device_name)

        self._attr_name = f"{self._device_name} Move {self._direction.capitalize()}"
        self._attr_unique_id = f"{self._device_slug}_move_{direction}"
        self.entity_id = f"button.{self._device_slug}_move_{direction}"

        self._attr_icon = {
            "up": "mdi:arrow-up",
            "down": "mdi:arrow-down",
            "left": "mdi:arrow-left",
            "right": "mdi:arrow-right"
        }.get(direction, "mdi:arrow-right")

    @property
    def device_info(self):
        return {
            "identifiers": {(DOMAIN, self._config["ip_address"])},
            "name": self._device_name,
            "manufacturer": "LSC",
            "model": "Caméra IP",
            "connections": {("ipv4", self._config["ip_address"])},
        }

    def press(self) -> None:
        try:
            ip = self._config["ip_address"]
            username = self._config.get("username", "")
            password = self._config.get("password", "")
            url = f"http://{ip}:8080/cgi-bin/motor.cgi?dir={self._direction}&dist=10"
            response = requests.get(url, auth=HTTPBasicAuth(username, password), timeout=5)
            response.raise_for_status()
        except Exception:
            pass

class LscTelnetToggleButton(ButtonEntity):
    def __init__(self, config):
        self._config = config
        self._device_name = config.get("device_name", config["ip_address"])
        self._device_slug = slugify(self._device_name)

        self._attr_name = f"{self._device_name} Telnet On/Off"
        self._attr_unique_id = f"{self._device_slug}_telnet_toggle"
        self.entity_id = f"button.{self._device_slug}_telnet_toggle"
        self._attr_icon = "mdi:toggle-switch"

        self._telnet_enabled = False

    @property
    def device_info(self):
        return {
            "identifiers": {(DOMAIN, self._config["ip_address"])},
            "name": self._device_name,
            "manufacturer": "LSC",
            "model": "Caméra IP",
            "connections": {("ipv4", self._config["ip_address"])},
        }

    async def async_added_to_hass(self):
        await self.async_update_telnet_status()

    async def async_update_telnet_status(self):
        ip = self._config["ip_address"]
        port = 24
        try:
            reader, writer = await asyncio.wait_for(
                asyncio.open_connection(ip, port),
                timeout=3
            )
            writer.close()
            await writer.wait_closed()
            self._telnet_enabled = True
        except Exception:
            self._telnet_enabled = False
        self.async_write_ha_state()

    async def async_press(self) -> None:
        ip = self._config["ip_address"]
        username = self._config.get("username", "")
        password = self._config.get("password", "")

        if self._telnet_enabled:
            url = f"http://{ip}:8080/cgi-bin/telnetoff.cgi"
        else:
            url = f"http://{ip}:8080/cgi-bin/telneton.cgi"

        try:
            session = self._config["hass"].helpers.aiohttp_client.async_get_clientsession()
            resp = await session.get(url, auth=HTTPBasicAuth(username, password), timeout=5)
            resp.raise_for_status()
        except Exception:
            return

        await asyncio.sleep(1)
        await self.async_update_telnet_status()

    @property
    def is_on(self) -> bool:
        return self._telnet_enabled

async def async_setup_entry(hass, entry, async_add_entities):
    config = hass.data[DOMAIN][entry.entry_id]
    config["hass"] = hass

    entities = [LscSyncTimeButton(config), LscTelnetToggleButton(config)]

    if config.get("is_360", False):
        for direction in ["up", "down", "left", "right"]:
            entities.append(LscMoveButton(config, direction))

    async_add_entities(entities)
