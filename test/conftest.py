import pytest

from app import create_app
from configs import TestingConfig


@pytest.fixture()
def client():
    test_app = create_app(TestingConfig)
    with test_app.test_client() as client:
        yield client
