from celery import Celery
from app import create_app

# http://flask.pocoo.org/docs/1.0/patterns/celery/
def make_celery_app(app=None):
    app = app or create_app('settings')
    
    celery = Celery(
        app.import_name,
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL'],
    )

    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery