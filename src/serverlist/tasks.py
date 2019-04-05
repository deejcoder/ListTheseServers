"""
All celery tasks
This is mainly for pinging servers to determine their availability
"""

from celery import Celery


# autofinalize will raise a warning if this is initialized before the app is
celery = Celery(__name__, autofinalize=False)


@celery.task
def ping(a, b):
    return a + b