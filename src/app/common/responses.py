from flask import jsonify

from .models import BaseModel


def json_response(payload, status=200):
    """
    * Prevent top-level arrays since they're considered 'generally unsafe'
    https://github.com/pallets/flask/issues/170
    * Also, if class belongs to BaseModel, call as_dict first to serialize
    """
    if isinstance(payload, BaseModel):
        return jsonify(payload.as_dict()), status

    if isinstance(payload, list):
        result = [item.as_dict() if isinstance(item, BaseModel) else item for item in payload]
        return jsonify(list=result), status

    return jsonify(payload), status
    