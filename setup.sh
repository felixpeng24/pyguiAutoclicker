#!/bin/bash

# Install required packages
echo "Installing required packages..."
pip3 install -r requirements.txt

# Make the autoclicker executable
chmod +x autoclicker.py

echo "Setup complete!"