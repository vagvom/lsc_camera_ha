from .const import DOMAIN

async def async_setup_entry(hass, entry):
    hass.data.setdefault(DOMAIN, {})
    config = entry.data.copy()
    config["hass"] = hass
    hass.data[DOMAIN][entry.entry_id] = config

    await hass.config_entries.async_forward_entry_setup(entry, "camera")
    await hass.config_entries.async_forward_entry_setup(entry, "button")

    return True

async def async_unload_entry(hass, entry):
    await hass.config_entries.async_forward_entry_unload(entry, "camera")
    await hass.config_entries.async_forward_entry_unload(entry, "button")

    hass.data[DOMAIN].pop(entry.entry_id)
    return True
