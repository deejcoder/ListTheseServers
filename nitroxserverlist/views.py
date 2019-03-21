"""
For all the views which route to some URL
"""

from nitroxserverlist import app, models

print(__file__)
@app.route('/')
def server_list():
    servers = models.Server.query.all()
    return render_template('server_list.html', servers=servers)