from app.http.api.middlewares import login_required, admin_or_owner
from app.servers.models import Server, ServerActivity
from sqlalchemy import desc
from app.common import json_response

class ServerHandler:
    def get_all(self):
        servers = Server.query.order_by(desc(Server.status)).all()
        return json_response(servers)

    def get_owned(self):
        pass

    def get_activity(self, id):
        activity = ServerActivity.query.filter_by(server_id=id)

        # format with correct date/time, and status
        activity_formatted = map(
            lambda r: [
                r.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
                1 if r.status else 0
            ],
            activity
        )

        activity = {
            'interval_s': 30 * 60,  # 30 minutes
            'data': list(activity_formatted)
        }
        return json_response(activity)

    @login_required
    def add(self, serverinfo):
        pass

    @admin_or_owner
    def delete(self, id):
        pass

    @admin_or_owner
    def update(self, id, serverinfo):
        pass

    @login_required
    def report(self, id):
        pass
