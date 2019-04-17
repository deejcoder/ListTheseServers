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

    __serialize_fields__ = ['id', 'server_name', 'ip_address', 'port', 'status', 'country', 'description']

    id = db.Column(db.Integer, primary_key=True)
    ip_address = db.Column(db.String(39), nullable=False) # 39 = max length for ipv6
    port = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Boolean, nullable=True)
    server_name = db.Column(db.String(120), nullable=False)
    country = db.Column(db.String(3), nullable=False)
    description = db.Column(db.String(800), nullable=False)

    # last record in ServerActivity
    last_ping = db.Column(db.Integer, unique=True, nullable=True)

    def __init__(self, ip_address, port, server_name, country, description):
        self.ip_address = ip_address
        self.port = port
        self.server_name = server_name
        self.country = country
        self.description = description

    def __repr__(self):
        return f'<Server ({self.id}): {self.server_name}>' 

    @classmethod
    def create_server(cls, ip_address: str, port: int, server_name: str, 
        country: str, description: str, tags=[]):
        """
        Simple wrapper to creating a server, adding tags when needed
        """

        server = Server(ip_address, port, server_name, country, description)
        db.session.add(server)
        db.session.commit()

        for tag_text in tags:
            tag = Tag(server.id, tag_text)
            db.session.add(tag)



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


class ServerTag(BaseModel, db.Model):
    """
    Allows servers to have many tags
    """
    id = db.Column(db.Integer, primary_key=True)
    server_id = db.Column(db.Integer, db.ForeignKey('servers.id'), nullable=False)
    text = db.Column(db.String(30), nullable=False)

    def __init__(self, server_id, text):
        self.server_id = server_id
        self.text = text
