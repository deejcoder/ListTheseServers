# ========= [ Flask  ] ==========

DEBUG = True

# ========= [ postgres ]=========
POSTGRES = {
    'user': 'nitrox',
    'pw': 'nitroxserverlistpass',
    'db': 'nitrox',
    'host': 'localhost',
    'port': 5432,
}
SQLALCHEMY_DATABASE_URI = 'postgresql://{user}:{pw}@{host}:{port}/{db}'.format(**POSTGRES)


# ======== [ celery ]=========
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

