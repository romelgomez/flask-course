#!/bin/bash

# 
# This program created an isolated environment to have all dependencies 
#

# Get in PROJECT_FOLDER const the current folder where this program is currently running
PROJECT_FOLDER="$(pwd)"

VENV_DIR=${PROJECT_FOLDER}/./venv

# Create virtual environment directory 
python3 -m venv ./venv

# Check for virtual environment directory 
if [ -d "$VENV_DIR" ]; then
    # Active virtual environment 
    . ./venv/bin/activate
    # Install requirements
    pip install -r ./requirements.txt
    # Upgrade Pip
    pip install --upgrade pip
    python3 --version
    # Set ENVIRONMENT VAR for this project
    source bash_scripts/env.sh
    echo '.:ENVIRONMENT VAR:.'
    echo 'FLASK_APP: ' $FLASK_APP
    echo 'FLASK_DEBUG: ' $FLASK_DEBUG
else
    echo ERROR: ./venv it\'s not a valid folder
    exit 1
fi
 