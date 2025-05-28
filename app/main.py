"""
FastAPI Application Main Module

This is the main entry point for the FastAPI application.
It sets up the FastAPI instance, includes routers, configures middleware,
and provides template rendering capabilities.
"""

from contextlib import asynccontextmanager
from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
import logging
from pathlib import Path

from app.core.config import Settings, get_settings
from app.api import health_router, users_router

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Get application settings
settings = get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan events."""
    # Startup
    logger.info(f"Starting {settings.app_name} v{settings.app_version}")
    logger.info(f"Environment: {settings.environment}")
    logger.info(f"Debug mode: {settings.debug}")
    
    yield
    
    # Shutdown
    logger.info(f"Shutting down {settings.app_name}")

# Create FastAPI application instance
app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description=settings.app_description,
    debug=settings.debug,
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan,
)

# Configure CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_credentials=True,
    allow_methods=settings.allowed_methods,
    allow_headers=settings.allowed_headers,
)

# Setup static files
app.mount(
    "/static", 
    StaticFiles(directory=Path(__file__).parent / "static"), 
    name="static"
)

# Setup templates
templates = Jinja2Templates(directory=Path(__file__).parent / "templates")

# Include API routers
app.include_router(health_router, prefix="/api")
app.include_router(users_router, prefix="/api")


@app.get("/", response_class=HTMLResponse)
async def read_root(
    request: Request, 
    settings: Settings = Depends(get_settings)
):
    """
    Render the main template page.
    
    This endpoint serves the main HTML template with links to the API documentation.
    """
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "app_name": settings.app_name,
            "app_version": settings.app_version,
            "app_description": settings.app_description,
            "environment": settings.environment,
        }
    )


@app.get("/favicon.ico")
async def favicon():
    """Return a simple favicon response."""
    return {"message": "No favicon configured"}


# Custom exception handlers
@app.exception_handler(404)
async def not_found_handler(request: Request, exc):
    """Custom 404 error handler for API endpoints."""
    # Check if this is an API request
    if request.url.path.startswith("/api/"):
        return JSONResponse(
            status_code=404,
            content={"detail": "Not found"}
        )
    
    # For non-API requests, return HTML template
    return templates.TemplateResponse(
        request=request,
        name="base.html",
        context={
            "app_name": settings.app_name,
            "app_version": settings.app_version,
            "environment": settings.environment,
        },
        status_code=404
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host=settings.host,
        port=settings.port,
        reload=settings.debug,
        log_level=settings.log_level.lower(),
    )
