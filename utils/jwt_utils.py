from functools import wraps

from flask import current_app as app
from flask import request
from jwt import (DecodeError, ExpiredSignatureError, InvalidSignatureError,
                 InvalidTokenError, decode)


def jwt_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.headers.get('X-API-KEY')  # noqa
        if not token:
            return {'errors': {'apikey': 'API key is missing'}, 'message': 'Unautorized'}, 401  # noqa
        try:
            decode(token, app.config['SECRET_KEY'],
                   algorithms=['HS256'], verify=True)
        except (ExpiredSignatureError, InvalidTokenError, DecodeError,
                InvalidSignatureError, ExpiredSignatureError) as e:
            return {'errors': {'apikey': str(e)}, 'message': 'Unautorized'}, 401  # noqa
        return f(*args, **kwargs)
    return decorated_function
