"""
All celery tasks
This is mainly for pinging servers to determine their availability
"""

from nitroxserverlist import celery


@celery.task
def ping(a, b):
    return a + b