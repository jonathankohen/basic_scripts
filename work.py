"""Initializes necessary applications for daily routine"""

import subprocess
import webbrowser
import asyncio


async def zoom_app():
    subprocess.call(["/usr/bin/open", "/applications/zoom.us.app"])
    asyncio.sleep(2)
    # Rob's class
    webbrowser.open("https://codingdojo.zoom.us/j/81837621985")


async def work_apps():
    subprocess.call(["/usr/bin/open", "/applications/discord.app"])
    subprocess.call(["/usr/bin/open", "/applications/slack.app"])
    subprocess.call(["/usr/bin/open", "/applications/visual studio code.app"])
    asyncio.sleep(2)


async def social_apps():
    subprocess.call(["/usr/bin/open", "/system/applications/messages.app"])
    subprocess.call(["/usr/bin/open", "/applications/messenger.app"])
    subprocess.call(["/usr/bin/open", "/applications/whatsapp.app"])
    subprocess.call(["/usr/bin/open", "/applications/notes.app"])


async def main():
    await zoom_app()
    await work_apps()
    await social_apps()
    # Class schedule
    webbrowser.open(
        "https://docs.google.com/spreadsheets/d/1i1SZtY-hHB2yiSL-SP9QUheYVLvhsuOM15qa_9eVXJ0/edit?usp=sharing"
    )


if __name__ == "__main__":
    asyncio.run(main())