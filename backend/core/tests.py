import pytest
from django.test import Client


@pytest.fixture
def client():
    return Client()


@pytest.mark.django_db
def test_health_check_returns_200(client):
    response = client.get("/api/health/")

    assert response.status_code == 200


@pytest.mark.django_db
def test_health_check_returns_expected_json(client):
    response = client.get("/api/health/")

    assert response.json() == {
        "status": "ok",
        "message": "Part-Time Job Matching API is running"
    }


@pytest.mark.django_db
def test_health_check_accepts_get_request(client):
    response = client.get("/api/health/")

    assert response.status_code != 405


@pytest.mark.django_db
def test_health_check_returns_json_content_type(client):
    response = client.get("/api/health/")

    assert response["Content-Type"] == "application/json"
