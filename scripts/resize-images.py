import argparse
import os
from PIL import Image

# python3 /Users/albert/Documents/Projects/lin.github.io/scripts/resize-images.py /Users/albert/Documents/Projects/lin.github.io/content/img/penn --max-mb 1 --suffix=-1mb --extensions jpg,jpeg

def iter_images(folder, extensions, recursive):
    if recursive:
        for root, _, files in os.walk(folder):
            for name in files:
                if name.lower().endswith(extensions):
                    yield os.path.join(root, name)
    else:
        for name in os.listdir(folder):
            if name.lower().endswith(extensions):
                yield os.path.join(folder, name)


def build_output_path(path, suffix):
    base, ext = os.path.splitext(path)
    if base.endswith(suffix):
        return None
    return f"{base}{suffix}{ext}"


def resize_to_limit(
    src_path,
    out_path,
    max_bytes,
    min_quality,
    min_scale,
    max_iterations=20,
):
    with Image.open(src_path) as im:
        im = im.convert("RGB")
        scale = 1.0
        quality = 85
        last_size = None

        for _ in range(max_iterations):
            if scale < min_scale:
                scale = min_scale

            if scale != 1.0:
                new_w = max(1, int(im.width * scale))
                new_h = max(1, int(im.height * scale))
                resized = im.resize((new_w, new_h), Image.LANCZOS)
            else:
                resized = im

            resized.save(
                out_path,
                format="JPEG",
                quality=quality,
                optimize=True,
                progressive=True,
                subsampling=2,
            )
            last_size = os.path.getsize(out_path)
            if last_size <= max_bytes:
                return last_size

            if quality > min_quality:
                quality -= 10
            else:
                scale *= 0.9
                quality = 85

        return last_size


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("folder", help="Target folder containing images")
    parser.add_argument("--max-mb", type=float, default=1.0)
    parser.add_argument("--suffix", default="-1mb")
    parser.add_argument("--min-quality", type=int, default=55)
    parser.add_argument("--min-scale", type=float, default=0.5)
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--recursive", action="store_true")
    parser.add_argument("--extensions", default="jpg,jpeg")
    args = parser.parse_args()

    folder = os.path.abspath(args.folder)
    if not os.path.isdir(folder):
        raise SystemExit(f"Folder not found: {folder}")

    extensions = tuple(f".{ext.strip().lower()}" for ext in args.extensions.split(",") if ext.strip())
    max_bytes = int(args.max_mb * 1_000_000)

    updated = 0
    skipped = 0

    for path in sorted(iter_images(folder, extensions, args.recursive)):
        if os.path.getsize(path) <= max_bytes:
            skipped += 1
            continue

        out_path = build_output_path(path, args.suffix)
        if not out_path:
            skipped += 1
            continue

        if os.path.exists(out_path) and not args.overwrite:
            if os.path.getsize(out_path) <= max_bytes:
                skipped += 1
                continue

        new_size = resize_to_limit(
            src_path=path,
            out_path=out_path,
            max_bytes=max_bytes,
            min_quality=args.min_quality,
            min_scale=args.min_scale,
        )
        updated += 1
        print(f"{os.path.basename(path)} -> {os.path.basename(out_path)} | {new_size / 1_000_000:.2f}MB")

    print(f"Done. Updated: {updated}, Skipped: {skipped}")


if __name__ == "__main__":
    main()
