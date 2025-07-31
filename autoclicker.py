#!/usr/bin/env python3
"""
Mac Autoclicker
A simple autoclicker that can be toggled on/off with a key press
"""

import time
import threading
import sys
from pynput import keyboard, mouse
from pynput.mouse import Button
import pyautogui

class AutoClicker:
    def __init__(self):
        self.is_running = False
        self.click_thread = None
        self.cps = 1.0  # Current CPS
        self.min_interval = 0.033  # Minimum interval between clicks (33ms for up to 30 CPS)
        
        # Pyautogui's fail-safe, stops script when mouse is moved to top left corner
        pyautogui.FAILSAFE = True
        
        # Set up keyboard listener
        self.keyboard_listener = keyboard.Listener(on_press=self.on_key_press)

        # Print controls
        print("  F6 - Toggle autoclicker on/off")
        print("  F7 - Increase CPS")
        print("  F8 - Decrease CPS")
        print("  F9 - Quit")
        print(f"Current CPS: {self.cps} (Max: 30)")
    
    def on_key_press(self, key):
        try:
            if key == keyboard.Key.f6:
                self.toggle_clicking()
            elif key == keyboard.Key.f7:
                self.increase_cps()
            elif key == keyboard.Key.f8:
                self.decrease_cps()
            elif key == keyboard.Key.f9:
                self.quit_clicker()
        except AttributeError:
            pass
    
    def toggle_clicking(self):
        if self.is_running:
            self.stop_clicking()
        else:
            self.start_clicking()
    
    def start_clicking(self):
        # Added redundancy to prevent multiple threads from being created
        if not self.is_running:
            self.is_running = True
            # Let specific task run in background while main program runs, rest of program doesn't wait
            # daemon=True causes thread to end when main thread exits
            self.click_thread = threading.Thread(target=self.click_loop, daemon=True)
            self.click_thread.start()
            print(f"Autoclicker STARTED - CPS: {self.cps}")
    
    def stop_clicking(self):
        #Redundancy to prevent multiple threads from being created
        if self.is_running:
            self.is_running = False
            if self.click_thread:
                # Wait for thread to finish, timeout after 0.1 seconds
                self.click_thread.join(timeout=0.1)
            print("Autoclicker STOPPED")
    
    def click_loop(self):
        click_count = 0
        while self.is_running:
            try:
                # Calculate interval based on CPS, min interval to control clicks per second
                interval = max(1.0 / self.cps, self.min_interval)
                
                # Perform click 
                pyautogui.click()
                
                # Increment click counter and print every 20 click, debugging
                click_count += 1
                if click_count % 20 == 0:
                    print(f"Click count: {click_count}")

                # Debugging to see if clicks are being made
                time.sleep(interval)
            except Exception as e:
                print(f"Error in click loop: {e}")
                break
    
    def increase_cps(self):
        if self.cps < 30.0:  # Max 30 CPS
            self.cps += 1
            print(f"CPS increased to: {self.cps}")
        else:
            print("CPS already at maximum (30)")
    
    def decrease_cps(self):
        if self.cps > 1:  # Min 1 CPS
            self.cps -= 1
            print(f"CPS decreased to: {self.cps}")
        else:
            print("CPS already at minimum (1)")
    
    def quit_clicker(self):
        print("Quitting autoclicker...")
        self.stop_clicking()
        self.keyboard_listener.stop()
        #exit successfully
        sys.exit(0)
    
    def run(self):
        """Start the autoclicker"""
        try:
            self.keyboard_listener.start()
            self.keyboard_listener.join()
        #ctrl C to quit
        except KeyboardInterrupt:
            print("\nQuitting...")
            self.quit_clicker()

def main():
    """Main function"""
    try:
        clicker = AutoClicker()
        clicker.run()
    except Exception as e:
        print(f"Error: {e}")
        #back to terminal
        sys.exit(1)

#makes code importable by other scripts without running main()
if __name__ == "__main__":
    main() 