"""Constants for the Adaptive Shutters integration."""

import homeassistant.helpers.config_validation as cv
from homeassistant.const import CONF_ENTITY_ID
from homeassistant.helpers import selector

ICON_MAIN = "mdi:window-shutter-auto"

DOMAIN = "adaptive_shutters"

CONF_START_TILTING_AZIMUTH, DEFAULT_START_TILTING_AZIMUT = "start_tilting_azimuth", 165
CONF_END_TILTING_AZIMUTH, DEFAULT_END_TILTING_AZIMUT = "END_tilting_azimuth", 360

# weather TODO: ??
CONF_WEATHER_ENTITY, DEFAULT_WEATHER_ENTITY = (
    "weather_entity",
    "sensor.openweathermap_cloud_coverage",
)

CONF_MAX_CLOUD_COVARAGE, DEFAULT_MAX_CLOUD_COVARAGE = "max_cloud_covarage", 90


# sun
CONF_SUN_ENTITY_ID, DEFAULT_SUN_ENTITY_ID = "sun_entity_id", "sun.sun"

CONF_SUNRISE_TIME, DEFAULT_SUNRISE_TIME = "sunrise_time", ""
CONF_SUNRISE_OFFSET, DEFAULT_SUNRISE_OFFSET = "sunrise_offset", 0

CONF_SUNSET_TIME, DEFAULT_SUNSET_TIME = "sunset_time", ""
CONF_SUNSET_OFFSET, DEFAULT_SUNSET_OFFSET = "sunset_offset", 0

CONF_NAME, DEFAULT_NAME = "name", "default"
# DOCS[CONF_NAME] = "Display name for this switch. 📝"

# - cloud b
# - tilting azimuth
# - weather entity
# - sun entity
# - morning:
#     - open time fixed
#     - sunrise
#     - sunrise offset
#     - week days
#     - vacation/days of days
#     - guest override
# - evening:
#     - fixed time
#     - sunset
#     - sunset offset
