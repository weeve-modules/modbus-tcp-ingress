"""
Entrypoint file that sets up and starts REST API server for the module.
"""

from os import getenv
from logging import getLogger
from api import setup_logging
from module.module import module_main

setup_logging()
log = getLogger("main")

def main():
    log.info(
        "%s running with end-point set to %s",
        getenv("MODULE_NAME"),
        getenv("EGRESS_URLS"),
    )

    module_main()

if __name__ == "__main__":
    main()
