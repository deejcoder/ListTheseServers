"""
All celery tasks
This is mainly for pinging servers to determine their availability
"""

from celery import Celery


# autofinalize will raise a warning if this is initialized before the app is
celery = Celery(__name__, autofinalize=False)


@celery.task(bind=True)
def get_server_status(self, ip):
    """
    Ping a server and determine if it is online or not
    """
    return ip