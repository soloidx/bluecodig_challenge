import pytest
from fastapi.testclient import TestClient
from project.app import app, get_db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from project import models

web_client = TestClient(app)

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


@pytest.fixture(scope="function")
def db():
    models.Base.metadata.create_all(bind=engine)
    yield engine
    models.Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def client(db):
    try:
        app.dependency_overrides[get_db] = override_get_db
        yield
    finally:
        app.dependency_overrides.clear()


def test_normal_flow(client):
    data = {"origin": "https://test.com:8080/foo/bar"}
    response = web_client.post("/uri/", json=data)
    # should create a new short url
    assert response.status_code == 201

    json_obj = response.json()
    short_code = json_obj["short_code"]
    count = json_obj["count"]
    response = web_client.get(f"/{short_code}", follow_redirects=False)
    # should redirect to the original url
    assert response.status_code == 302
    assert count == 0

    response = web_client.get("/uri/")
    json_obj = response.json()
    # should increase the count
    assert json_obj[0]["count"] == 1


def test_url_created_twice(client):
    data = {"origin": "https://test.com:8080/foo/bar"}
    response = web_client.post("/uri/", json=data)
    json_obj = response.json()
    short_code = json_obj["short_code"]
    count = json_obj["count"]

    assert count == 0

    web_client.get(f"/{short_code}", follow_redirects=False)

    response = web_client.post("/uri/", json=data)
    # should redirect to the original url
    assert response.status_code == 201

    json_obj = response.json()
    new_short_code = json_obj["short_code"]
    count = json_obj["count"]

    assert new_short_code == short_code
    assert count == 1


def test_url_with_query_param(client):
    data = {"origin": "https://test.com:8080/foo/bar?a=1&b=2"}
    response = web_client.post("/uri/", json=data)
    json_obj = response.json()
    short_code = json_obj["short_code"]

    data = {"origin": "https://test.com:8080/foo/bar"}
    response = web_client.post("/uri/", json=data)
    json_obj = response.json()
    new_short_code = json_obj["short_code"]

    assert new_short_code == short_code
