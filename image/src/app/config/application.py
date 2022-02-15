"""
All constants specific to the application
"""
from app.utils.env import env


APPLICATION = {
    "OUTPUT_LABEL": env("OUTPUT_LABEL", "temperature"),
    "OUTPUT_UNIT": env("OUTPUT_UNIT", "Celsius"),
}
