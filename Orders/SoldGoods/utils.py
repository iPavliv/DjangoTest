from functools import wraps

from django.conf import settings
from django.http import HttpResponse

settings.DEBUG = True
from django.db import connection


def get_query_count(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        response = f(*args, **kwargs)
        query_num = len(connection.queries)
        return HttpResponse((query_num, response))
    return wrapper
