from homeassistant.components.camera import Camera, CameraEntityFeature
from homeassistant.components.ffmpeg import DATA_FFMPEG
from homeassistant.helpers.aiohttp_client import async_aiohttp_proxy_stream
from .const import DOMAIN

class LSCCamera(Camera):
    def __init__(self, config):
        super().__init__()
        self._config = config
        self._hass = config["hass"]

        ip = self._config["ip_address"]
        self._rtsp_url = f"rtsp://{ip}/main_ch"
        self._ffmpeg = self._hass.data[DATA_FFMPEG]

        self._attr_name = self._config.get("device_name", f"LSC Camera {ip}")
        self._attr_supported_features = CameraEntityFeature.STREAM
        self._attr_should_poll = False
        self._attr_icon = "mdi:cctv"

    @property
    def unique_id(self):
        return f"lsc_camera_{self._config['ip_address']}"

    @property
    def device_info(self):
        return {
            "identifiers": {(DOMAIN, self._config["ip_address"])},
            "name": self._config.get("device_name", f"LSC Camera {self._config['ip_address']}"),
            "manufacturer": "LSC",
            "model": "Caméra IP",
            "connections": {("ipv4", self._config["ip_address"])},
        }

    async def stream_source(self):
        return self._rtsp_url

    async def handle_async_mjpeg_stream(self, request):
        stream = self._ffmpeg.create_ffmpeg_streamer()
        await stream.open_camera(self._rtsp_url)
        try:
            stream_reader = await stream.get_reader()
            return await async_aiohttp_proxy_stream(
                self._hass,
                request,
                stream_reader,
                "multipart/x-mixed-replace; boundary=ffserver"
            )
        finally:
            await stream.close()

async def async_setup_entry(hass, entry, async_add_entities):
    config = hass.data[DOMAIN][entry.entry_id]
    config["hass"] = hass

    entities = [LSCCamera(config)]

    async_add_entities(entities)
