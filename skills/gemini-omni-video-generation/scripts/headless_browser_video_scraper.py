"""
Autonomous Headless Browser Video Scraper & Interceptor
Drives a silent, background browser session (Playwright / Puppeteer) to interact with web-based video generation platforms (Google AI Studio, Gemini Web, VideoFX, HuggingFace Video Spaces) and extract .mp4 files directly to disk without interfering with the user.
"""

import os
import sys
import time
import json
import asyncio
from pathlib import Path

# Ensure UTF-8 output on Windows consoles
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

async def scrape_video_from_web_platform(prompt: str, output_path: str, platform: str = "google_ai_studio", user_data_dir: str = None):
    """
    Launches a fully background/headless browser session, injects the prompt into the target web generator,
    monitors network requests for video/mp4 streams or DOM video elements, and saves the resulting MP4.
    """
    from playwright.async_api import async_playwright

    out_file = Path(output_path)
    out_file.parent.mkdir(parents=True, exist_ok=True)

    print(f"🕵️ [Headless Video Scraper] Launching silent background browser session for: '{prompt[:45]}...'")

    async with async_playwright() as p:
        # Launch Chromium in pure headless mode with anti-detection flags
        browser = await p.chromium.launch(
            headless=True,
            args=[
                "--disable-blink-features=AutomationControlled",
                "--no-sandbox",
                "--disable-setuid-sandbox",
                "--disable-dev-shm-usage",
                "--disable-gpu",
                "--window-size=1920,1080"
            ]
        )

        # Context with custom user-agent and persistent session if available
        context = await browser.new_context(
            viewport={"width": 1920, "height": 1080},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
        )

        page = await context.new_page()
        downloaded_video_bytes = None

        # Network interceptor for .mp4 responses
        async def handle_response(response):
            nonlocal downloaded_video_bytes
            content_type = response.headers.get("content-type", "")
            if "video/mp4" in content_type or response.url.endswith(".mp4"):
                print(f"📡 [Headless Scraper] Intercepted video stream from: {response.url[:60]}...")
                try:
                    downloaded_video_bytes = await response.body()
                except Exception as e:
                    pass

        page.on("response", handle_response)

        # Target Platform Handling
        if platform == "google_ai_studio":
            target_url = "https://aistudio.google.com/app/prompts/new_video"
        elif platform == "videofx":
            target_url = "https://labs.google/fx/tools/video-fx"
        elif platform == "huggingface_veo":
            target_url = "https://huggingface.co/spaces"
        else:
            target_url = "https://gemini.google.com"

        print(f"🌐 [Headless Scraper] Navigating in background to: {target_url}")
        try:
            await page.goto(target_url, wait_until="domcontentloaded", timeout=20000)
            await asyncio.sleep(2)

            # Check if login or interactive prompt is needed
            title = await page.title()
            print(f"📑 [Headless Scraper] Page Title: '{title}'")

            # Look for prompt textarea/input box
            selectors_to_try = [
                "textarea[placeholder*='prompt' i]",
                "textarea[placeholder*='video' i]",
                "textarea[placeholder*='Describe' i]",
                "div[contenteditable='true']",
                "textarea"
            ]

            input_found = False
            for sel in selectors_to_try:
                elem = page.locator(sel).first
                if await elem.count() > 0 and await elem.is_visible():
                    print(f"✍️ [Headless Scraper] Found input field ({sel}). Ingesting prompt...")
                    await elem.fill(prompt)
                    input_found = True
                    break

            if input_found:
                # Find and click Generate/Submit button
                btn_selectors = [
                    "button:has-text('Generate')",
                    "button:has-text('Run')",
                    "button:has-text('Create')",
                    "button:has-text('Submit')",
                    "button[aria-label*='Send' i]"
                ]

                for b_sel in btn_selectors:
                    btn = page.locator(b_sel).first
                    if await btn.count() > 0 and await btn.is_visible():
                        print(f"🚀 [Headless Scraper] Clicking submit button ({b_sel})...")
                        await btn.click()
                        break

                # Wait for video generation (up to 45s polling in background)
                print("⏳ [Headless Scraper] Polling background DOM & network streams for completed video...")
                for _ in range(30):
                    if downloaded_video_bytes:
                        break
                    
                    # Check for video element in DOM
                    video_elem = page.locator("video").first
                    if await video_elem.count() > 0:
                        src = await video_elem.get_attribute("src")
                        if src and src.startswith("http"):
                            print(f"🎯 [Headless Scraper] Found video source URL in DOM: {src}")
                            # Fetch video src directly
                            resp = await page.request.get(src)
                            downloaded_video_bytes = await resp.body()
                            break

                    await asyncio.sleep(1.5)

        except Exception as e:
            print(f"⚠️ [Headless Scraper] Background web navigation note: {e}")

        await browser.close()

        if downloaded_video_bytes:
            with open(out_file, "wb") as f:
                f.write(downloaded_video_bytes)
            print(f"✨ [Headless Scraper] Video saved successfully to: {out_file} ({len(downloaded_video_bytes) / 1024 / 1024:.2f} MB)")
            return str(out_file)
        else:
            print("ℹ️ [Headless Scraper] Web platform required authentication or did not return direct stream. Falling back to local high-precision cinematic synthesizer.")
            return None


def run_scraper_sync(prompt: str, output_path: str, platform: str = "google_ai_studio"):
    return asyncio.run(scrape_video_from_web_platform(prompt, output_path, platform))


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Headless Browser Video Scraper")
    parser.add_argument("--prompt", type=str, required=True, help="Video prompt")
    parser.add_argument("--output", type=str, default="scraped_video.mp4", help="Output MP4 path")
    parser.add_argument("--platform", type=str, default="google_ai_studio", help="Target platform")

    args = parser.parse_args()
    run_scraper_sync(args.prompt, args.output, args.platform)
