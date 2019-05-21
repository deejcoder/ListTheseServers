"""
The goal of this application factory is to overcome
circular imports while still creating readable code
"""

from flask import Flask

from celery import Celery
from app.http.api import endpoints
from app.servers.models import db

class Factory:
    def __init__(self, config_object='settings'):
        """
            config_object: file containing configuration
        """
        self.config_object = config_object
        # initialize app or celery
        self._setup_app()
        self._setup_db()
        self._setup_celery()
        self._register_blueprints()

    def get_app(self):
        return self.app

    def _setup_app(self):
        self.app = Flask(__name__, static_url_path='/static/')
        self.app.config.from_object(self.config_object)
        self.app.logger.info(f'Initialized Flask app with debug={self.app.debug}')

    def _setup_db(self):
        self.db = db
        self.db.init_app(self.app)

    def _setup_celery(self):
        """
        Configures and finalizes Celery
        """
        self.celery = Celery('app.servers', autofinalize=False)
        self.celery.conf.broker_url = self.app.config['CELERY_BROKER_URL']
        self.celery.conf.result_backend = self.app.config['CELERY_RESULT_BACKEND']
        self.celery.autodiscover_tasks(['app.servers'])
        self.celery.finalize()

    def _register_blueprints(self):
        """
        Register blueprints here
        """
        self.app.register_blueprint(endpoints.bp, url_prefix='')
