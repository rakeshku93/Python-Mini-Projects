"""Launches a map in the browser using **an address** from the command line or clipboard using **webbrowser**"""
import webbrowser
import time
import sys
import pyperclip


if len(sys.argv) > 1:
    address = " ".join(sys.argv[1:])
    print(f"{address = }")
    
else:
    address = pyperclip.paste()

if __name__ == "__main__":
    webbrowser.open(f"https://www.google.com/maps/place/{address}")