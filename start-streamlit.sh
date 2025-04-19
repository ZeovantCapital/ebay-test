#!/bin/bash

# Activate virtual environment
source $(dirname "$0")/.venv/bin/activate

# Run Streamlit in headless mode on port 8501
streamlit run $(dirname "$0")/dashboard.py --server.port 8501 --server.headless true
