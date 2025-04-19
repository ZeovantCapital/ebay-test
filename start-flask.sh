#!/bin/bash

# Activate virtual environment
source $(dirname "$0")/.venv/bin/activate

# Navigate to the Flask app folder
cd $(dirname "$0")/ebay-notify

# Run with Gunicorn
gunicorn --bind 127.0.0.1:5000 app:app
