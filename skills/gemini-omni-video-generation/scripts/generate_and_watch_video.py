r"""
Continuous Video Generator and Live Watcher for Gemini Pro / Veo
Submits the video generation prompt in a single persistent page session, keeps the page active,
monitors real-time rendering, and downloads the raw .mp4 directly.
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

async def generate_and_watch(prompt: str, output_path: str):
    from playwright.async_api import async_playwright

    out_file = Path(output_path)
    out_file.parent.mkdir(parents=True, exist_ok=True)

    user_home = Path(os.environ.get("USERPROFILE", r"C:\Users\pichau"))
    automation_profile = user_home / ".gemini" / "chrome_automation_profile"

    print("🚀 [Live Watcher] Launching persistent Gemini Pro session...")

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
                print(f"📡 [Live Watcher] Captured video stream: {response.url[:70]}...")
                try:
                    intercepted_bytes = await response.body()
                except Exception as ex_b:
                    print(f"[Live Watcher Notice] Body read: {ex_b}")

        page.on("response", handle_response)

        await page.goto("https://gemini.google.com/app", wait_until="domcontentloaded")
        await asyncio.sleep(4)

        # Ingest prompt
        editor = page.locator("rich-textarea div[contenteditable='true'], div[contenteditable='true']").first
        if await editor.count() > 0:
            print(f"✍️ Ingesting prompt: '{prompt}'")
            await editor.click()
            await page.keyboard.type(prompt, delay=8)
            await asyncio.sleep(1)

            send_btn = page.locator("button[aria-label*='Enviar' i], button[aria-label*='Send' i], .send-button, gem-icon-button.send-button").first
            if await send_btn.count() > 0 and await send_btn.is_visible():
                print("🚀 Submitting video generation prompt to Gemini Pro...")
                await send_btn.click()
            else:
                await page.keyboard.press("Enter")

        # Stay on the same page and poll for 150 seconds
        print("⏳ [Live Watcher] Monitoring live page stream for completed video...")
        for step in range(30):
            await asyncio.sleep(5)
            
            # Save periodic progress snapshot
            snap_path = out_file.parent / f"render_progress_step.png"
            await page.screenshot(path=str(snap_path))

            if intercepted_bytes:
                print("🎉 [Live Watcher] Intercepted completed video binary from network!")
                break

            video_count = await page.locator("video").count()
            if video_count > 0:
                video_el = page.locator("video").first
                src = await video_el.get_attribute("src")
                if src and (src.startswith("blob:") or src.startswith("http")):
                    print(f"🎯 [Live Watcher] Found video player with src: {src[:60]}...")
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
                        print(f"Note on blob: {e}")

            # Check download button
            dl_btn = page.locator("button[aria-label*='Download' i], button[aria-label*='Baixar' i], a[download]").first
            if await dl_btn.count() > 0 and await dl_btn.is_visible():
                print("💾 [Live Watcher] Found download button! Triggering browser download...")
                try:
                    async with page.expect_download(timeout=10000) as download_info:
                        await dl_btn.click()
                    download = await download_info.value
                    await download.save_as(str(out_file))
                    print(f"🎉 [Live Watcher] Video downloaded successfully: {out_file}")
                    await context.close()
                    return True
                except Exception as ex:
                    print(f"Download note: {ex}")

        await context.close()

        if intercepted_bytes:
            with open(out_file, "wb") as f:
                f.write(intercepted_bytes)
            print(f"🎉 [Live Watcher] Master video file saved: {out_file} ({len(intercepted_bytes) / 1024 / 1024:.2f} MB)")
            return True
        else:
            print("ℹ️ Stream cycle finished. Progress state captured in screenshot.")
            return False

if __name__ == "__main__":
    p = sys.argv[1] if len(sys.argv) > 1 else "Gere um vídeo cinematográfico em alta resolução 1080p da Pirâmide do Louvre à noite com chuva e reflexos dourados"
    o = sys.argv[2] if len(sys.argv) > 2 else "C:\\Users\\pichau\\Documents\\antigravity\\proud-babbage\\assets\\videos\\veo_generated_direct.mp4"
    asyncio.run(generate_and_watch(p, o))
