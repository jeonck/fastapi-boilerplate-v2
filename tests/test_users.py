"""
Test User API endpoints.

This module contains tests for user-related API endpoints including
CRUD operations.
"""

import pytest
from fastapi.testclient import TestClient


def test_get_users(client: TestClient):
    """Test getting all users."""
    response = client.get("/api/users/")
    assert response.status_code == 200
    
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 2  # We have 2 default users


def test_get_users_with_pagination(client: TestClient):
    """Test getting users with pagination parameters."""
    response = client.get("/api/users/?skip=0&limit=1")
    assert response.status_code == 200
    
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 1


def test_get_user_by_id(client: TestClient):
    """Test getting a specific user by ID."""
    response = client.get("/api/users/1")
    assert response.status_code == 200
    
    data = response.json()
    assert data["id"] == 1
    assert "username" in data
    assert "email" in data
    assert "created_at" in data


def test_get_user_by_id_not_found(client: TestClient):
    """Test getting a non-existent user."""
    response = client.get("/api/users/999")
    assert response.status_code == 404
    
    data = response.json()
    assert "detail" in data


def test_get_user_by_username(client: TestClient):
    """Test getting a user by username."""
    response = client.get("/api/users/username/admin")
    assert response.status_code == 200
    
    data = response.json()
    assert data["username"] == "admin"


def test_get_user_by_username_not_found(client: TestClient):
    """Test getting a non-existent user by username."""
    response = client.get("/api/users/username/nonexistent")
    assert response.status_code == 404


def test_create_user(client: TestClient, sample_user_data):
    """Test creating a new user."""
    response = client.post("/api/users/", json=sample_user_data)
    assert response.status_code == 201
    
    data = response.json()
    assert data["username"] == sample_user_data["username"]
    assert data["email"] == sample_user_data["email"]
    assert data["full_name"] == sample_user_data["full_name"]
    assert "id" in data
    assert "created_at" in data


def test_create_user_duplicate_username(client: TestClient):
    """Test creating a user with duplicate username."""
    user_data = {
        "username": "admin",  # This already exists
        "email": "newemail@example.com",
        "password": "newpassword123"
    }
    
    response = client.post("/api/users/", json=user_data)
    assert response.status_code == 400
    
    data = response.json()
    assert "already exists" in data["detail"]


def test_update_user(client: TestClient, sample_user_update_data):
    """Test updating an existing user."""
    response = client.put("/api/users/1", json=sample_user_update_data)
    assert response.status_code == 200
    
    data = response.json()
    assert data["full_name"] == sample_user_update_data["full_name"]
    assert data["email"] == sample_user_update_data["email"]
    assert "updated_at" in data


def test_update_user_not_found(client: TestClient, sample_user_update_data):
    """Test updating a non-existent user."""
    response = client.put("/api/users/999", json=sample_user_update_data)
    assert response.status_code == 404


def test_delete_user(client: TestClient, sample_user_data):
    """Test deleting a user."""
    # First create a user
    create_response = client.post("/api/users/", json=sample_user_data)
    assert create_response.status_code == 201
    user_id = create_response.json()["id"]
    
    # Then delete it
    delete_response = client.delete(f"/api/users/{user_id}")
    assert delete_response.status_code == 200
    
    data = delete_response.json()
    assert data["success"] is True
    assert "deleted" in data["message"]


def test_delete_user_not_found(client: TestClient):
    """Test deleting a non-existent user."""
    response = client.delete("/api/users/999")
    assert response.status_code == 404
