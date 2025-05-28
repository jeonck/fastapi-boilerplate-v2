"""
API package initialization.

This module initializes the API package and provides
access to all API routers.
"""

from .health import router as health_router
from .users import router as users_router

__all__ = [
    "health_router",
    "users_router",
]
