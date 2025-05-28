"""
Application Configuration Settings

This module handles all configuration settings for the FastAPI application,
including environment variables, database settings, and other configuration options.
"""

import os
from typing import List, Optional
from pydantic_settings import BaseSettings
from pydantic import field_validator


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""
    
    # Application Information
    app_name: str = "FastAPI Template"
    app_version: str = "0.1.0"
    app_description: str = "A FastAPI template with Jinja2 templates"
    
    # Server Configuration
    host: str = "0.0.0.0"
    port: int = 8000
    debug: bool = True
    environment: str = "development"
    
    # CORS Configuration
    allowed_origins: List[str] = [
        "http://localhost:3000",
        "http://localhost:8000", 
        "http://127.0.0.1:8000"
    ]
    allowed_methods: List[str] = ["*"]
    allowed_headers: List[str] = ["*"]
    
    # Logging Configuration
    log_level: str = "INFO"
    
    # Database Configuration (Optional)
    database_url: Optional[str] = None
    
    # Security Configuration (Optional)
    secret_key: Optional[str] = None
    access_token_expire_minutes: int = 30
    
    @field_validator('allowed_origins', mode='before')
    @classmethod
    def parse_cors_origins(cls, v):
        if isinstance(v, str):
            return [origin.strip() for origin in v.split(',')]
        return v
    
    @field_validator('allowed_methods', mode='before')
    @classmethod
    def parse_cors_methods(cls, v):
        if isinstance(v, str):
            return [method.strip() for method in v.split(',')]
        return v
    
    @field_validator('allowed_headers', mode='before')
    @classmethod
    def parse_cors_headers(cls, v):
        if isinstance(v, str):
            return [header.strip() for header in v.split(',')]
        return v
    
    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
        "case_sensitive": False
    }


# Global settings instance
settings = Settings()


def get_settings() -> Settings:
    """Get application settings instance."""
    return settings
