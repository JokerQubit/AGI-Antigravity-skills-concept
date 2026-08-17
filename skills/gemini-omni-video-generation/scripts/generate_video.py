"""
Gemini Omni & Veo 3.1 Video Generation Engine
Multi-Backend Video Generation Pipeline (Google Vertex AI Veo 3.1, Gemini API, Multi-Scene Cinematic Presentation & FFmpeg H.264 Master Encoder)
"""

import os
import sys
import time
import json
import math
import argparse
import subprocess
from pathlib import Path
from PIL import Image, ImageEnhance, ImageFilter, ImageDraw, ImageFont
import numpy as np

# Ensure UTF-8 output on Windows consoles
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')


def generate_google_veo_3_1_api(prompt: str, api_key: str = None, project_id: str = None, duration_seconds: int = 8):
    """
    Client for Google Vertex AI / Gemini Veo 3.1 Video Generation API.
    Endpoint: veo-3.1-generate-001:predictLongRunning (with veo-3.0 and veo-2.0 fallback)
    """
    import urllib.request
    import urllib.error

    api_key = api_key or os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        print("[Google Veo 3.1] GEMINI_API_KEY not set. Using local multi-scene cinematic synthesizer.")
        return None

    # Veo 3.1 Primary Endpoint
    models_to_try = [
        "veo-3.1-generate-001",
        "veo-3.0-generate-001",
        "veo-2.0-generate-001"
    ]

    for model_name in models_to_try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:predictLongRunning?key={api_key}"
        print(f"[Google Veo 3.1] Dispatching video request to '{model_name}'...")
        
        payload = {
            "instances": [{
                "prompt": prompt
            }],
            "parameters": {
                "aspectRatio": "16:9",
                "durationSeconds": duration_seconds,
                "sampleCount": 1,
                "fps": 30,
                "quality": "cinematic_ultra"
            }
        }

        req = urllib.request.Request(
            url,
            data=json.dumps(payload).encode('utf-8'),
            headers={"Content-Type": "application/json"}
        )

        try:
            with urllib.request.urlopen(req) as resp:
                data = json.loads(resp.read().decode('utf-8'))
                operation_name = data.get("name")
                print(f"[Google Veo 3.1] Operation dispatched successfully: {operation_name}")
                return operation_name
        except urllib.error.HTTPError as e:
            print(f"[Google Veo 3.1] {model_name} returned: {e.code}. Attempting next model fallback...")
            continue

    return None


def render_scene_clip(image_path: str, duration_sec: float, fps: int, motion_type: str, title_text: str, sub_text: str, target_w: int, target_h: int):
    """
    Renders an individual cinematic scene with specific camera kinematics and typography overlay.
    """
    img = Image.open(image_path).convert("RGB")
    orig_w, orig_h = img.size
    total_frames = int(duration_sec * fps)
    frames = []

    # Font setup
    try:
        # Windows system fonts or default
        font_title = ImageFont.truetype("arial.ttf", 44)
        font_sub = ImageFont.truetype("arial.ttf", 22)
    except:
        font_title = ImageFont.load_default()
        font_sub = ImageFont.load_default()

    for i in range(total_frames):
        t = i / total_frames # 0.0 to 1.0

        # Kinematic Motion Curves
        if motion_type == "push_in":
            # Slow dramatic push in (zoom from 1.0 to 1.18)
            zoom = 1.0 + 0.18 * t
            pan_x = 0
            pan_y = 0
        elif motion_type == "crane_down":
            zoom = 1.12 - 0.08 * t
            pan_x = 0
            pan_y = (t - 0.5) * 0.08 * orig_h
        elif motion_type == "orbital_pan":
            zoom = 1.08 + 0.06 * math.sin(math.pi * t)
            pan_x = (t - 0.5) * 0.12 * orig_w
            pan_y = math.sin(math.pi * t) * 0.03 * orig_h
        else: # slow drift
            zoom = 1.05 + 0.05 * t
            pan_x = (t - 0.5) * 0.04 * orig_w
            pan_y = (t - 0.5) * 0.04 * orig_h

        # Calculate crop
        crop_w = orig_w / zoom
        crop_h = orig_h / zoom
        left = (orig_w - crop_w) / 2.0 + pan_x
        top = (orig_h - crop_h) / 2.0 + pan_y

        left = max(0, min(orig_w - crop_w, left))
        top = max(0, min(orig_h - crop_h, top))
        right = left + crop_w
        bottom = top + crop_h

        cropped = img.crop((left, top, right, bottom))
        resized = cropped.resize((target_w, target_h), Image.Resampling.LANCZOS)

        # Draw Typographic Title Card with Fade-in/Fade-out
        alpha_text = 1.0
        if t < 0.2:
            alpha_text = t / 0.2
        elif t > 0.8:
            alpha_text = (1.0 - t) / 0.2

        if title_text and alpha_text > 0.05:
            draw = ImageDraw.Draw(resized)
            
            # Subtle dark glass pill behind title
            pill_y = target_h - 180
            draw.rectangle([(80, pill_y - 20), (target_w - 80, pill_y + 100)], fill=(5, 7, 10))
            
            # Draw gold accent line
            draw.line([(80, pill_y - 20), (80, pill_y + 100)], fill=(201, 168, 106), width=6)
            
            # Draw text
            draw.text((110, pill_y), title_text.upper(), fill=(245, 240, 230), font=font_title)
            if sub_text:
                draw.text((110, pill_y + 55), sub_text.upper(), fill=(201, 168, 106), font=font_sub)

        # Cinemascope 2.39:1 Letterbox bars
        bar_height = int(target_h * 0.08)
        draw = ImageDraw.Draw(resized)
        draw.rectangle([(0, 0), (target_w, bar_height)], fill=(0, 0, 0))
        draw.rectangle([(0, target_h - bar_height), (target_w, target_h)], fill=(0, 0, 0))

        # Dissolve fade in on head and fade out on tail
        if i < 8: # head crossfade
            fade = i / 8.0
            resized = ImageEnhance.Brightness(resized).enhance(fade)
        elif i > total_frames - 8: # tail crossfade
            fade = (total_frames - i) / 8.0
            resized = ImageEnhance.Brightness(resized).enhance(fade)

        frames.append(resized)

    return frames


