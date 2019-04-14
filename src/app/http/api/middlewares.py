import json
from functools import wraps
from flask import abort, g, request
from jwt import decode, exceptions


def login_required(f):
    """
    Decorator: login_required, wraps a function and is executed
    before the function is invoked.
    Checks to see if the user is authenticated using JWT
    """
    @wraps(f)
    def wrap(*args, **kwargs):

        authorization = request.headers.get("authorization", None)

        if not authorization:
            return json.dumps({'error': 'no authorization token provided'}), 403, {'Content-type': 'application/json'}

        try:
            auth_token = authorization.split(' ')[1]
            resp = decode(auth_token, None, verify=False, algorithms=['HS256'])
            g.user = resp['sub']
        except exceptions.DecodeError as identifier:
            return json.dumps({'error': 'invalid authorization token'}), 403, {'Content-type': 'application/json'}
        
        return f(*args, **kwargs)
    return wrap
