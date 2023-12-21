from __future__ import annotations

import logging

import voluptuous as vol
import homeassistant.helpers.config_validation as cv

# from collections.abc import Callable
# from dataclasses import dataclass

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_NAME

from homeassistant.components.switch import PLATFORM_SCHEMA, SwitchEntity

from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

DEFAULT_NAME = "Adaptive Shutters"

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Optional(CONF_NAME, default=DEFAULT_NAME): cv.string,
    }
)


async def async_setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None,
) -> None:
    """Set up the sensor platform."""

    add_entities([AdaptiveSwitch(hass, config)], True)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Example sensor based on a config entry."""
    async_setup_platform(hass, entry)


class AdaptiveSwitch(SwitchEntity):
    _attr_has_entity_name = True
    _attr_name = None

    def __init__(self, hass: HomeAssistant, config_entry: ConfigEntry) -> None:
        self._is_on = False
        self._attr_device_info = ...  # For automatic device registration
        self._attr_unique_id = ...

        self.hass = hass
        self._name = config_entry[CONF_NAME]

    @property
    def is_on(self):
        """If the switch is currently on or off."""
        return self._is_on

    def turn_on(self, **kwargs):
        """Turn the switch on."""
        self._is_on = True

    def turn_off(self, **kwargs):
        """Turn the switch off."""
        self._is_on = False

    @property
    def icon(self) -> str | None:
        """Icon of the entity."""
        return "mdi:window-shutter-auto"

    @property
    def name(self):
        """Name of the entity."""
        return self._name


    def update(self) -> None:
        """Synchronize state with switch."""
        # self.hass.states.set(STATE_ENTITY_ID, self._state)

#    def validate( config_entry: ConfigEntry | None)
