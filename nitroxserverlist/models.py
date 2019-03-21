"""
Database model:
- Server; represents a server in the server list
- BaseModel is used by all models
"""
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class BaseModel(db.Model):
    __abstract__ = True

    def __init__(self, *args):
        super().__init__(*args)

    def __repr__(self):
        return '%s(%s)' % (self.__class__.__name__, {
            column: value
            for column, value in self._to_dict().items()
        })

    def json(self):
        return {
            column: value if not isinstance(value, datetime.date) else value.strftime('%Y-%m-%d')
            for column, value in self._to_dict().items()
        }


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
    server_name = db.Column(db.String(120), nullable=False)
    gamemode = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(800), nullable=False)


    def __repr__(self):
        return f'<Server ({self.id}): {self.server_name}>' 
