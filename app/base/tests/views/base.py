from typing import Any
from urllib.parse import urlencode

from app.base.exceptions import APIWarning
from app.base.tests.base import BaseTest


class BaseViewTest(BaseTest):
    path: str

    def get(self, path=None, query=None):
        return self.client.get(f'{path or self.path}?{urlencode(query or {})}')

    def post(self, path=None, data=None):
        return self.client.post(path or self.path, data)

    def put(self, path=None, data=None):
        return self.client.put(path or self.path, data)

    def patch(self, path=None, data=None):
        return self.client.patch(path or self.path, data)

    def delete(self, path=None, data=None):
        return self.client.delete(path or self.path, data)

    def assert_response(self, response, status=200, data: dict = None):
        self.assert_equal(response.status_code, status)
        self.assert_json(response.json() if response.content else {}, data or {})

    def _test(
        self,
        method: str,
        exp_data: dict[str, Any] | APIWarning = None,
        data: dict[str, Any] = None,
        status: int = None,
        path: str = None,
    ):
        response = getattr(self, method)(path, data)
        if response.content:
            status = status or {'post': 201, 'delete': 204}.get(method, 200)
        else:
            status = 204
        if isinstance(exp_data, APIWarning):
            status = exp_data.status
            exp_data = exp_data.serialize()
        self.assert_response(response, status, exp_data)
