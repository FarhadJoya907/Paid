import os
import subprocess
import FKING
import time
import sys
from itertools import cycle

# Colors for terminal text (ANSI escape codes)
COLORS = ['\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m', '\033[96m', '\033[97m', '\033[0m']

def colorful_loading_animation(duration=20):
    # Cycle through colors for the animation
    end_time = time.time() + duration
    symbols = ['|', '/', '-', '\\']
    color_cycle = cycle(COLORS)  # Cycle through the colors

    while time.time() < end_time:
        for symbol in symbols:
            color = next(color_cycle)  # Get the next color
            os.system('clear')
            sys.stdout.write(f'\r{color}Loading... {symbol}\033[0m')  # Reset color with \033[0m
            sys.stdout.flush()
            time.sleep(0.25)

    sys.stdout.write('\r\033[92mLoading complete! \033[0m\n')  # Green "complete" message

try:
    # Display colorful loading animation for 20 seconds
    colorful_loading_animation()

    # Show that the tool is only for 64-bit systems
    print("\033[93mThis tool is only for 64-bit systems!\033[0m")

    # Open the provided WhatsApp link using the default web browser
   ## link = "https://chat.whatsapp.com/LrFY7kB8LkBDt09udn9c5S"

    # For Windows, macOS, or Linux
    if os.name == 'nt':  # Windows
        subprocess.run(["start", link], shell=True)
    elif os.name == 'posix':  # macOS/Linux
        subprocess.run(["xdg-open", link])  # For Linux or macOS, this will open the URL in the default browser

    print("▶️ Running main function...")
    Main()  # Assumes 'main' exists; will raise an error if it doesn't.

except ImportError as e:
    print("❌ Import error:", e)

except AttributeError:
    print("⚠️ 'main' function not found. Check available attributes:", dir(AUTRT))
