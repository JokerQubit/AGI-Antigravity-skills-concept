"""
YouTube & Open Multimedia Audio Prospecting Engine
Downloads, extracts, trims, normalizes and converts authentic audio streams into web and video production assets using yt-dlp and ffmpeg.
"""

import os
import sys
import subprocess
from pathlib import Path

# Ensure UTF-8 output on Windows consoles
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

def download_and_extract_audio(query_or_url: str, output_path: str, duration_sec: float = 25.0, start_sec: float = 10.0):
    """
    Searches YouTube or accepts a direct URL, downloads the highest quality audio stream,
    trims to the required duration, applies volume normalization and subtle fade in/out, and saves to output_path.
    """
    out_file = Path(output_path)
    out_file.parent.mkdir(parents=True, exist_ok=True)
    temp_dir = out_file.parent / "_temp_audio"
    temp_dir.mkdir(parents=True, exist_ok=True)
    temp_raw = temp_dir / "raw_audio.opus"

    print(f"🎵 [Audio Prospecting] Prospecting authentic audio for: '{query_or_url}'...")

    # If it's a search term rather than a direct URL, use ytsearch
    search_target = query_or_url if query_or_url.startswith("http") else f"ytsearch1:{query_or_url}"

    # Use yt-dlp to download best audio
    yt_cmd = [
        sys.executable, "-m", "yt_dlp",
        "--no-playlist",
        "--extract-audio",
        "--audio-format", "wav",
        "--output", str(temp_dir / "raw_audio.%(ext)s"),
        search_target
    ]

    print(f"📡 [Audio Prospecting] Fetching real acoustic stream with yt-dlp...")
    res = subprocess.run(yt_cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"yt-dlp stderr: {res.stderr}")
        # Try fallback or check downloaded files
    
    # Locate downloaded audio file in temp_dir
    downloaded_files = list(temp_dir.glob("raw_audio.*"))
    if not downloaded_files:
        raise RuntimeError(f"Failed to extract audio stream from {query_or_url}")

    raw_audio_file = downloaded_files[0]
    print(f"🎛️ [Audio Prospecting] Post-processing audio with FFmpeg (Duration: {duration_sec}s, Fade In/Out)...")

    # Post-process with FFmpeg: trim, normalize audio, add 1s fade-in and 1.5s fade-out
    fade_out_start = max(0, duration_sec - 1.5)
    codec = "libmp3lame" if out_file.suffix.lower() == ".mp3" else "aac"
    ffmpeg_cmd = [
        "ffmpeg", "-y",
        "-ss", str(start_sec),
        "-t", str(duration_sec),
        "-i", str(raw_audio_file),
        "-af", f"loudnorm,afade=t=in:st=0:d=1.0,afade=t=out:st={fade_out_start}:d=1.5",
        "-c:a", codec,
        "-b:a", "256k",
        str(out_file)
    ]

    res_ff = subprocess.run(ffmpeg_cmd, capture_output=True, text=True)
    if res_ff.returncode != 0:
        print(f"FFmpeg stderr: {res_ff.stderr}")
        raise RuntimeError("Audio post-processing failed.")

    # Cleanup temp
    for f in temp_dir.glob("*"):
        try:
            f.unlink()
        except OSError as err:
            print(f"[Cleanup Warning] Could not remove temp file {f}: {err}")
    try:
        temp_dir.rmdir()
    except OSError as err:
        print(f"[Cleanup Warning] Could not remove temp dir {temp_dir}: {err}")

    print(f"✨ [Audio Prospecting] Authentic Audio Mastered: {out_file} ({out_file.stat().st_size / 1024:.1f} KB)")
    return str(out_file)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Extract authentic audio from YouTube/Open Sources")
    parser.add_argument("--query", type=str, required=True, help="Search query or YouTube URL")
    parser.add_argument("--output", type=str, default="authentic_soundscape.mp3", help="Output audio path")
    parser.add_argument("--duration", type=float, default=25.0, help="Duration in seconds")
    parser.add_argument("--start", type=float, default=10.0, help="Start offset in seconds")

    args = parser.parse_args()
    download_and_extract_audio(args.query, args.output, args.duration, args.start)
