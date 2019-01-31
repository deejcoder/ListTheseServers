from flask import Flask, render_template
from settings import app
import models


@app.route('/')
def server_list():
    servers = models.Server.query.all()
    return render_template('server_list.html', servers=servers)

if __name__ == '__main__':
    app.run()