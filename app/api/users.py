"""
User API Routes

This module contains all user-related API endpoints including
CRUD operations for user management.
"""

from typing import List
from fastapi import APIRouter, Depends, HTTPException, Query, status
from app.schemas.user import UserResponse, UserCreate, UserUpdate
from app.schemas.base import SuccessResponse, ErrorResponse
from app.services.user_service import UserService, get_user_service

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/", response_model=List[UserResponse])
async def get_users(
    skip: int = Query(0, ge=0, description="Number of users to skip"),
    limit: int = Query(100, ge=1, le=1000, description="Maximum number of users to return"),
    user_service: UserService = Depends(get_user_service)
):
    """
    Get all users with pagination.
    
    - **skip**: Number of users to skip (for pagination)
    - **limit**: Maximum number of users to return
    """
    users = await user_service.get_users(skip=skip, limit=limit)
    return users


@router.get("/{user_id}", response_model=UserResponse)
async def get_user(
    user_id: int,
    user_service: UserService = Depends(get_user_service)
):
    """
    Get a specific user by ID.
    
    - **user_id**: The ID of the user to retrieve
    """
    user = await user_service.get_user_by_id(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID {user_id} not found"
        )
    return user


@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(
    user_data: UserCreate,
    user_service: UserService = Depends(get_user_service)
):
    """
    Create a new user.
    
    - **user_data**: User information including username, email, and password
    """
    # Check if username already exists
    existing_user = await user_service.get_user_by_username(user_data.username)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists"
        )
    
    new_user = await user_service.create_user(user_data)
    return new_user


@router.put("/{user_id}", response_model=UserResponse)
async def update_user(
    user_id: int,
    user_data: UserUpdate,
    user_service: UserService = Depends(get_user_service)
):
    """
    Update an existing user.
    
    - **user_id**: The ID of the user to update
    - **user_data**: Updated user information
    """
    updated_user = await user_service.update_user(user_id, user_data)
    if not updated_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID {user_id} not found"
        )
    return updated_user


@router.delete("/{user_id}", response_model=SuccessResponse)
async def delete_user(
    user_id: int,
    user_service: UserService = Depends(get_user_service)
):
    """
    Delete a user.
    
    - **user_id**: The ID of the user to delete
    """
    success = await user_service.delete_user(user_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID {user_id} not found"
        )
    
    return SuccessResponse(
        message=f"User with ID {user_id} successfully deleted"
    )


@router.get("/username/{username}", response_model=UserResponse)
async def get_user_by_username(
    username: str,
    user_service: UserService = Depends(get_user_service)
):
    """
    Get a user by username.
    
    - **username**: The username to search for
    """
    user = await user_service.get_user_by_username(username)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with username '{username}' not found"
        )
    return user
