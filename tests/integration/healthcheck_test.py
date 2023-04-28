from fastapi.testclient import TestClient
from project.app import app

client = TestClient(app)


def test_health_check_is_present():
    response = client.get("/healthcheck/")
    assert response.status_code == 200
