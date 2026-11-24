import pytest
from django.test import Client


@pytest.fixture
def client():
    return Client()


@pytest.mark.django_db
def test_health_check_returns_200(client):
    # Arrange
    url = "/api/health/"

    # Act
    response = client.get(url)

    # Assert
    assert response.status_code == 200


@pytest.mark.django_db
def test_health_check_returns_expected_json(client):
    # Arrange
    url = "/api/health/"

    # Act
    response = client.get(url)

    # Assert
    assert response.json() == {
        "status": "ok",
        "message": "Part-Time Job Matching API is running"
    }


@pytest.mark.django_db
def test_health_check_returns_json_content_type(client):
    # Arrange
    url = "/api/health/"

    # Act
    response = client.get(url)

    # Assert
    assert response["Content-Type"] == "application/json"


@pytest.mark.django_db
def test_health_check_handles_head_request(client):
    # Arrange
    url = "/api/health/"

    # Act
    response = client.head(url)

    # Assert
    assert response.status_code == 200
    assert response["Content-Type"] == "application/json"
    assert response.content == b""


@pytest.mark.django_db
def test_health_check_with_json_accept_header(client):
    # Arrange
    url = "/api/health/"

    # Act
    response = client.get(url, HTTP_ACCEPT="application/json")

    # Assert
    assert response.status_code == 200
    assert response["Content-Type"] == "application/json"


@pytest.mark.django_db
def test_health_check_with_html_accept_header(client):
    # Arrange
    url = "/api/health/"

    # Act
    response = client.get(url, HTTP_ACCEPT="text/html")

    # Assert
    assert response.status_code == 200
    assert response["Content-Type"] == "application/json"
