r"""
Inspect Gemini File Upload DOM Elements & Attachment Mechanisms
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

async def inspect_upload():
    from playwright.async_api import async_playwright

    user_home = Path(os.environ.get("USERPROFILE", r"C:\Users\pichau"))
    automation_profile = user_home / ".gemini" / "chrome_automation_profile"

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
        await asyncio.sleep(4)

        # Inspect all buttons and inputs near the prompt box
        elements = await page.evaluate(r"""
            () => {
                const results = [];
                const buttons = document.querySelectorAll('button, input, mat-icon, gem-icon-button, [role="button"]');
                for (const b of buttons) {
                    const rect = b.getBoundingClientRect();
                    if (rect.top > 400 || b.tagName === 'INPUT') { // focus on lower half
                        results.push({
                            tag: b.tagName,
                            id: b.id,
                            className: b.className,
                            ariaLabel: b.getAttribute('aria-label') || '',
                            type: b.getAttribute('type') || '',
                            text: (b.innerText || '').slice(0, 30),
                            rect: { x: rect.x, y: rect.y, w: rect.width, h: rect.height }
                        });
                    }
                }
                return results;
            }
        """)

        print(f"🔍 Found {len(elements)} elements in lower viewport:")
        for el in elements:
            print(f"  • {el['tag']} (type={el['type']}) aria='{el['ariaLabel']}' text='{el['text']}' class='{el['className'][:30]}'")

        # Try clicking the plus button and checking for file input appearing
        print("\n👉 Testing Click on '+' button...")
        plus_btn = page.locator("button:has(mat-icon:has-text('add')), button[aria-label*='Add' i], button.leading-action, [mattooltip*='Add' i]").first
        if await plus_btn.count() > 0:
            print(f"Found plus button: {await plus_btn.evaluate('el => el.outerHTML')}")
            await plus_btn.click()
            await asyncio.sleep(2)
            
            # Re-check for menu items or file inputs
            menu_items = await page.evaluate(r"""
                () => {
                    const items = document.querySelectorAll('.mat-mdc-menu-item, [role="menuitem"], input[type="file"]');
                    return Array.from(items).map(i => ({
                        tag: i.tagName,
                        aria: i.getAttribute('aria-label') || '',
                        text: i.innerText || '',
                        type: i.getAttribute('type') || ''
                    }));
                }
            """)
            print(f"📋 Menu items after click: {menu_items}")

        await context.close()

if __name__ == "__main__":
    asyncio.run(inspect_upload())
