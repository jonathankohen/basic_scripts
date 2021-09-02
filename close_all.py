"""Initializes necessary applications for daily routine"""

import subprocess
import time


def zoom_app():
    subprocess.call(["osascript", "-e", 'tell application "Zoom" to quit'])


def work_apps():
    subprocess.call(["osascript", "-e", 'tell application "Discord" to quit'])
    subprocess.call(["osascript", "-e", 'tell application "Slack" to quit'])
    subprocess.call(["osascript", "-e", 'tell application "Visual Studio Code" to quit'])


def social_apps():
    subprocess.call(["osascript", "-e", 'tell applicat998ion "Messages" to quit'])
    subprocess.call(["osascript", "-e", 'tell application "Messenger" to quit'])
    subprocess.call(["osascript", "-e", 'tell application "WhatsApp" to quit'])
    subprocess.call(["osascript", "-e", 'tell application "Notes" to quit'])


def main():
    work_apps()
    social_apps()
    zoom_app()


if __name__ == "__main__":
    main()