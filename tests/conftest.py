"""
Test configuration and fixtures.

This module contains pytest configuration and common fixtures
used across all test modules.
"""

import uuid
import pytest
from fastapi.testclient import TestClient
from app.main import app


@pytest.fixture
def client():
    """Create a test client for the FastAPI application."""
    return TestClient(app)


@pytest.fixture
def sample_user_data():
    """Sample user data for testing."""
    unique_id = str(uuid.uuid4())[:8]
    return {
        "username": f"testuser_{unique_id}",
        "email": f"test_{unique_id}@example.com",
        "full_name": "Test User",
        "password": "testpassword123"
    }


@pytest.fixture
def sample_user_update_data():
    """Sample user update data for testing."""
    return {
        "full_name": "Updated Test User",
        "email": "updated@example.com"
    }
