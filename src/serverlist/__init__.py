# Flask
"""
from flask import Flask
from serverlist.config import Config
from serverlist.models import db
import serverlist.views


app = Flask(__name__, static_url_path='/static')
app.config.from_object(Config)
db.init_app(app)


# Celery
from celery import Celery
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)


__all__ = ['app', 'celery', 'db']
"""