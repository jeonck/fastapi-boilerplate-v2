"""
User Service

This module contains business logic for user-related operations.
"""

from typing import List, Optional
from datetime import datetime
from app.schemas.user import UserCreate, UserResponse, UserUpdate


class UserService:
    """Service class for user operations."""
    
    def __init__(self):
        # In a real application, this would be a database
        self._users_db = [
            {
                "id": 1,
                "username": "admin",
                "email": "admin@example.com",
                "full_name": "Administrator",
                "is_active": True,
                "created_at": datetime.utcnow(),
                "updated_at": datetime.utcnow(),
            },
            {
                "id": 2,
                "username": "user",
                "email": "user@example.com", 
                "full_name": "Regular User",
                "is_active": True,
                "created_at": datetime.utcnow(),
                "updated_at": datetime.utcnow(),
            }
        ]
    
    async def get_users(self, skip: int = 0, limit: int = 100) -> List[UserResponse]:
        """Get all users with pagination."""
        users = self._users_db[skip:skip + limit]
        return [UserResponse(**user) for user in users]
    
    async def get_user_by_id(self, user_id: int) -> Optional[UserResponse]:
        """Get user by ID."""
        user = next((u for u in self._users_db if u["id"] == user_id), None)
        return UserResponse(**user) if user else None
    
    async def get_user_by_username(self, username: str) -> Optional[UserResponse]:
        """Get user by username."""
        user = next((u for u in self._users_db if u["username"] == username), None)
        return UserResponse(**user) if user else None
    
    async def create_user(self, user_data: UserCreate) -> UserResponse:
        """Create a new user."""
        new_id = max(u["id"] for u in self._users_db) + 1 if self._users_db else 1
        new_user = {
            "id": new_id,
            "username": user_data.username,
            "email": user_data.email,
            "full_name": user_data.full_name,
            "is_active": user_data.is_active,
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow(),
        }
        self._users_db.append(new_user)
        return UserResponse(**new_user)
    
    async def update_user(self, user_id: int, user_data: UserUpdate) -> Optional[UserResponse]:
        """Update an existing user."""
        user_index = next(
            (i for i, u in enumerate(self._users_db) if u["id"] == user_id), None
        )
        
        if user_index is None:
            return None
        
        user = self._users_db[user_index]
        update_data = user_data.model_dump(exclude_unset=True)
        
        for field, value in update_data.items():
            user[field] = value
        
        user["updated_at"] = datetime.utcnow()
        self._users_db[user_index] = user
        
        return UserResponse(**user)
    
    async def delete_user(self, user_id: int) -> bool:
        """Delete a user."""
        user_index = next(
            (i for i, u in enumerate(self._users_db) if u["id"] == user_id), None
        )
        
        if user_index is None:
            return False
        
        del self._users_db[user_index]
        return True
    
    async def authenticate_user(self, username: str, password: str) -> Optional[UserResponse]:
        """Authenticate user (mock implementation)."""
        # In a real application, you would verify the password hash
        user = await self.get_user_by_username(username)
        if user and user.is_active:
            # Mock password check - in real app, use proper password hashing
            return user
        return None


# Global service instance
user_service = UserService()


def get_user_service() -> UserService:
    """Get user service instance."""
    return user_service
