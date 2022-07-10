from os import getenv

PARAMS = {
    "SERVER_HOST_ADDRESS": getenv("SERVER_HOST_ADDRESS", "127.0.0.1"),
    "SERVER_HOST_PORT": int(getenv("SERVER_HOST_PORT", 12345)),
    "FUNCTION": getenv("FUNCTION", "holding_registers"),
    "START_ADDRESS": int(getenv("START_ADDRESS", 0)),
    "LENGTH": int(getenv("LENGTH", 1)),
    "INTERVAL_PERIOD": int(getenv("INTERVAL_PERIOD", 5)),
    "INTERVAL_UNIT": getenv("INTERVAL_UNIT", "s"),
}
