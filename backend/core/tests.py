"""Tests for the core application health check endpoint."""

import pytest


@pytest.mark.django_db
def test_health_check_returns_200(client):
    """Verify that the health endpoint returns HTTP 200."""
    url = "/api/health/"
    response = client.get(url)

    assert response.status_code == 200


@pytest.mark.django_db
def test_health_check_returns_expected_json(client):
    """Verify that the health endpoint returns the expected JSON."""
    url = "/api/health/"
    response = client.get(url)

    assert response.json() == {
        "status": "ok",
        "message": "Part-Time Job Matching API is running",
    }


@pytest.mark.django_db
def test_health_check_returns_json_content_type(client):
    """Verify that the health endpoint returns JSON content."""
    url = "/api/health/"
    response = client.get(url)

    assert response["Content-Type"] == "application/json"


@pytest.mark.django_db
def test_health_check_handles_head_request(client):
    """Verify that the health endpoint handles HEAD requests."""
    url = "/api/health/"
    response = client.head(url)

    assert response.status_code == 200
    assert response["Content-Type"] == "application/json"
    assert response.content == b""


@pytest.mark.django_db
def test_health_check_with_json_accept_header(client):
    """Verify that the endpoint accepts JSON requests."""
    url = "/api/health/"
    response = client.get(url, HTTP_ACCEPT="application/json")

    assert response.status_code == 200
    assert response["Content-Type"] == "application/json"


@pytest.mark.django_db
def test_health_check_with_html_accept_header(client):
    """Verify that the endpoint still returns JSON for HTML requests."""
    url = "/api/health/"
    response = client.get(url, HTTP_ACCEPT="text/html")

    assert response.status_code == 200
    assert response["Content-Type"] == "application/json"
