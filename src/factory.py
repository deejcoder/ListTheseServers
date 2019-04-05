"""
The goal of this application factory is to overcome
circular imports while still creating readable code
"""

import logging

from flask import Flask


from serverlist.tasks import celery
from serverlist import routes, models


class Factory:
    """
    Four steps:
        1. Initialize Flask app or Celery configured app (depends on which worker is running)
        2. Initialize SQLAlchemy
        3. Configure Celery
        4. Register any blueprints
    """

    def __init__(self, mode, debug=False, config_object='settings'):
        """
            mode: celery or app
            debug: True or False
            config_object: file containing configuration
        """
        assert mode in ('app', 'celery'), f"Bad mode {mode}. Must be 'app' or 'celery'"

        self.mode = mode
        self.debug = debug
        self.config_object = config_object

        # configure logger
        self.logger = logging.getLogger()
        self.logger.setLevel(debug)
        
        # initalize the worker
        self.app = None
        self.db = models.db
        self.celery = celery

        self._entrypoint()


    def _entrypoint(self):
        """
        Creates the Flask app, if it is a celery worker, configure celery tasks too!
        """
        # initialize Flask app
        self.app = Flask(__name__, static_url_path='/static/')
        self.app.debug = self.debug
        self.app.config.from_object(self.config_object)

        # run setup functions
        self._setup_db()
        self._setup_celery()
        self._register_blueprints()


    def get_app(self):
        return self.app if self.mode == 'app' else self.celery


    def _setup_db(self):
        self.db.init_app(self.app)


    def _setup_celery(self):
        """
        Configures and finalizes Celery
        """

        self.celery.conf.broker_url = self.app.config['CELERY_BROKER_URL']
        self.celery.conf.result_backend = self.app.config['CELERY_RESULT_BACKEND']

        TaskBase = self.celery.Task
        class AppContextTask(TaskBase):
            abstract = True

            def __call__(self, *args, **kwargs):
                with self.app.app_context():
                    return TaskBase.__call__(self, *args, **kwargs)
        

        self.celery.Task = AppContextTask
        self.celery.finalize()


    def _register_blueprints(self):
        """
        Register blueprints here
        """
        self.app.register_blueprint(routes.bp, url_prefix='')
