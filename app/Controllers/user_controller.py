from functools import wraps 
from flask import abort
from flask_login import current_user

def role_required(role):
    def decorador(func):
        @wraps(func)
        def wraps_function(*args, **kwargs):
            if not current_user.is_authenticated or current_user.role != role:
                abort(403)
            return func(*args, **kwargs)
        return wraps_function
    return decorador
