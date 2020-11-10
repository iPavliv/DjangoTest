from functools import wraps

from django.conf import settings
from django.shortcuts import render

settings.DEBUG = True
from django.db import connection


def get_query_count(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        response = f(*args, **kwargs)
        query_num = len(connection.queries)
        context = {'query_number': query_num, 'data': response[2]}
        return render(response[0], response[1], context=context)
    return wrapper
