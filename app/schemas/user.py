"""
User Schemas

This module contains Pydantic models for user-related operations.
"""

from typing import Optional
from pydantic import BaseModel, Field, EmailStr
from .base import BaseSchema, TimestampMixin


class UserBase(BaseSchema):
    """Base user schema."""
    
    username: str = Field(..., min_length=3, max_length=50, description="Username")
    email: EmailStr = Field(..., description="User email address")
    full_name: Optional[str] = Field(None, max_length=100, description="Full name")
    is_active: bool = Field(True, description="User active status")


class UserCreate(UserBase):
    """Schema for creating a new user."""
    
    password: str = Field(..., min_length=8, description="User password")


class UserUpdate(BaseModel):
    """Schema for updating user information."""
    
    username: Optional[str] = Field(None, min_length=3, max_length=50)
    email: Optional[EmailStr] = None
    full_name: Optional[str] = Field(None, max_length=100)
    is_active: Optional[bool] = None


class UserResponse(UserBase, TimestampMixin):
    """Schema for user response."""
    
    id: int = Field(..., description="User ID")
    
    model_config = {"from_attributes": True}


class UserLogin(BaseModel):
    """Schema for user login."""
    
    username: str = Field(..., description="Username or email")
    password: str = Field(..., description="User password")
