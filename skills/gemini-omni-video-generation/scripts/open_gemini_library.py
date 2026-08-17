r"""
Quick Browser Opener for Gemini Library & Videos
Opens the user's persistent Gemini profile in a normal Chrome window so they can see all generated videos in their Library.
"""

import os
import sys
import asyncio
from pathlib import Path

# Ensure UTF-8 output on Windows consoles
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

async def open_library(url: str = "https://gemini.google.com/library"):
    from playwright.async_api import async_playwright

    user_home = Path(os.environ.get("USERPROFILE", r"C:\Users\pichau"))
    automation_profile = user_home / ".gemini" / "chrome_automation_profile"

    print(f"🌐 Opening Gemini Library in Chrome: {url}")
    print("👉 Pressione CTRL+C quando terminar de navegar.")

    async with async_playwright() as p:
        context = await p.chromium.launch_persistent_context(
            user_data_dir=str(automation_profile),
            channel="chrome",
            headless=False,
            viewport={"width": 1920, "height": 1080},
            args=["--disable-blink-features=AutomationControlled"]
        )

        page = context.pages[0] if context.pages else await context.new_page()
        await page.goto(url)

        try:
            while True:
                await asyncio.sleep(1)
        except (asyncio.CancelledError, KeyboardInterrupt):
            pass

        await context.close()

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "https://gemini.google.com/library"
    asyncio.run(open_library(target))
