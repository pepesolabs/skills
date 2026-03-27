#!/usr/bin/env python3
"""
extract_palette.py — Extract dominant color palette from an image.

Usage:
    python3 extract_palette.py <image_path> [--colors N] [--format css|json|table]

Output:
    Prints the dominant colors in the specified format (default: table).

Requirements:
    pip install Pillow colorthief

Examples:
    python3 extract_palette.py screenshot.png
    python3 extract_palette.py design.jpg --colors 8 --format css
    python3 extract_palette.py mockup.png --format json
"""

import sys
import json
import argparse
from pathlib import Path


def rgb_to_hex(rgb: tuple[int, int, int]) -> str:
    return "#{:02X}{:02X}{:02X}".format(*rgb)


def rgb_to_hsl(rgb: tuple[int, int, int]) -> tuple[float, float, float]:
    r, g, b = (x / 255.0 for x in rgb)
    max_c, min_c = max(r, g, b), min(r, g, b)
    delta = max_c - min_c
    l = (max_c + min_c) / 2

    if delta == 0:
        h = s = 0.0
    else:
        s = delta / (1 - abs(2 * l - 1))
        if max_c == r:
            h = ((g - b) / delta) % 6
        elif max_c == g:
            h = (b - r) / delta + 2
        else:
            h = (r - g) / delta + 4
        h = (h * 60) % 360

    return round(h, 1), round(s * 100, 1), round(l * 100, 1)


def classify_color(rgb: tuple[int, int, int]) -> str:
    """Return a rough semantic label for the color."""
    h, s, l = rgb_to_hsl(rgb)
    if l < 10:
        return "Near Black"
    if l > 90:
        return "Near White"
    if s < 12:
        return "Neutral Grey"
    if 0 <= h < 30 or h >= 330:
        return "Red / Pink"
    if 30 <= h < 60:
        return "Orange / Yellow"
    if 60 <= h < 90:
        return "Yellow / Lime"
    if 90 <= h < 150:
        return "Green"
    if 150 <= h < 195:
        return "Teal / Cyan"
    if 195 <= h < 255:
        return "Blue"
    if 255 <= h < 285:
        return "Indigo / Violet"
    if 285 <= h < 330:
        return "Purple / Magenta"
    return "Unknown"


def infer_theme(palette: list[tuple[int, int, int]]) -> str:
    """Heuristically infer the broad design theme from the palette."""
    hsls = [rgb_to_hsl(c) for c in palette]
    avg_l = sum(l for _, _, l in hsls) / len(hsls)
    avg_s = sum(s for _, s, _ in hsls) / len(hsls)
    has_neon = any(s > 80 and 30 < l < 70 for _, s, l in hsls)
    low_l_count = sum(1 for _, _, l in hsls if l < 20)
    high_contrast = max(l for _, _, l in hsls) - min(l for _, _, l in hsls) > 60

    if avg_l < 30 and has_neon:
        return "Dark / Cyberpunk"
    if avg_l < 35:
        return "Dark Mode"
    if avg_s < 15:
        return "Monochrome / Minimal"
    if avg_s > 60 and avg_l > 60:
        return "Vibrant / Playful"
    if avg_s < 40 and 60 < avg_l < 85:
        return "Pastel / Soft"
    if avg_l > 80 and high_contrast:
        return "Neobrutalism (light)"
    if avg_l > 75:
        return "Light / Clean"
    if 35 < avg_l < 65 and avg_s > 30:
        return "Earthy / Natural"
    return "Balanced / Neutral"


def extract_palette(image_path: str, n_colors: int = 6) -> list[tuple[int, int, int]]:
    """Extract palette using colorthief. Falls back to Pillow quantize if unavailable."""
    try:
        from colorthief import ColorThief
        ct = ColorThief(image_path)
        palette = ct.get_palette(color_count=n_colors, quality=1)
        return palette[:n_colors]
    except ImportError:
        pass

    # Pillow fallback (less accurate but always available)
    from PIL import Image
    img = Image.open(image_path).convert("RGB")
    img = img.resize((200, 200))  # Downsample for speed
    quantized = img.quantize(colors=n_colors, method=Image.Quantize.MEDIANCUT)
    palette_data = quantized.getpalette()
    colors = []
    for i in range(n_colors):
        r, g, b = palette_data[i*3], palette_data[i*3+1], palette_data[i*3+2]
        colors.append((r, g, b))
    return colors


def output_table(palette: list[tuple[int, int, int]], theme: str):
    print(f"\n🎨 Inferred Theme: {theme}\n")
    print(f"{'#':<4} {'HEX':<10} {'RGB':<20} {'HSL':<25} {'Label'}")
    print("-" * 75)
    for i, rgb in enumerate(palette, 1):
        hex_val = rgb_to_hex(rgb)
        hsl = rgb_to_hsl(rgb)
        label = classify_color(rgb)
        rgb_str = f"rgb({rgb[0]}, {rgb[1]}, {rgb[2]})"
        hsl_str = f"hsl({hsl[0]:.0f}, {hsl[1]:.0f}%, {hsl[2]:.0f}%)"
        print(f"{i:<4} {hex_val:<10} {rgb_str:<20} {hsl_str:<25} {label}")


def output_css(palette: list[tuple[int, int, int]], theme: str):
    print(f"/* Extracted palette — Inferred theme: {theme} */")
    print(":root {")
    for i, rgb in enumerate(palette, 1):
        hex_val = rgb_to_hex(rgb)
        label = classify_color(rgb).lower().replace(" ", "-").replace("/", "")
        print(f"  --color-{i}: {hex_val};  /* {label} */")
    print("}")


def output_json(palette: list[tuple[int, int, int]], theme: str):
    result = {
        "inferred_theme": theme,
        "palette": [
            {
                "index": i,
                "hex": rgb_to_hex(rgb),
                "rgb": {"r": rgb[0], "g": rgb[1], "b": rgb[2]},
                "hsl": {
                    "h": rgb_to_hsl(rgb)[0],
                    "s": rgb_to_hsl(rgb)[1],
                    "l": rgb_to_hsl(rgb)[2],
                },
                "label": classify_color(rgb),
            }
            for i, rgb in enumerate(palette, 1)
        ],
    }
    print(json.dumps(result, indent=2))


def main():
    parser = argparse.ArgumentParser(
        description="Extract dominant color palette from an image.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("image", help="Path to the image file")
    parser.add_argument(
        "--colors", "-n", type=int, default=6,
        help="Number of colors to extract (default: 6)"
    )
    parser.add_argument(
        "--format", "-f", choices=["table", "css", "json"], default="table",
        help="Output format (default: table)"
    )
    args = parser.parse_args()

    image_path = Path(args.image)
    if not image_path.exists():
        print(f"Error: File not found: {image_path}", file=sys.stderr)
        sys.exit(1)

    try:
        from PIL import Image  # noqa: F401
    except ImportError:
        print("Error: Pillow is required. Run: pip install Pillow", file=sys.stderr)
        sys.exit(1)

    palette = extract_palette(str(image_path), args.colors)
    theme = infer_theme(palette)

    if args.format == "table":
        output_table(palette, theme)
    elif args.format == "css":
        output_css(palette, theme)
    elif args.format == "json":
        output_json(palette, theme)


if __name__ == "__main__":
    main()