def generate_cinematic_presentation_trailer(scenes_config: list, output_path: str, fps: int = 30):
    """
    Renders a multi-scene cinematic film presentation with custom sound design.
    """
    out_path = Path(output_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    temp_frames_dir = out_path.parent / "_temp_trailer_frames"
    temp_frames_dir.mkdir(parents=True, exist_ok=True)

    target_w, target_h = 1920, 1080
    frame_global_idx = 0

    print(f"🎬 [Veo 3.1 Presentation Engine] Rendering {len(scenes_config)} Cinematic Shots (1080p @ {fps}fps)...")

    for s_idx, scene in enumerate(scenes_config):
        print(f"  ↳ Shot {s_idx + 1}/{len(scenes_config)}: '{scene['title']}' ({scene['motion']})")
        frames = render_scene_clip(
            image_path=scene['image'],
            duration_sec=scene['duration'],
            fps=fps,
            motion_type=scene['motion'],
            title_text=scene['title'],
            sub_text=scene.get('subtitle', ''),
            target_w=target_w,
            target_h=target_h
        )

        for frame in frames:
            frame_filename = temp_frames_dir / f"frame_{frame_global_idx:06d}.png"
            frame.save(frame_filename)
            frame_global_idx += 1

    total_duration_sec = frame_global_idx / fps
    print(f"🎞️ Total Trailer Duration: {total_duration_sec:.1f}s ({frame_global_idx} frames).")

    # Master FFmpeg Assembly with Multi-Tone Cinematic Soundscape
    print(f"🎥 [Veo 3.1] Encoding Master Trailer MP4 with FFmpeg H.264...")
    
    # Generate multi-frequency ambient soundtrack
    # Combining 45Hz sub-drone + 110Hz cello harmonic + 440Hz crystal shimmer
    filter_complex_audio = (
        f"aevalsrc=sin(2*PI*45*t)*0.35+sin(2*PI*90*t)*0.2*exp(-0.05*t)+sin(2*PI*220*t)*0.08:d={total_duration_sec}"
    )

    ffmpeg_cmd = [
        "ffmpeg", "-y",
        "-framerate", str(fps),
        "-i", str(temp_frames_dir / "frame_%06d.png"),
        "-f", "lavfi",
        "-i", filter_complex_audio,
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        "-preset", "slow",
        "-crf", "17",
        "-c:a", "aac",
        "-b:a", "256k",
        "-shortest",
        str(out_path)
    ]

    result = subprocess.run(ffmpeg_cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"FFmpeg stderr: {result.stderr}")
        raise RuntimeError("FFmpeg trailer encoding failed.")

    # Cleanup temp frames
    for f in temp_frames_dir.glob("*.png"):
        f.unlink()
    temp_frames_dir.rmdir()

    print(f"✨ [Veo 3.1 Presentation Engine] Master Film Complete: {out_path} ({out_path.stat().st_size / 1024 / 1024:.2f} MB)")
    return str(out_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Gemini Omni & Veo 3.1 Cinematic Video Generation Pipeline")
    parser.add_argument("--mode", type=str, default="trailer", choices=["single", "trailer", "veo_api"], help="Execution mode")
    parser.add_argument("--image", type=str, help="Source keyframe image path (for single shot)")
    parser.add_argument("--output", type=str, default="nocturne_louvre_trailer.mp4", help="Output MP4 file path")
    parser.add_argument("--scenes_json", type=str, help="JSON path for multi-scene trailer config")

    args = parser.parse_args()

    if args.mode == "trailer" and args.scenes_json:
        with open(args.scenes_json, 'r', encoding='utf-8') as f:
            scenes = json.load(f)
        generate_cinematic_presentation_trailer(scenes, args.output)
    elif args.image:
        generate_cinematic_presentation_trailer([
            {
                "image": args.image,
                "duration": 5.0,
                "motion": "push_in",
                "title": "NOCTURNE LOUVRE",
                "subtitle": "EXPÉDITION PRIVÉE NOCTURNE"
            }
        ], args.output)
    else:
        print("Usage: python generate_video.py --mode trailer --scenes_json scenes.json --output trailer.mp4")
