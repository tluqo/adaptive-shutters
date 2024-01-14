"""Adaptive Shutters integration in Home-Assistant."""
from __future__ import annotations

from typing import Any

from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType
from homeassistant.config_entries import SOURCE_IMPORT, ConfigEntry
from homeassistant.const import CONF_SOURCE
from .const import DOMAIN

PLATFORMS = ["switch"]


def setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Your controller/hub specific code."""

    return True


async def reload_configuration_yaml(event: dict, hass: HomeAssistant):  # noqa: ARG001
    """Reload configuration.yaml."""
    await hass.services.async_call("homeassistant", "check_config", {})


async def async_setup(hass: HomeAssistant, config: dict[str, Any]):
    """Import integration from config."""
    if DOMAIN in config:
        for entry in config[DOMAIN]:
            hass.async_create_task(
                hass.config_entries.flow.async_init(
                    DOMAIN,
                    context={CONF_SOURCE: SOURCE_IMPORT},
                    data=entry,
                ),
            )
    return True


async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool:
    """Set up the component."""
    # data = hass.data.setdefault(DOMAIN, {})

    # This will reload any changes the user made to any YAML configurations.
    # Called during 'quick reload' or hass.reload_config_entry
    hass.bus.async_listen("hass.config.entry_updated", reload_configuration_yaml)

    await hass.config_entries.async_forward_entry_setups(config_entry, PLATFORMS)

    # undo_listener = config_entry.add_update_listener(async_update_options)
    # data[config_entry.entry_id] = {UNDO_UPDATE_LISTENER: undo_listener}
    # for platform in PLATFORMS:
    #     hass.async_create_task(
    #         hass.config_entries.async_forward_entry_setup(config_entry, platform),
    #     )

    return True
