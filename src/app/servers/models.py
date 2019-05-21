"""
Database model:
- Server; represents a server in the server list
- BaseModel is used by all models
"""

from enum import Enum
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Perm(Enum):
    Guest = 0
    User = 1
    Admin = 2


class Server(db.Model):
    """
    Model representing a server
    """
    __tablename__ = 'servers'
    __table_args__ = (
        db.UniqueConstraint('hostname', 'port', name='hostname_port_unique_constraint'),
    )

    # __serialize_fields__ = ['id', 'server_name', 'ip_address', 'port', 'status', 'country', 'description']

    id = db.Column(db.Integer, primary_key=True)
    server_name = db.Column(db.String(120), nullable=False)
    hostname = db.Column(db.String(100), nullable=False)
    port = db.Column(db.Integer, nullable=False)
    uid = db.Column(db.Integer, db.ForeignKey('users.id'))
    status = db.Column(db.Boolean, nullable=True)
    last_ping_id = db.Column(db.Integer, db.ForeignKey('activities.id'))
    country = db.Column(db.String(3), nullable=False)
    description = db.Column(db.String(800), nullable=False)
    tags = db.Column(db.String(100), nullable=False)
    ping_method = db.Column(db.Integer, nullable=False)
    ping_payload = db.Column(db.LargeBinary, nullable=True)
    ping_response = db.Column(db.LargeBinary, nullable=True)

    last_ping = db.relationship('activities')
    user = db.relationship('users', backref=db.backref('servers', lazy=True))

    def __repr__(self):
        return f'<Server ({self.id}): {self.server_name}>' 


class ServerActivity(db.Model):
    """
    Model used for logging downtime/uptime of a server
    """
    __tablename__ = 'activities'

    id = db.Column(db.Integer, primary_key=True)
    server_id = db.Column(db.Integer, db.ForeignKey('servers.id'))
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.now())
    status = db.Column(db.Boolean, nullable=False)

    server = db.relationship('servers', backref=db.backref('activities', lazy=True))

class User(db.Model):
    """

    """
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), nullable=False)
    salt = db.Column(db.String(32), nullable=False)
    password = db.Column(db.String(32), nullable=False)  #  hash(password + salt32)
    reg_time = db.Column(db.DateTime, nullable=False, default=datetime.now())
