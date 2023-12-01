#!/bin/sh

set -e

echo "Installing pipx if it's not installed..."
which pipx || brew install pipx

echo "Installing poetry if it's not installed..."
which poetry || pipx install "poetry>=1.3.0,<1.4.0"

echo "Configure poetry to create virtual environment outside of project folder, in default poetry virtualenvs location."
poetry config virtualenvs.in-project false

echo "Installing dependencies..."
poetry install

echo "Done. Configure your IDE to use the following virtual environment path: $(poetry env info -p)/bin/python"