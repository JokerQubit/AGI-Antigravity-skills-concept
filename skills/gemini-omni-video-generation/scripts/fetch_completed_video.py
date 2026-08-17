r"""
Fetch Completed Video from Gemini Pro Web Session
Navigates to the active chat session in Gemini Pro, waits for the video generation placeholder to complete,
and extracts the high-resolution .mp4 video file to disk.
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

async def fetch_video(output_path: str):
    from playwright.async_api import async_playwright

    out_file = Path(output_path)
    out_file.parent.mkdir(parents=True, exist_ok=True)

    user_home = Path(os.environ.get("USERPROFILE", r"C:\Users\pichau"))
    automation_profile = user_home / ".gemini" / "chrome_automation_profile"

    print(f"🚀 [Video Fetcher] Connecting to active Gemini Pro session...")

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
                print(f"📡 [Video Fetcher] Intercepted video stream: {response.url[:80]}...")
                try:
                    intercepted_bytes = await response.body()
                except:
                    pass

        page.on("response", handle_response)

        await page.goto("https://gemini.google.com/app", wait_until="domcontentloaded")
        await asyncio.sleep(5)

        print("⏳ [Video Fetcher] Monitoring chat for completed video element (up to 120s)...")
        for i in range(40):
            if intercepted_bytes:
                break

            # Look for video element in DOM
            video_el = page.locator("video").first
            if await video_el.count() > 0:
                src = await video_el.get_attribute("src")
                if src:
                    print(f"🎯 [Video Fetcher] Found generated video src: {src[:70]}...")
                    if src.startswith("blob:") or src.startswith("http"):
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
                            break
                        except Exception as e:
                            print(f"Note on evaluating blob: {e}")

            # Check for download button on video player
            download_btn = page.locator("button[aria-label*='Download' i], button[aria-label*='Baixar' i], a[download]").first
            if await download_btn.count() > 0 and await download_btn.is_visible():
                print("💾 [Video Fetcher] Clicking download button on video...")
                try:
                    async with page.expect_download(timeout=15000) as download_info:
                        await download_btn.click()
                    download = await download_info.value
                    await download.save_as(str(out_file))
                    print(f"🎉 [Video Fetcher] Video saved via browser download: {out_file}")
                    await context.close()
                    return str(out_file)
                except Exception as ex:
                    print(f"Download exception: {ex}")

            await asyncio.sleep(3)

        # Final screenshot
        await page.screenshot(path=str(out_file.parent / "gemini_completed_state.png"))

        await context.close()

        if intercepted_bytes:
            with open(out_file, "wb") as f:
                f.write(intercepted_bytes)
            print(f"🎉 [Video Fetcher] Raw video binary saved: {out_file} ({len(intercepted_bytes) / 1024 / 1024:.2f} MB)")
            return str(out_file)
        else:
            print("ℹ️ Video is still in rendering pipeline. Screenshot saved.")
            return None

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "gemini_pro_video.mp4"
    asyncio.run(fetch_video(out))
