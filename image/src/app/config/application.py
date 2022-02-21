"""
All constants specific to the application
"""
from app.utils.env import env
from app.utils.intenv import intenv


APPLICATION = {
    "SERVER_HOST_ADDRESS": env("SERVER_HOST_ADDRESS", "127.0.0.1"),
    "SERVER_HOST_PORT": intenv("SERVER_HOST_PORT", 12345),
    "FUNCTION": env("FUNCTION", "holding_registers"),
    "START_ADDRESS": intenv("START_ADDRESS", 0),
    "LENGTH": intenv("LENGTH", 1),
    "INTERVAL_PERIOD": intenv("INTERVAL_PERIOD", 5),
    "INTERVAL_UNIT": env("INTERVAL_UNIT", "s"),
    "OUTPUT_LABEL": env("OUTPUT_LABEL", "registers")
}
