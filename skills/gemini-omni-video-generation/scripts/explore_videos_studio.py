r"""
Explore and Generate directly via Gemini Pro 'https://gemini.google.com/videos'
Navigates directly to the dedicated Videos tool URL, inspects UI controls, injects the prompt, and downloads the output.
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

async def main():
    from playwright.async_api import async_playwright

    user_home = Path(os.environ.get("USERPROFILE", r"C:\Users\pichau"))
    automation_profile = user_home / ".gemini" / "chrome_automation_profile"

    print("🚀 [Videos Studio] Navigating directly to https://gemini.google.com/videos...")

    async with async_playwright() as p:
        context = await p.chromium.launch_persistent_context(
            user_data_dir=str(automation_profile),
            channel="chrome",
            headless=True,
            viewport={"width": 1920, "height": 1080},
            args=["--disable-blink-features=AutomationControlled"]
        )

        page = context.pages[0] if context.pages else await context.new_page()
        await page.goto("https://gemini.google.com/videos", wait_until="domcontentloaded")
        await asyncio.sleep(5)

        current_url = page.url
        print(f"🌐 [Videos Studio] Current URL: {current_url}")

        # Capture screenshot of the Videos Studio UI
        shot_path = Path(r"C:\Users\pichau\Documents\antigravity\proud-babbage\assets\videos\gemini_videos_studio_ui.png")
        await page.screenshot(path=str(shot_path))
        print(f"📸 [Videos Studio] UI Screenshot saved to: {shot_path}")

        # List all interactive buttons and inputs
        elements = await page.evaluate(r"""
            () => {
                const items = Array.from(document.querySelectorAll('button, input, textarea, div[role="button"], rich-textarea, select, [aria-label]'))
                    .map(el => ({
                        tag: el.tagName,
                        text: el.innerText ? el.innerText.trim().slice(0, 60) : '',
                        aria: el.getAttribute('aria-label') || '',
                        placeholder: el.getAttribute('placeholder') || ''
                    }))
                    .filter(i => i.text || i.aria || i.placeholder);
                return items;
            }
        """)

        print(f"🔍 Found {len(elements)} interactive elements:")
        for el in elements[:20]:
            print(f"   • {el['tag']}: text='{el['text']}' aria='{el['aria']}' placeholder='{el['placeholder']}'")

        # Ingest prompt into the video generator
        prompt = "Gere um vídeo cinematográfico em alta resolução 1080p da Pirâmide de vidro do Louvre à noite com reflexos dourados e chuva suave"
        editor = page.locator("rich-textarea div[contenteditable='true'], textarea, input[type='text'], [role='textbox']").first
        if await editor.count() > 0:
            print(f"✍️ Ingesting prompt into Videos tool: '{prompt}'")
            await editor.click()
            await page.keyboard.type(prompt, delay=10)
            await asyncio.sleep(1)

            send_btn = page.locator("button[aria-label*='Enviar' i], button[aria-label*='Send' i], button[aria-label*='Criar' i], button:has-text('Gerar'), button:has-text('Create'), .send-button").first
            if await send_btn.count() > 0:
                print("🚀 Submitting video generation...")
                await send_btn.click()
                await asyncio.sleep(5)
                await page.screenshot(path=str(shot_path.parent / "gemini_videos_generating_state.png"))

        await context.close()

if __name__ == "__main__":
    asyncio.run(main())
