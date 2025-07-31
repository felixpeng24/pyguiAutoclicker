#!/bin/bash

echo "Setting up Mac Autoclicker..."

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed. Please install Python 3 first."
    exit 1
fi

# Install required packages
echo "Installing required packages..."
pip3 install -r requirements.txt

# Make the autoclicker executable
chmod +x autoclicker.py

echo "Setup complete!"
echo ""
echo "To run the autoclicker:"
echo "  python3 autoclicker.py"
echo ""
echo "Controls:"
echo "  F6 - Toggle autoclicker on/off"
echo "  F7 - Increase CPS"
echo "  F8 - Decrease CPS"
echo "  F9 - Quit"
echo ""
echo "Note: You may need to grant accessibility permissions to Terminal/your terminal app"
echo "in System Preferences > Security & Privacy > Privacy > Accessibility" 