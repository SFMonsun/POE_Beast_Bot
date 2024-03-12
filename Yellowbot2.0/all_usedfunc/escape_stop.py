import keyboard
import sys
def should_continue():
    if keyboard.is_pressed('esc'):
        print("Escape pressed, stopping...")
        sys.exit()