import time

from flask import Blueprint, request
from sqlalchemy import desc

from .middlewares import login_required
from app.common import json_response
from app.servers.models import Server, ServerActivity
from flask_cors import CORS


bp = Blueprint('endpoints', __name__)
CORS(bp)


@bp.route('/api/servers/')
def servers_list():
    """ returns all servers sorted by status """
    # TODO: filters and paging
    servers = Server.query.order_by(desc(Server.status)).all()
    return json_response(servers)


@login_required
@bp.route('/api/server/get/')
def server_get():
    """
    get a list of server that belongs to current user
    :return:
    """
    pass


@bp.route("/api/server/activity/<id>/")
def server_activity(id):
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


@login_required
@bp.route('/api/server/add/', methods=['POST'])
def server_add():
    # total count limit
    pass


@login_required
@bp.route('/api/server/del/<id>/')
def server_del(id):
    # check if id belongs to current user, or admin
    pass


@login_required
@bp.route('/api/server/update/', methods=['POST'])
def server_update():
    # check if id belongs to current user, or admin
    pass


@login_required
@bp.route('/api/server/ping/<id>/')
def server_ping():
    """
    trigger a ping manually, refresh status
    """
    # check if id belongs to current user, or admin
    pass


@login_required
@bp.route('/api/server/report/<id>/')
def server_report(id):
    pass


@login_required
@bp.route('/api/ddns/add/', methods=['POST'])
def server_ddns_add():
    """
    server_id, custom_subdomain,
    :return: success or not
    """
    # check if id belongs to current user, or admin
    pass


@login_required
@bp.route('/api/ddns/del/<id>/')
def server_ddns_del(id):
    # check if id belongs to current user, or admin
    pass


@login_required
@bp.route('/api/ddns/update/', methods=['POST'])
def server_ddns_update():
    # check if id belongs to current user, or admin
    pass
