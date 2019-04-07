"""
For all the views which route to some URL
"""

from flask import current_app, Blueprint, render_template

from .models import Server


bp = Blueprint('servers', __name__)


@bp.route('/')
def server_list():
    servers = Server.query.all()
    return render_template('server_list.html', servers=servers)