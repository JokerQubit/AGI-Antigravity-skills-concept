#!/usr/bin/env python3
"""
Senior Real Acoustic Audio Management Tool.
Strictly governs REAL PHYSICAL SOUND ACQUISITION.
Procedural sine/noise synthesis is permanently BANNED by Constitutional Law 6.

Provides unified access to:
1. YouTube Real Audio Time-Slicing: Extraction of authentic mechanical/acoustic recordings via yt-dlp & ffmpeg.
2. Freesound.org API: Search and download isolated real-world Foley CC0/CC-BY acoustic recordings.
3. Local Sound Asset Indexer: Zero-latency cache and indexing for authentic recorded sound files.
"""

from __future__ import annotations

import argparse
from dataclasses import asdict, dataclass
import json
import os
from pathlib import Path
import re
import subprocess
import sys
from typing import Any, Dict, List, Optional
import urllib.parse
import urllib.request
import uuid


@dataclass
class SoundEffect:
    id: str
    name: str
    duration_seconds: float
    format: str
    provider: str
    source_url: str
    local_path: Optional[str] = None
    tags: Optional[List[str]] = None
    license: Optional[str] = None


class SFXError(Exception):
    """Custom exception for SFX operations."""


class FreesoundClient:
    """Client for querying and fetching authentic acoustic recordings from Freesound API."""

    BASE_URL = "https://freesound.org/apiv2"

    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.environ.get("FREESOUND_API_KEY", "")

    def is_configured(self) -> bool:
        return bool(self.api_key.strip())

    def search(
        self,
        query: str,
        min_duration: float = 0.1,
        max_duration: float = 5.0,
        page_size: int = 10,
        cc0_only: bool = True,
    ) -> List[SoundEffect]:
        """Search Freesound for real acoustic sound effects matching filters."""
        if not self.is_configured():
            return []

        filter_expr = f"duration:[{min_duration:.1f} TO {max_duration:.1f}]"
        if cc0_only:
            filter_expr += ' license:"Creative Commons 0"'

        params = {
            "query": query,
            "filter": filter_expr,
            "fields": "id,name,duration,type,url,previews,tags,license",
            "page_size": str(page_size),
            "token": self.api_key,
        }

        url = f"{self.BASE_URL}/search/text/?{urllib.parse.urlencode(params)}"
        req = urllib.request.Request(url, headers={"User-Agent": "Antigravity-AGI-SFX/2.2"})

        try:
            with urllib.request.urlopen(req, timeout=10) as response:
                payload = json.loads(response.read().decode("utf-8"))
        except Exception as e:
            raise SFXError(f"Freesound API request failed: {e}") from e

        results = []
        for item in payload.get("results", []):
            previews = item.get("previews", {})
            download_url = (
                previews.get("preview-hq-mp3")
                or previews.get("preview-lq-mp3")
                or previews.get("preview-hq-ogg")
                or ""
            )
            results.append(
                SoundEffect(
                    id=str(item.get("id")),
                    name=item.get("name", "untitled_sfx"),
                    duration_seconds=float(item.get("duration", 0.0)),
                    format=item.get("type", "mp3"),
                    provider="freesound",
                    source_url=download_url or item.get("url", ""),
                    tags=item.get("tags", []),
                    license=item.get("license", "CC0"),
                )
            )
        return results

    def download_url(self, url: str, output_path: Path) -> Path:
        """Download real audio stream directly to file via atomic write."""
        output_path.parent.mkdir(parents=True, exist_ok=True)
        tmp_file = output_path.parent / f"{output_path.name}.tmp.{uuid.uuid4().hex[:8]}"

        req = urllib.request.Request(url, headers={"User-Agent": "Antigravity-AGI-SFX/2.2"})
        try:
            with urllib.request.urlopen(req, timeout=30) as resp, open(tmp_file, "wb") as f:
                while chunk := resp.read(65536):
                    f.write(chunk)
            tmp_file.replace(output_path)
        except Exception as e:
            if tmp_file.exists():
                tmp_file.unlink(missing_ok=True)
            raise SFXError(f"Failed to download audio from {url}: {e}") from e

        return output_path

    def download_by_id(self, sound_id: str, output_path: Path) -> Path:
        """Fetch sound metadata by ID and download authentic audio."""
        if not self.is_configured():
            raise SFXError("Freesound API key is required to download by sound ID.")

        url = f"{self.BASE_URL}/sounds/{sound_id}/?token={self.api_key}"
        req = urllib.request.Request(url, headers={"User-Agent": "Antigravity-AGI-SFX/2.2"})
        try:
            with urllib.request.urlopen(req, timeout=10) as response:
                item = json.loads(response.read().decode("utf-8"))
        except Exception as e:
            raise SFXError(f"Failed to fetch Freesound metadata for ID {sound_id}: {e}") from e

        previews = item.get("previews", {})
        download_url = (
            previews.get("preview-hq-mp3")
            or previews.get("preview-lq-mp3")
            or previews.get("preview-hq-ogg")
            or item.get("download", "")
        )
        if not download_url:
            raise SFXError(f"No downloadable audio preview available for Freesound ID {sound_id}.")

        if output_path.is_dir():
            safe_name = re.sub(r"[^\w\-.]", "_", item.get("name", f"sfx_{sound_id}")) + ".mp3"
            dest_file = output_path / safe_name
        else:
            dest_file = output_path

        return self.download_url(download_url, dest_file)


