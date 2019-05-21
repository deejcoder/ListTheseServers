import time

from flask import Blueprint
from sqlalchemy import desc


from app.common import json_response
from app.servers.models import Server, ServerActivity
from flask_cors import CORS


bp = Blueprint('endpoints', __name__)
CORS(bp)


@bp.route('/api/servers')
def index():
    """ returns all servers sorted by status """
    servers = Server.query.order_by(desc(Server.status)).all()
    return json_response(servers)


@bp.route("/api/servers/<id>/activity", methods=["GET"])
def activity(id):
    """ Returns server activity as JSON, with correct format for graph """

    activity = ServerActivity.query.filter_by(server_id=id)

    # format with correct date/time, and status
    activity_formatted = map(
        lambda r : [
            r.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            1 if r.status else 0
        ],
        activity
    )

    activity = {
        'interval_s': 30 * 60, # 30 minutes
        'data': list(activity_formatted)
    }

    return json_response(activity)




