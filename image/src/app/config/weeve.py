"""
All constants specific to weeve
"""
from app.utils.env import env

WEEVE = {
    "MODULE_NAME": env("MODULE_NAME", "python-ingress-boilerplate"),
    "MODULE_TYPE": env("MODULE_TYPE", "INGRESS"),
    "EGRESS_SCHEME": env("EGRESS_SCHEME", "http"),
    "EGRESS_HOST": env("EGRESS_HOST", "0.0.0.0"),
    "EGRESS_PORT": env("EGRESS_PORT", "80"),
    "EGRESS_PATH": env("EGRESS_PATH", ""),
    "EGRESS_URL": env("EGRESS_URL", "http://localhost:8000")
}
