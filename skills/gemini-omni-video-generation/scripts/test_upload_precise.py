r"""
Test Precise Upload via 'Upload & tools' Menu in Gemini Pro
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

async def test_precise_upload(image_path: str):
    from playwright.async_api import async_playwright

    user_home = Path(os.environ.get("USERPROFILE", r"C:\Users\pichau"))
    automation_profile = user_home / ".gemini" / "chrome_automation_profile"

    img_file = Path(image_path).resolve()
    print(f"📎 Testing attachment of: {img_file}")

    async with async_playwright() as p:
        context = await p.chromium.launch_persistent_context(
            user_data_dir=str(automation_profile),
            channel="chrome",
            headless=True,
            viewport={"width": 1920, "height": 1080},
            args=["--disable-blink-features=AutomationControlled"]
        )

        page = context.pages[0] if context.pages else await context.new_page()
        await page.goto("https://gemini.google.com/app", wait_until="domcontentloaded")
        await asyncio.sleep(4)

        # Close any open dialogs
        await page.keyboard.press("Escape")
        await asyncio.sleep(1)

        # 1. Click 'Upload & tools' button
        upload_tools_btn = page.locator("button[aria-label*='Upload & tools' i], button[aria-label*='Upload and tools' i]").first
        if await upload_tools_btn.count() > 0:
            print("👉 Clicking 'Upload & tools' button...")
            await upload_tools_btn.click()
            await asyncio.sleep(1)

            # Inspect popup menu items
            menu_items = await page.evaluate(r"""
                () => {
                    const items = document.querySelectorAll('.mat-mdc-menu-item, [role="menuitem"]');
                    return Array.from(items).map(i => ({
                        text: (i.innerText || '').trim(),
                        aria: i.getAttribute('aria-label') || '',
                        class: i.className
                    }));
                }
            """)
            print(f"📋 Menu items found: {menu_items}")

            # 2. Click the 'Upload files' option with file chooser
            upload_item = page.locator("[role='menuitem']:has-text('Upload'), [role='menuitem']:has-text('files'), [role='menuitem']:has-text('image'), .mat-mdc-menu-item").first
            if await upload_item.count() > 0:
                print(f"👉 Clicking menu item '{await upload_item.inner_text()}' via FileChooser...")
                async with page.expect_file_chooser(timeout=8000) as fc_info:
                    await upload_item.click()
                fc = await fc_info.value
                await fc.set_files(str(img_file))
                print(f"🎉 Successfully attached {img_file.name} to Gemini prompt box!")
                await asyncio.sleep(4)

        # Screenshot to verify image thumbnail in input area
        shot_path = Path("C:/Users/pichau/Documents/antigravity/proud-babbage/assets/videos/upload_test_verification.png")
        await page.screenshot(path=str(shot_path))
        print(f"📸 Verification screenshot saved: {shot_path}")

        await context.close()

if __name__ == "__main__":
    img = r"C:\Users\pichau\Documents\antigravity\proud-babbage\assets\images\hero.jpg"
    asyncio.run(test_precise_upload(img))
