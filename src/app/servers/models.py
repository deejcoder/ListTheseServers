"""
Database model:
- Server; represents a server in the server list
- BaseModel is used by all models
"""

from enum import Enum
from flask_sqlalchemy import SQLAlchemy

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
    hostname = db.Column(db.String(100), nullable=False)
    port = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Boolean, nullable=True)
    server_name = db.Column(db.String(120), nullable=False)
    country = db.Column(db.String(3), nullable=False)
    description = db.Column(db.String(800), nullable=False)
    tags = db.Column(db.String(100), nullable=False)
    ping_method = db.Column(db.Integer, nullable=False)
    ping_payload = db.Column(db.LargeBinary, nullable=True)
    ping_response = db.Column(db.LargeBinary, nullable=True)
    # last record in ServerActivity
    last_ping = db.Column(db.Integer, unique=True, nullable=True)

    def __repr__(self):
        return f'<Server ({self.id}): {self.server_name}>' 


class ServerActivity(db.Model):
    """
    Model used for logging downtime/uptime of a server
    """
    id = db.Column(db.Integer, primary_key=True)
    server_id = db.Column(db.Integer, db.ForeignKey('servers.id'))
    timestamp = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.Boolean, nullable=False)
