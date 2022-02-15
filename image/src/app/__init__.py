"""
Main flask entry point
"""
from logging import getLogger


from app.config import WEEVE
from app.weeve import send_data
from app.module import module_main
log = getLogger(__name__)


def create_app() -> bool:
    """ Configures the flask ap and returns it

    Returns:
        bool: [App created or not]
    """
    ingress_data, err = module_main()

    if err:
        log.error("Error %s", err)
        return False
    if not ingress_data:
        log.error("No ingress data")
        return False
    sent = send_data(ingress_data)

    if sent:
        log.info("Data sent successfully")
        return True
    else:
        log.error("Error while sending data")
        return False
