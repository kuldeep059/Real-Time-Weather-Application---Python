#!/bin/bash

echo "🚀 Setting up the Flask Weather App..."

# Create virtual env
python -m venv venv
source venv/bin/activate || source venv/Scripts/activate

# Install dependencies
pip install -r requirements.txt

# Setup MongoDB indexes using a Python script
python create_indexes.py

echo "✅ Setup complete!"
