"""
All celery tasks
This is mainly for pinging servers to determine their availability
"""

from celery import Celery
# from celery.utils.log import get_task_logger

from serverlist.models import Server


# Init
celery = Celery('serverlist', autofinalize=False)


# Tasks
@celery.task
def check_servers_availability():
    """
    Pings a list of servers and determine if it is online or not
    """
    servers = Server.query.all()
    if not servers:
        return 'There are no servers to test the connectivity for...'
    return f'{servers[0]}: Checking status...' # just for testing, test one server



# Conf
BEAT_SCHEDULE = {
    "server-status-check-task": {
        "task": "serverlist.tasks.check_servers_availability",
        "schedule": 20.0
    }
}

celery.conf.beat_schedule = BEAT_SCHEDULE
    

