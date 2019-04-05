"""
For all the views which route to some URL
"""

from flask import current_app, Blueprint, render_template

from .models import Server
from .tasks import get_server_status


bp = Blueprint('servers', __name__)


@bp.route('/')
def server_list():
    task = get_server_status.apply_async(kwargs={'ip':'192.168.1.200'})
    servers = Server.query.all()
    return render_template('server_list.html', servers=servers)