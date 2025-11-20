#!/bin/bash
# Run the Universe Map Generator Web App

cd "$(dirname "$0")"

# Check if venv exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    source venv/bin/activate
    echo "Installing dependencies..."
    pip install -r requirements.txt
else
    source venv/bin/activate
fi

# Run the Flask app
echo ""
echo "🚀 Starting Universe Map Generator Web App..."
echo "================================================"
echo ""
python app.py

