from flask import Blueprint, Flask, g, json, request
from flask_cors import CORS

from app.servers.models import Server, ServerActivity

from .middlewares import login_required

bp = Blueprint('endpoints', __name__)
CORS(bp)


@bp.route('/')
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
        'data': server_activity_list
    }

    return json_response(activity)
