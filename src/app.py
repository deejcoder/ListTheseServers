from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def create_app(config_object='settings'):
    # initialize the Flask app
    app = Flask(__name__, static_url_path='/static/')

    # configure the Flask app
    app.config.from_object(config_object)
    db.init_app(app)

    # create blueprints
    create_blueprints(app)

    return app


def create_blueprints(current_app):
    # import any blueprints
    from serverlist.views import serverlist_app

    # register any blueprints
    current_app.register_blueprint(serverlist_app)
