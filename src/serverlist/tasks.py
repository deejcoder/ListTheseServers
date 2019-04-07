"""
All celery tasks
This is mainly for pinging servers to determine their availability
"""

# from celery.utils.log import get_task_logger
import os

from celery import Celery

from common.models import db
from serverlist.models import Server

# Init
celery = Celery('serverlist', autofinalize=False)


# Tasks
@celery.task
def check_servers_availability():
    """
    Pings a list of servers and determine if it is online or not, this can be expanded later
    Celery v5.0 will be introducing asyncio support
    """
    servers = Server.query.all()
    if not servers:
        return 'There are no servers to test the connectivity for...'

    for server in servers:
        send_ping_request.apply_async(kwargs={'serverid':server.id})

@celery.task
def send_ping_request(serverid):

    server = Server.query.filter_by(id=serverid).first()
    check = os.system(f"ping -c 1 {server.ip_address}")

     # True if the server is online
    server.status = True if check == 0 else False
    db.session.commit()



# Conf
BEAT_SCHEDULE = {
    "server-status-check-task": {
        "task": "serverlist.tasks.check_servers_availability",
        "schedule": 20.0
    }
}

celery.conf.beat_schedule = BEAT_SCHEDULE
