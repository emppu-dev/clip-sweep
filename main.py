import pyperclip
from plyer import notification
import time
import json

with open('config.json', 'r') as config_file:
    config = json.load(config_file)

clear_time = config["clear_time"]
notifications = config["notifications"]
clear_on_start = config["clear_on_start"]

def notify(message):
    if notifications:
        notification.notify(
            title="Clip Sweep",
            message=message,
            app_name="Clip Sweep",
            app_icon="icon.ico",
            timeout=3000
        )
    else:
        print(message)

current_clipboard_content = pyperclip.paste()
start_time = time.time()

notify("Clip Sweep is now running.")

if clear_on_start:
    time.sleep(clear_time)
    pyperclip.copy("")
    notify("Your clipboard has been cleared.")

while True:
    clipboard_content = pyperclip.paste()

    if clipboard_content and clipboard_content != current_clipboard_content:
        current_clipboard_content = clipboard_content
        start_time = time.time()

    if clipboard_content and time.time() - start_time >= clear_time:
        pyperclip.copy("")
        notify("Your clipboard has been cleared.")

    time.sleep(0.1)