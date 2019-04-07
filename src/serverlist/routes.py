"""
For all the views which route to some URL
"""

from flask import current_app, Blueprint, render_template
from sqlalchemy import desc

from .models import Server


bp = Blueprint('servers', __name__)


@bp.route('/')
def server_list():
    servers = Server.query.order_by(desc(Server.status)).all()
    return render_template('server_list.html', servers=servers)