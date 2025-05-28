"""
Test Main Application.

This module contains tests for the main application endpoints
and template rendering.
"""

import pytest
from fastapi.testclient import TestClient


def test_read_root(client: TestClient):
    """Test the root endpoint returns HTML."""
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    
    # Check if the response contains expected content
    content = response.text
    assert "FastAPI Template" in content
    assert "API Documentation" in content
    assert "/docs" in content
    assert "/redoc" in content


def test_favicon(client: TestClient):
    """Test the favicon endpoint."""
    response = client.get("/favicon.ico")
    assert response.status_code == 200
    
    data = response.json()
    assert "message" in data


def test_not_found_handler(client: TestClient):
    """Test the custom 404 handler."""
    response = client.get("/nonexistent-endpoint")
    assert response.status_code == 404
    # The 404 handler returns HTML template
    assert "text/html" in response.headers["content-type"]


def test_api_documentation_accessible(client: TestClient):
    """Test that API documentation endpoints are accessible."""
    # Test Swagger UI
    docs_response = client.get("/docs")
    assert docs_response.status_code == 200
    assert "text/html" in docs_response.headers["content-type"]
    
    # Test ReDoc
    redoc_response = client.get("/redoc")
    assert redoc_response.status_code == 200
    assert "text/html" in redoc_response.headers["content-type"]


def test_openapi_schema(client: TestClient):
    """Test that OpenAPI schema is available."""
    response = client.get("/openapi.json")
    assert response.status_code == 200
    
    schema = response.json()
    assert "openapi" in schema
    assert "info" in schema
    assert schema["info"]["title"] == "FastAPI Template"
