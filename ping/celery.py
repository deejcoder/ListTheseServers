# http://flask.pocoo.org/docs/1.0/patterns/celery/
# Used for intregrating Celery with Flask

from celery import Celery
from nitroxserverlist import settings
from datetime import timedelta


class CeleryWrapper:
    def __init__(self, app):
        self.celery = Celery(
            app.import_name,
            backend=app.config['CELERY_RESULT_BACKEND'],
            broker=app.config['CELERY_BROKER_URL'],
        )

        self.celery.conf.update(app.config)
        self.task = self.celery.Task

    class ContextTask(self.task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.task.__call__(self, *args, **kwargs)




