#!/bin/bash

# Quick test script to verify FastAPI application is working
echo "🧪 Testing FastAPI Template..."

# Start the server in background
echo "Starting server..."
./run.sh > server.log 2>&1 &
SERVER_PID=$!

# Wait for server to start
echo "Waiting for server to start..."
sleep 5

# Test health endpoint
echo "Testing health endpoint..."
curl -s http://localhost:8000/api/health/ | grep -q "healthy" && echo "✅ Health check passed" || echo "❌ Health check failed"

# Test main page
echo "Testing main page..."
curl -s http://localhost:8000/ | grep -q "FastAPI Template" && echo "✅ Main page loaded" || echo "❌ Main page failed"

# Test API docs
echo "Testing API docs..."
curl -s http://localhost:8000/docs | grep -q "swagger" && echo "✅ API docs accessible" || echo "❌ API docs failed"

# Clean up
echo "Stopping server..."
kill $SERVER_PID
rm -f server.log

echo "✅ All tests completed!"
