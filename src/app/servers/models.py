"""
Database model:
- Server; represents a server in the server list
- BaseModel is used by all models
"""

from app.common.models import db, BaseModel


class Server(BaseModel, db.Model):
    """
    Model representing a server
    """
    __tablename__ = 'servers'
    __table_args__ = (
        db.UniqueConstraint('ip_address', 'port', name='ip_port_unique_constraint'),
    )

    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(3), nullable=False)
    ip_address = db.Column(db.String(39), nullable=False) # 39 = max length for ipv6
    port = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Boolean, nullable=True)
    server_name = db.Column(db.String(120), nullable=False)
    gamemode = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(800), nullable=False)

    # last record in ServerActivity
    last_ping = db.Column(db.Integer, unique=True, nullable=True)


    def __repr__(self):
        return f'<Server ({self.id}): {self.server_name}>' 


class ServerActivity(BaseModel, db.Model):
    """
    Model used for logging downtime/uptime of a server
    """
    id = db.Column(db.Integer, primary_key=True)
    server_id = db.Column(db.Integer, db.ForeignKey('servers.id'))
    timestamp = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.Boolean, nullable=False)


    def __init__(self, server_id, timestamp, status):
        self.server_id = server_id
        self.timestamp = timestamp
        self.status = status