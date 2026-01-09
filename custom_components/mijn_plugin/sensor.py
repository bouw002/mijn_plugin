from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import DiscoveryInfoType

async def async_setup_platform(
    hass: HomeAssistant,
    config: dict,
    async_add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None,
) -> None:
    async_add_entities([MijnSensor()])

class MijnSensor(SensorEntity):
    _attr_name = "Mijn Plugin Sensor"
    _attr_unit_of_measurement = "°C"

    def __init__(self):
        self._attr_native_value = 21.5

    async def async_update(self):
        # Hier kun je later echte data ophalen
        self._attr_native_value = 21.5