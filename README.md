# FastAPI Template V2

A modern, production-ready FastAPI template with UV package management, Jinja2 templates, and one-command deployment.

## 🚀 Features

- **FastAPI** with async support and automatic API documentation
- **UV** for lightning-fast dependency management and virtual environments
- **Jinja2** templating engine with Bootstrap 5 UI components
- **Pydantic** for robust data validation and serialization
- **Structured project layout** following FastAPI best practices
- **One-command deployment** with `./run.sh`
- **Environment configuration** with `.env` files
- **Comprehensive testing** with pytest
- **API documentation** with Swagger UI and ReDoc
- **Template pages** with API access examples

## 📁 Project Structure

```
fastapi-template-v2/
├── app/
│   ├── api/                 # API route handlers
│   │   ├── health.py       # Health check endpoints
│   │   └── users.py        # User CRUD endpoints
│   ├── core/               # Core application configuration
│   │   └── config.py       # Settings and configuration
│   ├── models/             # Database models (if needed)
│   ├── schemas/            # Pydantic models for request/response
│   │   ├── base.py         # Base schemas
│   │   └── user.py         # User schemas
│   ├── services/           # Business logic layer
│   │   └── user_service.py # User service
│   ├── static/             # Static files (CSS, JS, images)
│   │   ├── css/
│   │   └── js/
│   ├── templates/          # Jinja2 HTML templates
│   │   ├── base.html       # Base template
│   │   └── index.html      # Main page template
│   └── main.py             # FastAPI application entry point
├── tests/                  # Test modules
├── .env                    # Environment variables
├── .env.example           # Environment variables example
├── pyproject.toml         # Project configuration and dependencies
├── run.sh                 # One-command deployment script
└── README.md              # This file
```

## 🛠 Quick Start

### Prerequisites

- Python 3.9+
- [UV](https://docs.astral.sh/uv/) package manager

Install UV if you haven't already:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Installation & Running

1. **Make the run script executable:**
   ```bash
   chmod +x run.sh
   ```

2. **Start the application:**
   ```bash
   ./run.sh
   ```
   
   This single command will:
   - Create a virtual environment if it doesn't exist
   - Install all dependencies
   - Start the FastAPI server with auto-reload

3. **Access your application:**
   - Main page: http://localhost:8000
   - API Documentation (Swagger): http://localhost:8000/docs
   - Alternative API docs (ReDoc): http://localhost:8000/redoc

## 🎯 Available Commands

The `run.sh` script supports multiple commands:

```bash
./run.sh          # Set up and run the application (default)
./run.sh install  # Only install dependencies
./run.sh dev      # Run in development mode (same as default)
./run.sh test     # Run all tests
./run.sh clean    # Remove virtual environment and cache files
./run.sh help     # Show help information
```

## 🌐 API Endpoints

### Health Checks
- `GET /api/health/` - Application health status
- `GET /api/health/ping` - Simple ping endpoint
- `GET /api/health/info` - Application information

### Users (Example CRUD)
- `GET /api/users/` - List all users (with pagination)
- `GET /api/users/{id}` - Get user by ID
- `GET /api/users/username/{username}` - Get user by username
- `POST /api/users/` - Create new user
- `PUT /api/users/{id}` - Update user
- `DELETE /api/users/{id}` - Delete user

## 🎨 Template Features

The included HTML templates provide:

- **Responsive Bootstrap 5 design**
- **Interactive API testing** directly from the web interface
- **Real-time health monitoring**
- **Direct links to API documentation**
- **Modern, professional UI/UX**

## ⚙️ Configuration

Configuration is handled through environment variables in `.env` file:

```env
# Application Settings
APP_NAME="FastAPI Template"
APP_VERSION="0.1.0"
DEBUG=True
ENVIRONMENT=development

# Server Settings  
HOST=0.0.0.0
PORT=8000

# CORS Settings
ALLOWED_ORIGINS=["http://localhost:3000", "http://localhost:8000"]
```

Copy `.env.example` to `.env` and modify as needed.

## 🧪 Testing

Run the test suite:

```bash
./run.sh test
```

Or manually with UV:

```bash
uv run pytest
```

Tests include:
- API endpoint testing
- Schema validation
- Error handling
- Template rendering

## 🚀 Deployment

### Development
```bash
./run.sh
```

### Production
For production deployment, consider:

1. Set `DEBUG=False` in `.env`
2. Configure proper `SECRET_KEY`
3. Use a production ASGI server like Gunicorn:
   ```bash
   uv run gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker
   ```

## 📚 Development Guide

### Adding New API Endpoints

1. Create a new router in `app/api/`
2. Define schemas in `app/schemas/`
3. Implement business logic in `app/services/`
4. Include the router in `app/main.py`
5. Add tests in `tests/`

### Adding New Templates

1. Create HTML templates in `app/templates/`
2. Add static files (CSS/JS) in `app/static/`
3. Create template routes in your API modules

### Environment Variables

All configuration should use environment variables defined in `app/core/config.py`.

## 🔧 Customization

This template is designed to be easily customizable:

- **Modify `app/core/config.py`** for configuration options
- **Update `app/templates/`** for UI changes
- **Extend `app/api/`** for new API endpoints
- **Add to `app/services/`** for business logic
- **Configure `pyproject.toml`** for dependencies

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass
6. Submit a pull request

## 💡 Tips

- Use the interactive template page to test your API endpoints
- Check the health endpoints to monitor your application
- The template includes examples for common FastAPI patterns
- UV is much faster than pip for dependency management
- The project structure follows FastAPI recommended practices

---

**Happy coding! 🎉**
# fastapi-boilerplate-v2
