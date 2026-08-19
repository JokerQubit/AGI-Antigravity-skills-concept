r"""
Chrome Profile Video Generator (Gemini Pro & Veo Engine)
Navigates to Gemini Pro Web UI using the user's authenticated persistent profile,
clicks the Videos tab or submits the video generation prompt, intercepts network video streams, and downloads the raw .mp4.
"""

import os
import sys
import time
import asyncio
from pathlib import Path

# Ensure UTF-8 output on Windows consoles
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

async def generate_gemini_pro_video(prompt: str, output_path: str, headless: bool = True):
    from playwright.async_api import async_playwright

    out_file = Path(output_path)
    out_file.parent.mkdir(parents=True, exist_ok=True)

    user_home = Path(os.environ.get("USERPROFILE", r"C:\Users\pichau"))
    automation_profile = user_home / ".gemini" / "chrome_automation_profile"

    print(f"🚀 [Gemini Pro Engine] Launching authenticated Chrome session...")
    print(f"📁 Target Output: {out_file}")

    async with async_playwright() as p:
        context = await p.chromium.launch_persistent_context(
            user_data_dir=str(automation_profile),
            channel="chrome",
            headless=headless,
            viewport={"width": 1920, "height": 1080},
            args=["--disable-blink-features=AutomationControlled"]
        )

        page = context.pages[0] if context.pages else await context.new_page()
        intercepted_video_urls = []
        downloaded_bytes = None

        # Intercept MP4 video responses
        async def handle_response(response):
            nonlocal downloaded_bytes
            content_type = response.headers.get("content-type", "")
            if "video/mp4" in content_type or response.url.endswith(".mp4") or "googlevideo.com" in response.url or "video" in content_type:
                print(f"📡 [Gemini Pro Engine] Intercepted video stream: {response.url[:80]}...")
                intercepted_video_urls.append(response.url)
                try:
                    downloaded_bytes = await response.body()
                except Exception as ex_b:
                    print(f"[Gemini Pro Engine] Body read notice: {ex_b}")

        page.on("response", handle_response)

        print("🌐 [Gemini Pro Engine] Navigating to https://gemini.google.com/app...")
        await page.goto("https://gemini.google.com/app", wait_until="domcontentloaded")
        await asyncio.sleep(3)

        # Check if 'Videos' tab in left navigation exists
        videos_nav = page.locator("a:has-text('Videos'), span:has-text('Videos'), div:has-text('Videos')").first
        if await videos_nav.count() > 0 and await videos_nav.is_visible():
            print("🎬 [Gemini Pro Engine] Clicking 'Videos' studio tab in sidebar...")
            try:
                await videos_nav.click()
                await asyncio.sleep(2)
            except Exception as ex_nav:
                print(f"[Gemini Pro Engine] Videos nav notice: {ex_nav}")

        # Ingest Prompt into input box
        print(f"✍️ [Gemini Pro Engine] Ingesting 6-pillar prompt: '{prompt[:60]}...'")
        editor = page.locator("rich-textarea div[contenteditable='true'], div[contenteditable='true']").first
        if await editor.count() > 0:
            await editor.click()
            await page.keyboard.type(prompt, delay=10)
            await asyncio.sleep(1)

            # Send prompt
            send_btn = page.locator("button[aria-label*='Send' i], button.send-button, mat-icon:has-text('send')").first
            if await send_btn.count() > 0:
                print("🚀 [Gemini Pro Engine] Clicking Send button...")
                await send_btn.click()
            else:
                await page.keyboard.press("Enter")

        print("⏳ [Gemini Pro Engine] Waiting for Veo neural video generation...")
        start_time = asyncio.get_event_loop().time()

        while (asyncio.get_event_loop().time() - start_time) < 180:
            if downloaded_bytes and len(downloaded_bytes) > 500000:
                print(f"🎉 [Gemini Pro Engine] Video stream captured ({len(downloaded_bytes) / 1024 / 1024:.2f} MB)!")
                with open(out_file, "wb") as f:
                    f.write(downloaded_bytes)
                print(f"✅ Video saved directly to disk: {out_file}")
                await context.close()
                return str(out_file)

            # Check for <video> element with blob
            video_el = page.locator("video").first
            if await video_el.count() > 0:
                src = await video_el.get_attribute("src")
                if src and src.startswith("blob:"):
                    print("🎯 Found video element with blob in DOM. Extracting...")
                    try:
                        video_b64 = await page.evaluate("""
                            async (blobUrl) => {
                                const resp = await fetch(blobUrl);
                                const blob = await resp.blob();
                                return new Promise((resolve) => {
                                    const reader = new FileReader();
                                    reader.onloadend = () => resolve(reader.result.split(',')[1]);
                                    reader.readAsDataURL(blob);
                                });
                            }
                        """, src)
                        import base64
                        downloaded_bytes = base64.b64decode(video_b64)
                        if len(downloaded_bytes) > 500000:
                            print(f"🎉 Extracted blob binary ({len(downloaded_bytes) / 1024 / 1024:.2f} MB)!")
                            break
                    except Exception as ex_b64:
                        print(f"[Gemini Pro Engine] Blob extraction notice: {ex_b64}")

            # Check for download buttons
            download_btn = page.locator("a[download], button[aria-label*='Download' i], button[aria-label*='Baixar' i]").first
            if await download_btn.count() > 0 and await download_btn.is_visible():
                print("💾 [Gemini Pro Engine] Found download button in DOM...")
                try:
                    async with page.expect_download(timeout=15000) as download_info:
                        await download_btn.click()
                    download = await download_info.value
                    await download.save_as(str(out_file))
                    print(f"🎉 [Gemini Pro Engine] Video saved via browser download: {out_file}")
                    await context.close()
                    return str(out_file)
                except Exception as ex_dl:
                    print(f"[Gemini Pro Engine] Download notice: {ex_dl}")

            await asyncio.sleep(1.5)

        # Take debug screenshot of final generation state
        debug_shot = out_file.parent / "gemini_pro_generation_state.png"
        await page.screenshot(path=str(debug_shot))
        print(f"📸 [Gemini Pro Engine] Final state screenshot: {debug_shot}")

        await context.close()

        if downloaded_bytes:
            with open(out_file, "wb") as f:
                f.write(downloaded_bytes)
            print(f"🎉 [Gemini Pro Engine] Raw video binary saved: {out_file} ({len(downloaded_bytes) / 1024 / 1024:.2f} MB)")
            return str(out_file)
        else:
            print("ℹ️ Prompt submitted to Gemini Pro. Generation state logged in screenshot.")
            return None

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Gemini Pro Veo Video Scraper")
    parser.add_argument("--prompt", type=str, required=True, help="Video prompt")
    parser.add_argument("--output", type=str, default="gemini_veo_video.mp4", help="Output MP4 path")
    parser.add_argument("--headed", action="store_true", help="Run with visible browser")

    args = parser.parse_args()
    asyncio.run(generate_gemini_pro_video(args.prompt, args.output, headless=not args.headed))
