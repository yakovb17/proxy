from http import HTTPStatus

import pytest
from flask.testing import FlaskClient

@pytest.mark.main
def test_health_check(client: FlaskClient) -> None:
    resp = client.get('/api/health_check/')

    assert resp.status_code == HTTPStatus.OK, f'Status code should be {HTTPStatus.OK}'
    assert resp.json == {'status': 'OK'}, 'response payload is not as expected'