class YouTubeSFXSlicer:
    """Extracts authentic acoustic slices from YouTube recordings using yt-dlp and ffmpeg."""

    TIME_REGEX = re.compile(r"^(\d{1,2}:)?(\d{1,2}:)?\d{1,2}(\.\d{1,3})?$")

    @classmethod
    def validate_timestamp(cls, timestamp: str) -> str:
        """Validate time format HH:MM:SS or MM:SS or SS.ms."""
        ts = timestamp.strip()
        if not cls.TIME_REGEX.match(ts):
            raise SFXError(f"Invalid timestamp format: '{timestamp}'. Expected HH:MM:SS or MM:SS or SS.")
        return ts

    @classmethod
    def build_command(
        cls,
        youtube_url: str,
        start_time: str,
        end_time: str,
        output_file: Path,
        audio_format: str = "wav",
        normalize: bool = True,
    ) -> List[str]:
        """Construct deterministic yt-dlp arguments for audio slice."""
        start_valid = cls.validate_timestamp(start_time)
        end_valid = cls.validate_timestamp(end_time)
        section = f"*{start_valid}-{end_valid}"

        cmd = [
            "yt-dlp",
            "-x",
            "--audio-format",
            audio_format,
            "--download-sections",
            section,
            "--force-keyframes-at-cuts",
            "-o",
            str(output_file.resolve()),
            "--no-playlist",
            "--quiet",
            "--no-warnings",
        ]

        if normalize:
            cmd.extend(["--postprocessor-args", "ffmpeg:-af loudnorm=I=-16:TP=-1.5:LRA=11"])

        cmd.append(youtube_url)
        return cmd

    def slice_audio(
        self,
        youtube_url: str,
        start_time: str,
        end_time: str,
        output_file: Path,
        audio_format: str = "wav",
        normalize: bool = True,
    ) -> Path:
        """Execute yt-dlp command to extract isolated real-world audio segment."""
        output_file.parent.mkdir(parents=True, exist_ok=True)
        tmp_output = output_file.with_name(f"{output_file.stem}_tmp_{uuid.uuid4().hex[:6]}.{audio_format}")

        cmd = self.build_command(
            youtube_url=youtube_url,
            start_time=start_time,
            end_time=end_time,
            output_file=tmp_output,
            audio_format=audio_format,
            normalize=normalize,
        )

        try:
            proc = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                check=False,
                timeout=120,
            )
        except subprocess.TimeoutExpired as e:
            if tmp_output.exists():
                tmp_output.unlink(missing_ok=True)
            raise SFXError("yt-dlp slice operation timed out after 120s.") from e
        except FileNotFoundError as e:
            raise SFXError("yt-dlp executable not found in system PATH. Please install yt-dlp to slice real audio.") from e

        if proc.returncode != 0:
            if tmp_output.exists():
                tmp_output.unlink(missing_ok=True)
            raise SFXError(f"yt-dlp failed (code {proc.returncode}): {proc.stderr.strip()}")

        actual_created = tmp_output
        if not actual_created.exists():
            candidates = list(tmp_output.parent.glob(f"{tmp_output.stem}*"))
            if candidates:
                actual_created = candidates[0]
            else:
                raise SFXError("Audio slice was not produced on disk.")

        actual_created.replace(output_file)
        return output_file


