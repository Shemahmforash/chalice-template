from http import HTTPStatus

import pytest
from chalice import Chalice
from pytest_chalice.handlers import RequestHandler, ResponseHandler

from app import app as chalice_app


@pytest.fixture
def app() -> Chalice:
    return chalice_app


class TestChalice:
    def test_index(self, client: RequestHandler):
        response: ResponseHandler = client.get("/")

        assert response.status_code == HTTPStatus.OK
        assert response.json == {"hello": "world"}
