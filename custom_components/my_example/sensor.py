
from __future__ import annotations
from datetime import timedelta
import logging

from homeassistant.components.sensor import SensorEntity
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import (
    DataUpdateCoordinator,
    UpdateFailed,
)
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.config_entries import ConfigEntry

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)
SCAN_INTERVAL = timedelta(seconds=30)  # or use a coordinator

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities):
    """Set up sensor entities from a config entry."""
    coordinator = DataUpdateCoordinator(
        hass,
        _LOGGER,
        name="my_example_coordinator",
        update_method=_async_update_data,
        update_interval=SCAN_INTERVAL,
    )
    await coordinator.async_config_entry_first_refresh()

    async_add_entities([MyExampleSensor(coordinator, entry)])

async def _async_update_data():
    """Fetch data (replace with actual I/O)."""
    try:
        # Example: return a dict or value from API/IO
        return {"value": 42}
    except Exception as err:
        raise UpdateFailed(f"Update failed: {err}") from err

class MyExampleSensor(SensorEntity):
    _attr_name = "My Example Value"
    _attr_icon = "mdi:counter"

    def __init__(self, coordinator: DataUpdateCoordinator, entry: ConfigEntry):
        self.coordinator = coordinator
        self._attr_unique_id = f"{entry.entry_id}_value"
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, entry.entry_id)},
            name="My Example Device",
            manufacturer="YourName",
            model="ExampleModel",
        )

    @property
    def native_value(self):
        return self.coordinator.data.get("value")

    async def async_update(self):
        await self.coordinator.async_request_refresh()

    @property
    def available(self) -> bool:
        return self.coordinator.last_update_success
