r"""
Official Google Veo 3.1 Dedicated Studio Generator & Stream Interceptor
Navigates specifically to the Google Veo Studio (https://gemini.google.com/videos or Sidebar -> Videos),
configures cinematic aspect ratio / resolution, attaches reference images with smart path resolution and popup menu FileChooser,
preserves the permanent chat link, and intercepts the genuine Google Veo .mp4 video stream directly to disk.
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

def resolve_image_path(raw_path: str) -> Path:
    """Smart image locator searching across CWD, absolute paths, and active projects."""
    if not raw_path:
        return None
    
    p = Path(raw_path)
    if p.is_file():
        return p.resolve()
    
    # Check CWD
    cwd_p = (Path.cwd() / raw_path).resolve()
    if cwd_p.is_file():
        return cwd_p
    
    # Check common user document projects
    user_home = Path(os.environ.get("USERPROFILE", r"C:\Users\pichau"))
    candidate_dirs = [
        user_home / "Documents" / "antigravity" / "proud-babbage",
        user_home / ".gemini" / "config" / "plugins" / "AGI-Antigravity-skills-concept",
        Path.cwd()
    ]
    
    for cdir in candidate_dirs:
        cand = (cdir / raw_path).resolve()
        if cand.is_file():
            return cand
        # Search by filename
        matches = list(cdir.rglob(p.name))
        if matches and matches[0].is_file():
            return matches[0].resolve()
            
    return None

async def generate_veo_studio_video(prompt: str, output_path: str, reference_image: str = None, headed: bool = False):
    from playwright.async_api import async_playwright

    out_file = Path(output_path).resolve()
    out_file.parent.mkdir(parents=True, exist_ok=True)

    user_home = Path(os.environ.get("USERPROFILE", r"C:\Users\pichau"))
    automation_profile = user_home / ".gemini" / "chrome_automation_profile"

    print("=" * 80)
    print("🎬 GOOGLE VEO 3.1 DEDICATED STUDIO GENERATOR")
    print(f"✍️ Cinematic Prompt: '{prompt}'")
    
    resolved_img = resolve_image_path(reference_image) if reference_image else None
    if reference_image:
        if resolved_img:
            print(f"📎 [Reference Image Found]: {resolved_img} ({os.path.getsize(resolved_img) / 1024:.1f} KB)")
        else:
            print(f"⚠️ [WARNING] Reference image not found at: '{reference_image}'")
            print(f"   Searched in CWD ({Path.cwd()}) and project folders.")
            
    print(f"📁 Target Output: {out_file}")
    print("=" * 80)

    async with async_playwright() as p:
        context = await p.chromium.launch_persistent_context(
            user_data_dir=str(automation_profile),
            channel="chrome",
            headless=not headed,
            viewport={"width": 1920, "height": 1080},
            args=["--disable-blink-features=AutomationControlled"]
        )

        page = context.pages[0] if context.pages else await context.new_page()
        intercepted_bytes = None
        permanent_chat_url = None

        # Network stream interceptor
        async def handle_response(response):
            nonlocal intercepted_bytes
            content_type = response.headers.get("content-type", "")
            url = response.url
            if ("video/mp4" in content_type or url.endswith(".mp4") or "googlevideo.com" in url or "contribution.usercontent.google.com" in url) and "download" in url:
                print(f"📡 [Google Veo Stream] Intercepted stream payload: {url[:75]}...")
                try:
                    data = await response.body()
                    if len(data) > 500000:
                        intercepted_bytes = data
                except Exception as ex:
                    print(f"[Stream Note] Response body intercept note: {ex}")

        page.on("response", handle_response)

        # 1. Direct navigation to Google Veo Studio
        print("🌐 [Step 1] Navigating to Google Veo Studio (https://gemini.google.com/videos)...")
        await page.goto("https://gemini.google.com/videos", wait_until="domcontentloaded")
        await asyncio.sleep(4)

        # 2. Check if we need to click the Videos tab in sidebar
        if "videos" not in page.url.lower():
            print("🔍 Locating 'Videos' tab in navigation menu...")
            videos_nav = page.locator("a[aria-label*='Videos' i], a:has-text('Videos'), button:has-text('Videos')").first
            if await videos_nav.count() > 0 and await videos_nav.is_visible():
                print("👉 Clicking 'Videos' studio tab...")
                await videos_nav.click()
                await asyncio.sleep(3)

        # Close any backdrop or overlay
        await page.keyboard.press("Escape")
        await asyncio.sleep(1)

        # 3. Attach reference image if provided (Image-to-Video Conditioning)
        if resolved_img:
            img_path_str = str(resolved_img)
            print(f"📎 [Step 2] Attaching reference image to Veo: {img_path_str}...")
            upload_success = False

            # Method A: Click 'Upload & tools' button -> Click 'Upload files' with expect_file_chooser
            upload_tools_btn = page.locator("button[aria-label*='Upload & tools' i], button[aria-label*='Upload and tools' i], button:has(mat-icon:has-text('add'))").first
            if await upload_tools_btn.count() > 0 and await upload_tools_btn.is_visible():
                try:
                    print("👉 Clicking 'Upload & tools' button in prompt area...")
                    await upload_tools_btn.click()
                    await asyncio.sleep(1)

                    upload_item = page.locator("[role='menuitem']:has-text('Upload'), [role='menuitem']:has-text('files'), [role='menuitem']:has-text('image'), .mat-mdc-menu-item").first
                    if await upload_item.count() > 0 and await upload_item.is_visible():
                        print(f"👉 Clicking menu item '{await upload_item.inner_text()}' via FileChooser...")
                        async with page.expect_file_chooser(timeout=8000) as fc_info:
                            await upload_item.click()
                        fc = await fc_info.value
                        await fc.set_files(img_path_str)
                        print(f"✅ [FileChooser] Attached {resolved_img.name} successfully!")
                        upload_success = True
                        await asyncio.sleep(3)
                except Exception as ex:
                    print(f"FileChooser fallback note: {ex}")

            # Method B: Direct input[type='file'] fallback
            if not upload_success:
                file_inputs = page.locator("input[type='file']")
                if await file_inputs.count() > 0:
                    for i in range(await file_inputs.count()):
                        try:
                            await file_inputs.nth(i).set_input_files(img_path_str)
                            print(f"✅ [Direct Input] Set files on input[type='file'] #{i}!")
                            upload_success = True
                            await asyncio.sleep(3)
                        except Exception as ex_in:
                            print(f"[FileInput Notice] Failed on input #{i}: {ex_in}")
                            continue

            if upload_success:
                print("⏳ Waiting for image upload thumbnail to register...")
                await asyncio.sleep(2)
            else:
                print("⚠️ [Warning] Could not attach file through standard inputs.")

        # 4. Locate the Veo Video Input Box
        print("✍️ [Step 3] Locating Veo prompt input box...")
        veo_input = page.locator("div[data-placeholder*='video' i], rich-textarea div[contenteditable='true'], div[contenteditable='true']").first
        
        if await veo_input.count() > 0:
            await veo_input.click()
            await asyncio.sleep(1)
            await veo_input.fill(veo_prompt)
        else:
            await page.keyboard.type(veo_prompt, delay=10)

        await asyncio.sleep(1)

        # 5. Click Send / Generate
        print("🚀 [Step 4] Triggering Google Veo generation...")
        send_btn = page.locator("button[aria-label*='Send' i], button[aria-label*='Enviar' i], button.send-button, mat-icon:has-text('send')").first
        if await send_btn.count() > 0 and await send_btn.is_visible():
            await send_btn.click()
        else:
            await page.keyboard.press("Enter")

        print("⏳ Generation started. Intercepting Veo MP4 stream and polling for render completion...")

        # 6. Polling & Stream Interception Loop
        max_wait_seconds = 240
        start_time = asyncio.get_event_loop().time()
        cycle = 0

        while (asyncio.get_event_loop().time() - start_time) < max_wait_seconds:
            await asyncio.sleep(3)
            cycle += 1
            elapsed = int(asyncio.get_event_loop().time() - start_time)

            # Check if network listener caught the MP4 bytes
            if intercepted_bytes and len(intercepted_bytes) > 500000:
                print(f"🎉 [Step 5] Intercepted full Veo video stream ({len(intercepted_bytes) / 1024 / 1024:.2f} MB)!")
                out_file.write_bytes(intercepted_bytes)
                print(f"✅ Master Veo MP4 written directly to disk: {out_file}")
                await context.close()
                return str(out_file)

            # Check for <video> elements with blob: or http: source
            video_el = page.locator("video").first
            if await video_el.count() > 0:
                src = await video_el.get_attribute("src")
                if src:
                    if src.startswith("http") and ("google" in src or "mp4" in src):
                        print(f"🎬 Found direct video URL: {src[:80]}...")
                    elif src.startswith("blob:"):
                        # Extract blob via in-browser fetch and Base64 conversion
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
                            intercepted_bytes = base64.b64decode(video_b64)
                            if len(intercepted_bytes) > 500000:
                                print(f"🎉 [Step 5] Veo blob binary extracted: {len(intercepted_bytes) / 1024 / 1024:.2f} MB!")
                                break
                        except Exception as ex_b64:
                            print(f"[Blob Extraction Notice] {ex_b64}")

                # Check for Download button
                dl_btn = page.locator("button[aria-label*='Download' i], button[aria-label*='Baixar' i], a[download]").first
                if await dl_btn.count() > 0 and await dl_btn.is_visible():
                    print("💾 Found Veo Download button. Downloading .mp4...")
                    try:
                        async with page.expect_download(timeout=10000) as download_info:
                            await dl_btn.click()
                        download = await download_info.value
                        await download.save_as(str(out_file))
                        print(f"🎉 [Step 5] Veo master video saved: {out_file}")
                        await context.close()
                        return str(out_file)
                    except Exception as ex_dl:
                        print(f"[Download Button Notice] {ex_dl}")

                if cycle % 5 == 0:
                    print(f"⏳ Generating with Veo... ({elapsed}s elapsed)")

        # Capture final studio state screenshot
        studio_shot = out_file.parent / "veo_studio_final_state.png"
        await page.screenshot(path=str(studio_shot))
        print(f"📸 Veo studio state screenshot saved: {studio_shot}")

        # Update permanent chat link before closing
        permanent_chat_url = page.url
        print(f"🔗 Permanent Chat Link: {permanent_chat_url}")

        await context.close()

        if intercepted_bytes and len(intercepted_bytes) > 100000:
            with open(out_file, "wb") as f:
                f.write(intercepted_bytes)
            print(f"🎉 [SUCCESS] Authentic Google Veo .mp4 saved: {out_file} ({len(intercepted_bytes) / 1024 / 1024:.2f} MB)")
            print(f"🌐 You can also view this chat anytime at: {permanent_chat_url}")
            return str(out_file)
        else:
            print("ℹ️ Request submitted. You can check the video at:")
            print(f"👉 {permanent_chat_url}")
            print(f"👉 https://gemini.google.com/library")
            return None

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Google Veo 3.1 Dedicated Studio Generator")
    parser.add_argument("--prompt", type=str, required=True, help="Cinematic video prompt")
    parser.add_argument("--output", type=str, default="veo_studio_video.mp4", help="Output MP4 file path")
    parser.add_argument("--image", type=str, default=None, help="Optional reference image path")
    parser.add_argument("--headed", action="store_true", help="Run with visible browser window")

    args = parser.parse_args()
    asyncio.run(generate_veo_studio_video(args.prompt, args.output, args.image, headed=args.headed))
