from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import logging
# from common.tasks import make_celery


class Factory:

    def __init__(self, mode, debug=False, config_object='settings'):
        """
            mode: celery or app
            debug: True or False
            config_object: file containing configuration
        """
        assert mode in ('app', 'celery'), f'bad mode {mode}'

        self.mode = mode
        self.debug = debug
        self.config_object = config_object
        
        # initalize the worker
        self.app = None
        self._entrypoint()


    def _entrypoint(self):
        """
        Creates the Flask app, if it is a celery worker, configure celery tasks too!
        """
        self.app = Flask(__name__, static_url_path='/static/')
        self.app.debug = self.debug
        self.app.config.from_object(self.config_object)

        if self.mode is 'celery':
            self._setup_celery()

        return self.app

    def safe_current_app(self):
        """
        Determines if the Flask app is initialized, returns an initialized app
        """
        if self.app is None:
            return _entrypoint(self)
        else return self.app


    def _setup_celery(self):
        """
        TODO
        Configures Celery
        """
        return

    def _setup_blueprints():
        """
        TODO
        Configures blueprints
        """
        from serverlist.views import serverlist_app

        self.app


"""
db = SQLAlchemy()

def create_app(config_object='settings'):
    # initialize the Flask app
    app = Flask(__name__, static_url_path='/static/')

    # configure the Flask app
    app.config.from_object(config_object)
    db.init_app(app)

    # create blueprints
    create_blueprints(app)

    # create celery tasks
    # create_celery_tasks(app)

    return app


def create_blueprints(current_app):
    # import any blueprints
    from serverlist.views import serverlist_app

    # register any blueprints
    current_app.register_blueprint(serverlist_app)


def create_celery_tasks(current_app):
    # initialize celery
    celery = make_celery(current_app)
    
    # import celery tasks
    import serverlist.tasks
"""