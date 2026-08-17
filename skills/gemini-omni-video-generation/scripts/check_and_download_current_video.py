r"""
Check and Download Active Video from Gemini Pro Session
Inspects the active chat in Gemini Pro, checks if the video rendering has completed, takes a screenshot of the video player,
and downloads the .mp4 video binary directly to disk.
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

async def check_and_download():
    from playwright.async_api import async_playwright

    user_home = Path(os.environ.get("USERPROFILE", r"C:\Users\pichau"))
    automation_profile = user_home / ".gemini" / "chrome_automation_profile"
    output_dir = Path(r"C:\Users\pichau\Documents\antigravity\proud-babbage\assets\videos")
    output_dir.mkdir(parents=True, exist_ok=True)
    out_video = output_dir / "gemini_veo_downloaded_video.mp4"

    print("🚀 [Video Inspector] Connecting to active Gemini Pro session...")

    async with async_playwright() as p:
        context = await p.chromium.launch_persistent_context(
            user_data_dir=str(automation_profile),
            channel="chrome",
            headless=True,
            viewport={"width": 1920, "height": 1080},
            args=["--disable-blink-features=AutomationControlled"]
        )

        page = context.pages[0] if context.pages else await context.new_page()
        intercepted_bytes = None

        async def handle_response(response):
            nonlocal intercepted_bytes
            content_type = response.headers.get("content-type", "")
            if "video/mp4" in content_type or response.url.endswith(".mp4") or "googlevideo.com" in response.url:
                print(f"📡 [Video Inspector] Intercepted video stream URL: {response.url[:70]}...")
                try:
                    intercepted_bytes = await response.body()
                except:
                    pass

        page.on("response", handle_response)

        await page.goto("https://gemini.google.com/app", wait_until="domcontentloaded")
        await asyncio.sleep(5)

        # Check latest chat state
        screenshot_path = output_dir / "gemini_current_chat_state.png"
        await page.screenshot(path=str(screenshot_path))
        print(f"📸 Current chat screenshot captured: {screenshot_path}")

        # Check for video tag in DOM
        video_count = await page.locator("video").count()
        print(f"🔍 Found {video_count} video element(s) in DOM.")

        if video_count > 0:
            video_el = page.locator("video").first
            src = await video_el.get_attribute("src")
            print(f"🎯 Video source attribute: {src}")

            if src and (src.startswith("blob:") or src.startswith("http")):
                print("📥 Fetching raw video data from browser context...")
                try:
                    video_b64 = await page.evaluate(r"""
                        async (url) => {
                            const resp = await fetch(url);
                            const blob = await resp.blob();
                            return new Promise((resolve) => {
                                const reader = new FileReader();
                                reader.onloadend = () => resolve(reader.result.split(',')[1]);
                                reader.readAsDataURL(blob);
                            });
                        }
                    """, src)
                    import base64
                    intercepted_bytes = base64.b64decode(video_b64)
                    print(f"✅ Video data fetched successfully: {len(intercepted_bytes) / 1024 / 1024:.2f} MB")
                except Exception as e:
                    print(f"Note on fetching video blob: {e}")

        # Check for download buttons
        download_btns = page.locator("button[aria-label*='Download' i], button[aria-label*='Baixar' i], a[download]")
        if await download_btns.count() > 0:
            print(f"💾 Found {await download_btns.count()} download button(s). Clicking...")
            try:
                async with page.expect_download(timeout=10000) as download_info:
                    await download_btns.first.click()
                download = await download_info.value
                await download.save_as(str(out_video))
                print(f"🎉 Video saved via native download: {out_video}")
            except Exception as ex:
                print(f"Native download note: {ex}")

        # Inspect text of latest message
        latest_text = await page.evaluate(r"""
            () => {
                const messages = Array.from(document.querySelectorAll('.model-response-text, message-content, [data-test-id*="response"]'));
                if (messages.length > 0) {
                    return messages[messages.length - 1].innerText;
                }
                return document.body.innerText.slice(-600);
            }
        """)
        print(f"💬 Latest Gemini Response Text:\n{latest_text[:300]}")

        await context.close()

        if intercepted_bytes:
            with open(out_video, "wb") as f:
                f.write(intercepted_bytes)
            print(f"🎉 Master video saved to: {out_video} ({len(intercepted_bytes) / 1024 / 1024:.2f} MB)")
            return True
        else:
            return False

if __name__ == "__main__":
    asyncio.run(check_and_download())