class LocalSFXLibrary:
    """Manages and indexes local authentic audio packs for zero-latency retrieval."""

    SUPPORTED_EXTENSIONS = {".wav", ".mp3", ".ogg", ".flac", ".m4a"}

    def __init__(self, library_dir: Optional[Path] = None):
        self.library_dir = library_dir or Path(__file__).resolve().parent.parent / "assets" / "sfx"

    def scan(self) -> List[SoundEffect]:
        """Scan local folder and return indexed real sound effects."""
        if not self.library_dir.exists():
            return []

        sounds = []
        for file_path in self.library_dir.rglob("*"):
            if file_path.is_file() and file_path.suffix.lower() in self.SUPPORTED_EXTENSIONS:
                category = file_path.parent.name
                sounds.append(
                    SoundEffect(
                        id=f"local_{file_path.stem}",
                        name=file_path.stem,
                        duration_seconds=0.0,
                        format=file_path.suffix.lstrip(".").lower(),
                        provider="local",
                        source_url=f"file:///{file_path.as_posix()}",
                        local_path=str(file_path.resolve()),
                        tags=[category, file_path.stem],
                        license="CC0/Local",
                    )
                )
        return sounds

    def search(self, query: str) -> List[SoundEffect]:
        """Fuzzy match query against filename and directory tags."""
        q = query.lower()
        results = []
        for sound in self.scan():
            matches_name = q in sound.name.lower()
            matches_tags = any(q in (tag or "").lower() for tag in (sound.tags or []))
            if matches_name or matches_tags:
                results.append(sound)
        return results


class SFXManager:
    """Unified facade coordinating Freesound, YouTube slicing, and Local Library."""

    def __init__(self, freesound_key: Optional[str] = None, local_dir: Optional[Path] = None):
        self.freesound = FreesoundClient(freesound_key)
        self.youtube = YouTubeSFXSlicer()
        self.local = LocalSFXLibrary(local_dir)

    def download(self, source: str, output_path: Path) -> Path:
        """Download real sound effect from direct URL or Freesound sound ID."""
        if source.startswith("http://") or source.startswith("https://"):
            return self.freesound.download_url(source, output_path)
        return self.freesound.download_by_id(source, output_path)

    def search(
        self,
        query: str,
        max_duration: float = 3.0,
        provider: str = "all",
    ) -> List[SoundEffect]:
        """Search across real sound providers."""
        results: List[SoundEffect] = []

        if provider in ("local", "all"):
            results.extend(self.local.search(query))

        if provider in ("freesound", "all") and self.freesound.is_configured():
            try:
                fs_results = self.freesound.search(query, max_duration=max_duration)
                results.extend(fs_results)
            except SFXError:
                pass

        return results


