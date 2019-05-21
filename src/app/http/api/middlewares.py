import json
from functools import wraps, partial
from flask import abort, g, request
from jwt import decode, exceptions
from app.servers.models import User
from hashlib import md5
from flask import g

# TODO: switch to flask-session
def login_required(f):
    """
    Decorator: login_required, wraps a function and is executed
    before the function is invoked.
    Checks to see if the user is authenticated using JWT
    """

    @wraps(f)
    def wrap(*args, **kwargs):
        # check login before
        if 'authorized' in g.__dict__ and g.authorized:
            return f(*args, **kwargs)

        # not login yet, start new auth procedure
        authorization = request.headers.get("authorization", None)
        if not authorization:
            return json.dumps({'error': 'no authorization token provided'}), 403, {'Content-type': 'application/json'}
        try:
            auth_token = authorization.split(' ')[1]
            # TODO: RSA (RS256)
            # https://pyjwt.readthedocs.io/en/latest/usage.html#encoding-decoding-tokens-with-rs256-rsa
            public_key = '-----BEGIN PUBLIC KEY----- ...'
            resp = decode(auth_token, public_key, verify=False, algorithms=['RS256'])
            id = resp['id']
            password = resp['password']
            user = User.query.get(id)
            if user:
                salt = user.salt
                hashed_password = md5(str.encode(password + salt))
                user = User.query.filter(id=id, password=hashed_password)
                if user:
                    g.authorized = True
                    g.user = user
        except exceptions.DecodeError as identifier:
            return json.dumps({'error': 'invalid authorization token'}), 403, {'Content-type': 'application/json'}
        if ('authorized' not in g.__dict__) or (not g.authorized):
            return json.dumps({'error': 'wrong username/password'}), 403, {'Content-type': 'application/json'}
        return f(*args, **kwargs)
    return wrap


def current_user_is_admin():
    pass


def server_belongs_to_current_user(id):
    if id is None:
        return False
    pass


def admin_or_owner(f):
    """
    function has to be defined as f(..., id, ...) and called as f(..., id=id, ...)
    :param f: function
    :return: bool
    """

    @login_required
    def wrap(*args, **kwargs):
        server_id = None
        if 'id' in kwargs:
            server_id = kwargs['id']
        if current_user_is_admin() or server_belongs_to_current_user(server_id):
            return f(*args, **kwargs)
        else:
            return json.dumps({'error': 'insufficient permission'}), 403, {'Content-type': 'application/json'}

    return wrap
