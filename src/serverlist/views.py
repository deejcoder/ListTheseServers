"""
For all the views which route to some URL
"""

from flask import current_app, Blueprint, render_template

from .models import Server


serverlist_app = Blueprint('serverlist_app', __name__)


@serverlist_app.route('/')
def server_list():
    servers = Server.query.all()
    return render_template('server_list.html', servers=servers)