#!/bin/bash

# FastAPI Template Quick Run Script
# This script sets up and runs the FastAPI application using uv

set -e  # Exit on any error

echo "🚀 FastAPI Template Quick Start"
echo "================================"

# Check if uv is installed
if ! command -v uv &> /dev/null; then
    echo "❌ uv is not installed. Please install uv first:"
    echo "   curl -LsSf https://astral.sh/uv/install.sh | sh"
    exit 1
fi

# Function to check if virtual environment exists
check_venv() {
    if [ -d ".venv" ]; then
        echo "✅ Virtual environment found"
        return 0
    else
        echo "📦 Creating virtual environment..."
        return 1
    fi
}

# Function to install dependencies
install_deps() {
    echo "📋 Installing dependencies..."
    uv sync
    echo "✅ Dependencies installed"
}

# Function to run the application
run_app() {
    echo "🔥 Starting FastAPI application..."
    echo "   Server will be available at: http://localhost:8000"
    echo "   API Documentation: http://localhost:8000/docs"
    echo "   Template Page: http://localhost:8000/"
    echo ""
    echo "Press Ctrl+C to stop the server"
    echo ""
    
    uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
}

# Main execution flow
main() {
    # Check and create virtual environment if needed
    if ! check_venv; then
        uv venv
        echo "✅ Virtual environment created"
    fi
    
    # Install dependencies
    install_deps
    
    # Run the application
    run_app
}

# Handle script arguments
case "${1:-}" in
    "install")
        echo "📦 Installing dependencies only..."
        if ! check_venv; then
            uv venv
            echo "✅ Virtual environment created"
        fi
        install_deps
        echo "✅ Setup complete! Run './run.sh' to start the server."
        ;;
    "dev")
        echo "🔧 Starting in development mode with auto-reload..."
        main
        ;;
    "test")
        echo "🧪 Running tests..."
        if ! check_venv; then
            echo "❌ Virtual environment not found. Run './run.sh install' first."
            exit 1
        fi
        uv run pytest
        ;;
    "clean")
        echo "🧹 Cleaning up..."
        if [ -d ".venv" ]; then
            rm -rf .venv
            echo "✅ Virtual environment removed"
        fi
        if [ -d "__pycache__" ]; then
            find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
            echo "✅ Cache files removed"
        fi
        echo "✅ Cleanup complete"
        ;;
    "help"|"-h"|"--help")
        echo "Usage: ./run.sh [command]"
        echo ""
        echo "Commands:"
        echo "  (none)    - Set up and run the FastAPI application"
        echo "  install   - Only install dependencies"
        echo "  dev       - Run in development mode (same as no args)"
        echo "  test      - Run tests"
        echo "  clean     - Remove virtual environment and cache files"
        echo "  help      - Show this help message"
        echo ""
        echo "First time setup:"
        echo "  chmod +x run.sh"
        echo "  ./run.sh"
        ;;
    *)
        main
        ;;
esac
