"""
Some Flask tools for managing the DB

`python manage.py [cmds]` -- similar to Django
"""

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from factory import Factory

if __name__ == '__main__':
    # exportable
    factory = Factory()
    app = factory.get_app()
    db = factory.db
    celery = factory.celery
    migrate = Migrate(app, db)
    manager = Manager(app)
    manager.add_command('db', MigrateCommand)
    manager.run()
