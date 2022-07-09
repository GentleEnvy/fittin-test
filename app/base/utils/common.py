from typing import Any, TypeVar
from urllib.parse import parse_qsl, urlencode, urlparse, urlunparse

from django.db import models
from rest_framework.response import Response

from app.base.utils.schema import extend_schema

__all__ = ['status_by_method', 'add_query_params', 'response_204']

_Choices = TypeVar('_Choices', bound=models.Choices)


def status_by_method(method: str) -> int:
    match method.lower():
        case 'post':
            return 201
        case 'delete':
            return 204
        case _:
            return 200


def add_query_params(url: str, **query_params: Any) -> str:
    url_parts = list(urlparse(url))
    old_query_params = dict(parse_qsl(url_parts[4]))
    new_query_params = {k: str(v) for k, v in query_params.items()}
    url_parts[4] = urlencode(old_query_params | new_query_params)
    return urlunparse(url_parts)


def response_204(f):
    def _f_decorator(*args, **kwargs):
        f(*args, **kwargs)
        return Response(status=204)

    return extend_schema(responses={201: None, 204: ''})(_f_decorator)