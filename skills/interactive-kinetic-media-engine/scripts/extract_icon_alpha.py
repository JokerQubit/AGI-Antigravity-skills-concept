#!/usr/bin/env python3
"""
extract_icon_alpha.py
Extracts pure white or chroma background from 3D isometric icons generated via Nano Banana,
generating high-transparency alpha PNGs for web and UI integration.
"""

import sys
import os
from PIL import Image
import numpy as np

def extract_alpha(input_path: str, output_path: str, tolerance: int = 240, mode: str = 'white') -> None:
    if not os.path.exists(input_path):
        print(f"Error: Input file {input_path} does not exist.")
        sys.exit(1)

    img = Image.open(input_path).convert("RGBA")
    data = np.array(img, dtype=np.uint8)

    r, g, b, a = data[:, :, 0], data[:, :, 1], data[:, :, 2], data[:, :, 3]

    if mode == 'white':
        # Detect near-white pixels
        bg_mask = (r >= tolerance) & (g >= tolerance) & (b >= tolerance)
    elif mode == 'black':
        # Detect near-black pixels
        bg_mask = (r <= (255 - tolerance)) & (g <= (255 - tolerance)) & (b <= (255 - tolerance))
    elif mode == 'chroma_green':
        # Detect chroma key green
        bg_mask = (g > 180) & (r < 100) & (b < 100)
    else:
        raise ValueError(f"Unknown mode: {mode}")

    # Set transparent alpha for background mask
    data[:, :, 3][bg_mask] = 0

    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    result = Image.fromarray(data)
    result.save(output_path, "PNG")
    print(f"Successfully created transparent icon asset: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python extract_icon_alpha.py <input_image_path> <output_png_path> [tolerance=240] [mode=white|black|chroma_green]")
        sys.exit(1)

    in_file = sys.argv[1]
    out_file = sys.argv[2]
    tol = int(sys.argv[3]) if len(sys.argv) > 3 else 240
    m = sys.argv[4] if len(sys.argv) > 4 else 'white'

    extract_alpha(in_file, out_file, tolerance=tol, mode=m)
