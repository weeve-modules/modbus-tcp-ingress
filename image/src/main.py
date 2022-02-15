"""Main app file"""
from logging import getLogger
from app import create_app
from app.config import WEEVE, configure_logging


log = getLogger("main")


def main():
    """ Main app entry point"""
    configure_logging()

    created = create_app()
    if created:
        log.info("%s Started", WEEVE["MODULE_NAME"])
    else:
        log.error("%s faced error while starting", WEEVE["MODULE_NAME"])


if __name__ == "__main__":
    main()
