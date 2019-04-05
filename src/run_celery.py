# celery worker -A run_celery.celery --loglevel=info

from factory import Factory


factory = Factory('celery')
celery = factory.get_app()