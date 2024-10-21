import pytest  # type: ignore
from fastapi.testclient import TestClient

from fastapi_zero.app import app


@pytest.fixture
def client():
    return TestClient(app)
