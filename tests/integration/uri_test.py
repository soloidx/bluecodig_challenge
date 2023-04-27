from fastapi.testclient import TestClient
from project.app import app

client = TestClient(app)


def test_create_new_uri_should_return_201():
    data = {"origin": "http://test.com:8080/foo/bar"}
    response = client.post("/uri", json=data)
    assert response.status_code == 201
