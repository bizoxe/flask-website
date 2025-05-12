import pytest
from pytest_mock import MockFixture

from src.app import create_app
from src.settings import TestingConfig


@pytest.fixture(scope="function")
def app():
    _app = create_app(config_object=TestingConfig)

    ctx = _app.test_request_context()
    ctx.push()

    yield _app
    ctx.pop()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture(scope="function")
def mock_send_email(mocker: MockFixture):
    mocker.patch("src.routes.base.send_email", return_value=True)


@pytest.fixture(scope="function")
def mock_send_email_failed(mocker: MockFixture):
    mocker.patch("src.routes.base.send_email", return_value=False)
