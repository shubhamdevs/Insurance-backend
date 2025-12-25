#!/bin/bash
cd "$(dirname "$0")"
source venv/bin/activate
export API_PORT=5001
python app.py
