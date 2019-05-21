from flask_sqlalchemy import SQLAlchemy
from flask import current_app


db = SQLAlchemy()


class BaseModel(db.Model):
    __abstract__ = True
    __serialize_fields__ = []

    def __init__(self, *args):
        super().__init__(*args)

    def __repr__(self):
        return '%s(%s)' % (self.__class__.__name__, {
            column: value
            for column, value in self.as_dict().items()
        })

    def as_dict(self):
        d = self.__dict__
        d.pop('_sa_instance_state', None)

        # variable specifying the fields to include in dict
        if len(self.__serialize_fields__):
            keys = list(d.keys())
            
            for key in keys:
                if key in self.__serialize_fields__:
                    continue
                
                d.pop(key, None)

        return d