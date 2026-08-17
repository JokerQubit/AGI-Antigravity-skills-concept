r"""
Animate Nano Banana Images with Google Veo (Image-to-Video Automation)
Uploads a local reference image (from Nano Banana), sends dynamic animation instructions to Google Veo,
and downloads the generated .mp4 video into the web project assets.
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

async def animate_image_with_veo(image_path: str, prompt: str, output_path: str, headless: bool = True):
    from playwright.async_api import async_playwright

    img_file = Path(image_path).resolve()
    out_file = Path(output_path).resolve()
    out_file.parent.mkdir(parents=True, exist_ok=True)

    user_home = Path(os.environ.get("USERPROFILE", r"C:\Users\pichau"))
    automation_profile = user_home / ".gemini" / "chrome_automation_profile"

    print(f"🎬 [Image-to-Video Engine] Uploading Reference Image: {img_file.name}")
    print(f"✍️ Animation Prompt: '{prompt}'")
    print(f"📁 Output Target: {out_file}")

    async with async_playwright() as p:
        context = await p.chromium.launch_persistent_context(
            user_data_dir=str(automation_profile),
            channel="chrome",
            headless=headless,
            viewport={"width": 1920, "height": 1080},
            args=["--disable-blink-features=AutomationControlled"]
        )

        page = context.pages[0] if context.pages else await context.new_page()
        intercepted_bytes = None

        # Network interceptor for video download
        async def handle_response(response):
            nonlocal intercepted_bytes
            content_type = response.headers.get("content-type", "")
            if "video/mp4" in content_type or response.url.endswith(".mp4") or "googlevideo.com" in response.url:
                print(f"📡 [Image-to-Video] Intercepted video stream: {response.url[:70]}...")
                try:
                    intercepted_bytes = await response.body()
                except:
                    pass

        page.on("response", handle_response)

        print("🌐 [Image-to-Video] Navigating to https://gemini.google.com/app...")
        await page.goto("https://gemini.google.com/app", wait_until="domcontentloaded")
        await asyncio.sleep(4)

        # Close any backdrop or open menu
        await page.keyboard.press("Escape")
        await asyncio.sleep(1)

        # Upload reference image via file input
        file_inputs = page.locator("input[type='file']")
        if await file_inputs.count() > 0:
            print(f"📎 [Image-to-Video] Direct file input found. Attaching {img_file.name}...")
            await file_inputs.first.set_input_files(str(img_file))
            await asyncio.sleep(3)
        else:
            # Click the plus / add button next to prompt input
            plus_btn = page.locator("button:has(mat-icon:has-text('add')), button[aria-label*='Add' i], button[aria-label*='Adicionar' i], button.leading-action").first
            if await plus_btn.count() > 0 and await plus_btn.is_visible():
                print("📎 [Image-to-Video] Clicking '+' button to reveal file upload...")
                await plus_btn.click()
                await asyncio.sleep(1)
                file_input = page.locator("input[type='file']").first
                if await file_input.count() > 0:
                    await file_input.set_input_files(str(img_file))
                    await asyncio.sleep(3)

        # Enter the animation prompt
        editor = page.locator("rich-textarea div[contenteditable='true'], div[contenteditable='true']").first
        if await editor.count() > 0:
            print("✍️ [Image-to-Video] Ingesting prompt into editor...")
            await editor.click()
            await page.keyboard.type(f"Crie um vídeo animando esta imagem de referência: {prompt}", delay=10)
            await asyncio.sleep(1)

            # Click send
            send_btn = page.locator("button[aria-label*='Enviar' i], button[aria-label*='Send' i], .send-button, gem-icon-button.send-button").first
            if await send_btn.count() > 0 and await send_btn.is_visible():
                print("🚀 [Image-to-Video] Submitting request to Veo engine...")
                await send_btn.click()
            else:
                await page.keyboard.press("Enter")

            # Polling for completion
            print("⏳ [Image-to-Video] Polling for completed video generation (up to 120s)...")
            for _ in range(50):
                if intercepted_bytes:
                    break

                video_el = page.locator("video").first
                if await video_el.count() > 0:
                    src = await video_el.get_attribute("src")
                    if src and (src.startswith("blob:") or src.startswith("http")):
                        print(f"🎯 [Image-to-Video] Found video in DOM: {src[:60]}...")
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
                            pass

                download_btn = page.locator("button[aria-label*='Download' i], button[aria-label*='Baixar' i], a[download]").first
                if await download_btn.count() > 0 and await download_btn.is_visible():
                    print("💾 [Image-to-Video] Downloading video...")
                    try:
                        async with page.expect_download(timeout=15000) as download_info:
                            await download_btn.click()
                        download = await download_info.value
                        await download.save_as(str(out_file))
                        print(f"🎉 [Image-to-Video] Video successfully saved: {out_file}")
                        await context.close()
                        return str(out_file)
                    except:
                        pass

                await asyncio.sleep(2.5)

        # Screenshot state
        shot_path = out_file.parent / "image_to_video_state.png"
        await page.screenshot(path=str(shot_path))
        print(f"📸 State screenshot saved: {shot_path}")

        await context.close()

        if intercepted_bytes:
            with open(out_file, "wb") as f:
                f.write(intercepted_bytes)
            print(f"✨ [Image-to-Video] Master .mp4 saved: {out_file} ({len(intercepted_bytes) / 1024 / 1024:.2f} MB)")
            return str(out_file)
        else:
            print("ℹ️ Request submitted and processing in Gemini Pro.")
            return None

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Animate Nano Banana image with Veo")
    parser.add_argument("--image", type=str, required=True, help="Path to input reference image")
    parser.add_argument("--prompt", type=str, required=True, help="Animation instruction prompt")
    parser.add_argument("--output", type=str, default="veo_animated_image.mp4", help="Output MP4 path")
    parser.add_argument("--headed", action="store_true", help="Run with visible browser")

    args = parser.parse_args()
    asyncio.run(animate_image_with_veo(args.image, args.prompt, args.output, headless=not args.headed))
