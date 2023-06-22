from functools import wraps
from flask import jsonify, g


def admin_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if hasattr(g, 'user') and g.user is not None and g.role == "admin":
            return func(*args, **kwargs)
        else:
            return jsonify({
                "code": 403,
                "message": "admin require",
                "data": None
            })
    return wrapper


def student_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if hasattr(g, 'user') and g.user is not None and g.role == "student":
            return func(*args, **kwargs)
        else:
            return jsonify({
                "code": 403,
                "message": "login require",
                "data": None
            })
    return wrapper