def main() -> int:
    parser = argparse.ArgumentParser(description="Antigravity Real Physical SFX Manager (Zero Synthetic Audio Engine)")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # 1. BANNED: Procedural synthesis blocker
    p_gen = subparsers.add_parser("generate", help="BANNED: Synthetic audio synthesis is prohibited by Law 6")
    p_gen.add_argument("--type", "-t", dest="preset", required=False)
    p_gen.add_argument("--output", "-o", required=False)

    # 2. Slice YouTube command
    p_slice = subparsers.add_parser("slice-youtube", help="Extract authentic acoustic slice from YouTube with yt-dlp")
    p_slice.add_argument("url", help="YouTube video URL")
    p_slice.add_argument("--start", required=True, help="Start time (HH:MM:SS or MM:SS or SS)")
    p_slice.add_argument("--end", required=True, help="End time (HH:MM:SS or MM:SS or SS)")
    p_slice.add_argument("--output", required=True, help="Destination audio file path (e.g. public/sfx/tactile_click.wav)")
    p_slice.add_argument("--format", default="wav", choices=["wav", "mp3", "ogg"])
    p_slice.add_argument("--no-normalize", action="store_true", help="Disable audio loudness normalization")

    # 3. Download sound (Freesound CC0 or direct URL)
    p_dl = subparsers.add_parser("download", help="Download authentic Foley audio from Freesound ID or direct CC0 URL")
    p_dl.add_argument("source", help="Freesound sound ID (e.g. 12345) or direct audio URL (https://...)")
    p_dl.add_argument("--output", "-o", required=True, help="Destination file path")
    p_dl.add_argument("--api-key", help="Optional Freesound API key")

    # 4. Search command
    p_search = subparsers.add_parser("search", help="Search for authentic sound effects in local library or Freesound")
    p_search.add_argument("query", help="Search terms (e.g. 'mechanical shutter', 'luxury door click')")
    p_search.add_argument("--max-duration", type=float, default=3.0, help="Max duration in seconds")
    p_search.add_argument("--provider", choices=["all", "local", "freesound"], default="all")
    p_search.add_argument("--json", action="store_true", help="Output results as JSON")

    # 5. Scan local library
    p_local = subparsers.add_parser("scan-local", help="List all authentic local audio recordings")
    p_local.add_argument("--dir", help="Custom local library directory")
    p_local.add_argument("--json", action="store_true", help="Output results as JSON")

    args = parser.parse_args()

    # ENFORCE CONSTITUTIONAL LAW 6: HARD BLOCK ON SYNTHETIC GENERATION
    if args.command == "generate":
        print(
            "CRITICAL HARD HALT - CONSTITUTIONAL LAW 6 VIOLATION:\n"
            "Generating synthetic noise, mathematical sine waves or robotic beeps via script is strictly BANNED.\n"
            "All sound effects must be authentic real-world acoustic recordings.\n"
            "Use 'python scripts/sfx_tool.py slice-youtube <URL> --start <TS> --end <TS> -o <PATH>'\n"
            "or 'python scripts/sfx_tool.py download <FREESOUND_ID_OR_CC0_URL> -o <PATH>' instead.",
            file=sys.stderr,
        )
        return 1

    api_key = getattr(args, "api_key", None)
    manager = SFXManager(freesound_key=api_key)

    if args.command == "slice-youtube":
        out_path = Path(args.output)
        try:
            saved = manager.youtube.slice_audio(
                youtube_url=args.url,
                start_time=args.start,
                end_time=args.end,
                output_file=out_path,
                audio_format=args.format,
                normalize=not args.no_normalize,
            )
            print(f"Successfully extracted authentic acoustic slice to: {saved.resolve()}")
            return 0
        except SFXError as e:
            print(f"Error extracting YouTube audio slice: {e}", file=sys.stderr)
            return 1

    if args.command == "download":
        out_path = Path(args.output)
        try:
            downloaded = manager.download(source=args.source, output_path=out_path)
            print(f"Successfully downloaded authentic audio: {downloaded.resolve()}")
            return 0
        except SFXError as e:
            print(f"Error downloading audio: {e}", file=sys.stderr)
            return 1

    if args.command == "search":
        results = manager.search(query=args.query, max_duration=args.max_duration, provider=args.provider)
        if args.json:
            print(json.dumps([asdict(r) for r in results], indent=2))
        else:
            print(f"Found {len(results)} authentic SFX results for '{args.query}':")
            for r in results:
                print(f"[{r.provider.upper()}] {r.name} ({r.format}, {r.duration_seconds:.1f}s) -> {r.source_url}")
        return 0

    if args.command == "scan-local":
        local_dir = Path(args.dir) if args.dir else None
        lib = LocalSFXLibrary(local_dir)
        sounds = lib.scan()
        if args.json:
            print(json.dumps([asdict(s) for s in sounds], indent=2))
        else:
            print(f"Indexed {len(sounds)} local sound files.")
            for s in sounds:
                print(f" - {s.name} ({s.format}): {s.local_path}")
        return 0

    return 0


if __name__ == "__main__":
    sys.exit(main())
