import pytest

from flask.testing import FlaskClient

from proxy.app import create_app

@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })

    yield app

@pytest.fixture()
def client(app) -> FlaskClient:
    return app.test_client()