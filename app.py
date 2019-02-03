from flask import Flask, render_template
import os

from nitroxserverlist.models import db
from config import Config
from ping import Ping

app = Flask(__name__, static_url_path='/static')
app.config.from_object(Config)

db.init_app(app)
ping = Ping(app)



@app.route('/')
def server_list():
    servers = models.Server.query.all()
    return render_template('server_list.html', servers=servers)


if __name__ == '__main__':
    app.run()