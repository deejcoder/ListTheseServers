"""
For all the views which route to some URL
"""

from flask import Blueprint, current_app, jsonify, render_template
from sqlalchemy import desc
import time

from .models import Server, ServerActivity

bp = Blueprint('servers', __name__)


@bp.route('/')
def server_list():
    servers = Server.query.order_by(desc(Server.status)).all()
    return render_template('server_list.html', servers=servers)


@bp.route('/api/servers/<id>/activity')
def server_activity(id):

    server_activity = ServerActivity.query.filter_by(server_id=id)
    server_activity_list = [[r.timestamp.strftime("%Y-%m-%d %H:%M:%S"), 1 if r.status else 0] for r in server_activity]
    activity = {
        'interval_s': 30 * 60, # 30 minutes
        'data': server_activity_list
    }

    return jsonify(activity)