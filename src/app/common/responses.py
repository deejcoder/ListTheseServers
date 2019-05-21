from flask import jsonify
from app.servers.models import db

def to_dict(queryresult):
    # untested conversion. patch later.
    # TODO: check conversion
    d = dict(queryresult.__dict__)     # copy
    d.pop('_sa_instance_state')
    return d

def json_response(payload, status=200):
    """
    * Prevent top-level arrays since they're considered 'generally unsafe'
    https://github.com/pallets/flask/issues/170
    * Also, if class belongs to BaseModel, call as_dict first to serialize
    """
    if isinstance(payload, db.Model):
        return jsonify(to_dict(payload)), status

    if isinstance(payload, list):
        result = [to_dict(payload) if isinstance(item, db.Model) else item for item in payload]
        return jsonify(list=result), status

    return jsonify(payload), status
