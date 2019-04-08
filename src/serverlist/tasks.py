"""
All celery tasks
This is mainly for pinging servers to determine their availability
"""

# from celery.utils.log import get_task_logger
import os

from celery import Celery
import datetime

from common.models import db
from serverlist.models import Server, ServerActivity

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

    if not server.status:
        db.session.commit()


    # check if last ping was longer than 30 minutes ago, if so add record; can prune this later
    if server.last_ping:
        try:
            last_ping = ServerActivity.query.get(server.last_ping)

            if last_ping.timestamp < (datetime.datetime.now() - datetime.timedelta(minutes=30)):
                add_activity_log(server)
        except Exception as e:
            print(e)

    else:
        add_activity_log(server)


def add_activity_log(server):
    log = ServerActivity(server_id=server.id, timestamp=datetime.datetime.now(), status=server.status)
    db.session.add(log)
    # commit first so we can get an ID
    db.session.commit()

    server.last_ping = log.id
    db.session.commit()



# Conf
BEAT_SCHEDULE = {
    "server-status-check-task": {
        "task": "serverlist.tasks.check_servers_availability",
        "schedule": 20.0
    }
}

celery.conf.beat_schedule = BEAT_SCHEDULE
