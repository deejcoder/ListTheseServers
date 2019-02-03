from flask import Flask
from ping.celery import CeleryWrapper


class Ping:
    """
    Creates a UDP ping request to all servers in the database
    to determine if they're online.
    """

    def __init__(self, app):
        self.app = app
        self.celery = CeleryWrapper(app).celery

        # needs proper organizing -- later
        @self.celery.task()
        def add(a, b):
            return a + b
        
        self.task = add.delay(1,1)
        



