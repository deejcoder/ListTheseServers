from app.http.api.middlewares import login_required, admin_or_owner
from app.servers.models import db
from app.plugins.pinger import Pinger
from app.servers.models import Server, ServerActivity
from app.servers.tasks import add_activity_log


def _update_status_callback(future):
    status = future.serverinfo.result()
    future.serverinfo.status = status
    add_activity_log(future.serverinfo)

class PingHandler:
    def __init__(self):
        self.pinger = Pinger()

    @admin_or_owner
    def ping_async(self, id):
        serverinfo = Server.query.get(id)
        self.pinger.ping(serverinfo=serverinfo, async_callback=_update_status_callback)
