from factory import Factory


factory = Factory('celery', True)
celery = factory.get_app()