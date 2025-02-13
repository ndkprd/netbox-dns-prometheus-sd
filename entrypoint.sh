#!/bin/bash

# Start Nginx in the background
service nginx start

# Start the Python application
python3 scripts/run.py
