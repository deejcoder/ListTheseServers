import time

from flask import Blueprint, request
from sqlalchemy import desc

from app.common import json_response
from app.servers.models import Server, ServerActivity
from app.common.handler import serverHandler, userHandler, pingHandler, ddnsHandler
from flask_cors import CORS


bp = Blueprint('endpoints', __name__)
CORS(bp)

"""
While using X-Handler, pass `id` argument (server id) as kwargs, so decorator `admin_or_owned` will work.
"""


@bp.route('/api/servers/')
def servers_list():
    """ returns all servers sorted by status """
    # TODO: filters and paging
    return serverHandler.get_all()


@bp.route('/api/server/get/')
def server_get():
    """
    get a list of server that belongs to current user
    :return:
    """
    return serverHandler.get_owned()


@bp.route("/api/server/activity/<id>/")
def server_activity(id):
    """ Returns server activity as JSON, with correct format for graph """
    return serverHandler.get_activity(id=id)


@bp.route('/api/server/add/', methods=['POST'])
def server_add():
    # TODO: uplimit
    serverinfo = request.get_json()
    return serverHandler.add(serverinfo=serverinfo)


@bp.route('/api/server/del/<id>/')
def server_del(id):
    return serverHandler.delete(id=id)


@bp.route('/api/server/update/<id>/', methods=['POST'])
def server_update(id):
    serverinfo = request.get_json()
    return serverHandler.update(id=id, serverinfo=serverinfo)


@bp.route('/api/server/report/<id>/')
def server_report(id):
    return serverHandler.report(id=id)


@bp.route('/api/ping/<id>/')
def ping(id):
    """
    trigger a ping manually, refresh status
    """
    return pingHandler.ping_sync(id=id)


@bp.route('/api/ddns/add/<id>/', methods=['POST'])
def ddns_add(id):
    """
    add a custom_subdomain to server_id
    """
    ddnsinfo = request.get_json()
    return ddnsHandler.add(id=id, ddnsinfo=ddnsinfo)


@bp.route('/api/ddns/del/<id>/')
def ddns_del(id):
    """
    :param id: server id
    """
    return ddnsHandler.delete(id=id)


@bp.route('/api/ddns/update/<id>/', methods=['POST'])
def ddns_update(id):
    """
    :param id: server id
    """
    ddnsinfo = request.get_json()
    return ddnsHandler.update(id=id, ddnsinfo=ddnsinfo)


# TODO: User api
