from http import HTTPStatus

import pytest
from flask.testing import FlaskClient

@pytest.mark.main
class TestProxyPassGetMethod:
    URL: str = '/api/proxy'

    def test_happy_flow(self, client: FlaskClient) -> None:
        resp = client.get(self.URL)

        assert resp.status_code == HTTPStatus.OK, f'status code should be {HTTPStatus.OK}'