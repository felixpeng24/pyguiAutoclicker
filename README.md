# Mac Autoclicker

A simple Python-based autoclicker for macOS that can be toggled on/off with keyboard shortcuts and allows you to adjust the clicks per second (CPS).

## Features

- **Toggle On/Off**: Press F6 to start/stop the autoclicker
- **Adjustable CPS**: Use F7 to increase and F8 to decrease clicks per second
- **Safe Limits**: CPS ranges from 0.5 to 30.0 clicks per second
- **Easy Quit**: Press F9 to quit the program
- **Thread-Safe**: Uses threading to prevent blocking

## Installation

1. **Install Python 3** (if not already installed):
   ```bash
   # Using Homebrew (recommended)
   brew install python3
   ```

2. **Run the setup script**:
   ```bash
   chmod +x setup.sh
   ./setup.sh
   ```

   Or manually install dependencies:
   ```bash
   pip3 install -r requirements.txt
   chmod +x autoclicker.py
   ```

## Usage

1. **Run the autoclicker**:
   ```bash
   python3 autoclicker.py
   ```

2. **Controls**:
   - **F6**: Toggle autoclicker on/off
   - **F7**: Increase CPS (clicks per second)
   - **F8**: Decrease CPS (clicks per second)
   - **F9**: Quit the program

3. **Position your cursor** where you want the clicks to occur, then press F6 to start.

## Important Notes

### Accessibility Permissions
On macOS, you may need to grant accessibility permissions to your terminal application:

1. Go to **System Preferences** > **Security & Privacy** > **Privacy** > **Accessibility**
2. Click the lock icon to make changes
3. Add your terminal application (Terminal, iTerm2, etc.) to the list
4. Check the box next to your terminal application

### Safety Features
- Minimum interval between clicks: 33ms (prevents excessive clicking)
- Maximum CPS: 30.0 (prevents system overload)
- Failsafe disabled for better control
- Clean shutdown with F9 or Ctrl+C

## Troubleshooting

### "Permission denied" errors
- Make sure you've granted accessibility permissions as described above
- Try running with `sudo python3 autoclicker.py` (not recommended for security reasons)

### Clicks not working
- Check that your terminal has accessibility permissions
- Try clicking in a different application
- Restart the terminal application

### Program not responding
- Press F9 to quit cleanly
- If that doesn't work, use Ctrl+C in the terminal

## Requirements

- macOS 10.14 or later
- Python 3.6 or later
- Required Python packages (installed automatically):
  - `pyautogui` - For mouse clicking
  - `pynput` - For keyboard input

## Disclaimer

This tool is for educational and personal use only. Please use responsibly and in accordance with your local laws and the terms of service of any applications you use it with. 