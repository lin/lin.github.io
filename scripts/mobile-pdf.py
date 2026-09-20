#!/usr/bin/env python3
"""
Generate a mobile-reading PDF for one or more posts in this Hugo site.

By default (`--format mobile`) each post becomes a PDF whose pages are
phone-width (default 390 CSS px, the iPhone 12 Pro logical width) and where
every `## ` (H2) section starts on its own page. Each page is exactly as tall
as that section renders -- no internal pagination, no trailing whitespace.

With `--format a4` the post is instead rendered onto standard A4 paper
(210mm wide, real print margins) with normal, printer-friendly pagination --
suitable for printing or sharing as a regular document.

USAGE
    scripts/mobile-pdf.py kao                 # -> content/posts/我的中高考-手机版.pdf  (named from the post title)
    scripts/mobile-pdf.py kao --format a4      # -> content/posts/我的中高考-A4版.pdf
    scripts/mobile-pdf.py content/posts/liuxiang.md -o ~/Desktop/lx.pdf
    scripts/mobile-pdf.py kao liuxiang irresponsible
    scripts/mobile-pdf.py all                 # every published post in content/posts/
    scripts/mobile-pdf.py all --drafts --outdir /tmp/pdfs

    npm run mobile-pdf -- kao                 # same, via package.json

OPTIONS
    -o, --output PATH   Output file. Only valid with a single post.
    --outdir DIR        Directory for outputs (default: next to each source .md).
    -f, --format {mobile,a4}  Page style (default mobile).
    --width PX          Page width in CSS px (default 390 for mobile, 794 for a4).
    --scale N           Image render scale / device pixel ratio (default 2).
    --split {h2,h1,none}  Where to break pages (default h2 for mobile, none for a4).
    --drafts           Include draft / future-dated posts (for `all`).
    --port N            Local static-server port (default 8899).
    --no-build         Reuse an existing ./public build instead of building fresh.
    --keep             Keep the temporary build directory (prints its path).

REQUIREMENTS
    hugo, pdfunite (poppler), and Python `playwright` with a usable Chrome
    (`pip install playwright` -- this script uses the system Google Chrome via
    channel="chrome", so `playwright install` is not required).
"""
from __future__ import annotations

import argparse
import atexit
import csv
import io
import os
import shutil
import signal
import subprocess
import sys
import tempfile
import time
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DEFAULT_WIDTH = 390
A4_WIDTH = 794  # CSS px, 210mm @ 96dpi
DEFAULT_SCALE = 2
SUFFIX = {"mobile": "手机版", "a4": "A4版"}  # <base>-手机版.pdf / <base>-A4版.pdf


# --------------------------------------------------------------------------- #
# helpers
# --------------------------------------------------------------------------- #
def die(msg: str, code: int = 1):
    print(f"error: {msg}", file=sys.stderr)
    sys.exit(code)


def need(binary: str, hint: str = ""):
    if shutil.which(binary) is None:
        die(f"`{binary}` not found on PATH." + (f" {hint}" if hint else ""))


def sh(cmd: list[str], **kw) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, cwd=REPO, text=True, capture_output=True, **kw)


# --------------------------------------------------------------------------- #
# post discovery (path/slug -> local URL) via `hugo list all`
# --------------------------------------------------------------------------- #
def load_post_index() -> list[dict]:
    r = sh(["hugo", "list", "all"])
    if r.returncode != 0:
        die("`hugo list all` failed:\n" + r.stderr)
    rows = list(csv.DictReader(io.StringIO(r.stdout)))
    posts = []
    for row in rows:
        if row.get("kind") != "page":
            continue
        if row.get("section") not in ("posts", "pages"):
            continue
        posts.append(row)
    return posts


def is_published(row: dict) -> bool:
    if str(row.get("draft", "")).lower() == "true":
        return False
    pub = row.get("publishDate", "") or row.get("date", "")
    # publishDate like 2026-11-22T00:00:00Z ; compare date part only
    try:
        from datetime import datetime, timezone

        d = datetime.fromisoformat(pub.replace("Z", "+00:00"))
        return d <= datetime.now(timezone.utc)
    except Exception:
        return True


def _safe_name(s: str) -> str:
    for ch in '/\\:*?"<>|':
        s = s.replace(ch, "-")
    return s.strip() or "post"


def resolve_targets(args, posts: list[dict], base_url: str) -> list[tuple[Path, str, str]]:
    """Return list of (source_path, local_url, output_stem)."""
    by_path = {row["path"]: row for row in posts}
    by_stem = {Path(row["path"]).stem: row for row in posts}

    def to_local(permalink: str) -> str:
        from urllib.parse import urlsplit

        path = urlsplit(permalink).path or "/"
        return base_url.rstrip("/") + path

    def stem_for(row: dict) -> str:
        # prefer the post title (matches this repo's Chinese-filename convention),
        # fall back to the source basename
        return _safe_name(row.get("title") or "") or Path(row["path"]).stem

    if args.targets == ["all"]:
        chosen = [
            row
            for row in posts
            if args.drafts or is_published(row)
        ]
        if not chosen:
            die("no posts matched")
        return [
            (REPO / row["path"], to_local(row["permalink"]), stem_for(row))
            for row in sorted(chosen, key=lambda r: r["path"])
        ]

    out = []
    for t in args.targets:
        row = None
        p = Path(t)
        # try: explicit path
        rel = None
        if p.suffix == ".md":
            try:
                rel = str(p.resolve().relative_to(REPO))
            except ValueError:
                rel = t
            row = by_path.get(rel)
        # try: bare slug / stem
        if row is None:
            row = by_stem.get(p.stem) or by_stem.get(t)
        if row is None:
            die(f"could not find a post for '{t}'. "
                f"Try a slug like 'kao' or a path like 'content/posts/kao.md'.")
        out.append((REPO / row["path"], to_local(row["permalink"]), stem_for(row)))
    return out


# --------------------------------------------------------------------------- #
# build + serve
# --------------------------------------------------------------------------- #
def build_site(base_url: str, keep: bool) -> Path:
    dest = Path(tempfile.mkdtemp(prefix="mobilepdf-site-"))
    if not keep:
        atexit.register(lambda: shutil.rmtree(dest, ignore_errors=True))
    print(f"building site -> {dest}")
    r = sh(
        ["hugo", "--baseURL", base_url, "-D", "-F", "--destination", str(dest),
         "--logLevel", "error"]
    )
    if r.returncode != 0:
        die("hugo build failed:\n" + r.stderr)
    if keep:
        print(f"  (kept: {dest})")
    return dest


def serve(root: Path, port: int) -> subprocess.Popen:
    proc = subprocess.Popen(
        [sys.executable, "-m", "http.server", str(port), "--bind", "127.0.0.1"],
        cwd=root,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    atexit.register(lambda: proc.terminate())
    # wait for it
    import urllib.request

    for _ in range(50):
        try:
            urllib.request.urlopen(f"http://127.0.0.1:{port}/", timeout=1)
            return proc
        except Exception:
            time.sleep(0.1)
    die("local static server did not come up")


# --------------------------------------------------------------------------- #
# per-post rendering
# --------------------------------------------------------------------------- #
OVERRIDE_CSS = """
<style id="mobile-pdf-override">
  html,body{margin:0!important;padding:0!important;background:#fff!important;}
  .container.wrapper,.wrapper,.container,.post,.markdown,.content{
     max-width:100%!important;width:auto!important;margin:0!important;
     padding:0!important;box-shadow:none!important;border:0!important;}
  body{padding:18px 18px 26px!important;}
  /* trim the gap above the first block on each section page, but never touch
     its padding -- zeroing padding-top lets a child <p>'s margin collapse out
     and glues the epigraph text to the top of its box */
  .markdown > h1:first-child,
  .markdown > h2:first-child,
  .markdown > h3:first-child{margin-top:0!important;}
  .markdown > blockquote:first-child{margin-top:4px!important;}
  /* clean single-column header (replaces the theme's flex date-badge, which
     never top-aligned the date digit with the title) */
  .pdf-head{margin:2px 0 24px 0;}
  .pdf-head .pdf-title{margin:0 0 8px 0;padding:0;font-weight:600;font-size:1.9rem;
     line-height:1.3;letter-spacing:.5px;color:#222;}
  .pdf-head .pdf-meta{font-size:13px;line-height:1.4;color:#8a8a8a;}
  .pdf-head .pdf-meta a{color:#3700ff;}
  .pdf-head .pdf-meta .sep{margin:0 .5em;opacity:.6;}
  img{max-width:100%!important;height:auto!important;}
  figure{margin:14px 0!important;text-align:center!important;}
  figcaption{font-size:12px!important;color:#555!important;line-height:1.4!important;}
  a{text-decoration:none!important;}
  .header,.footer,.site-header,nav.nav,.tags,#livereload,.post-info,.pagination{display:none!important;}
</style>
"""

# a4 pages get real print margins from page.pdf(), so drop the mobile body padding
A4_OVERRIDE_CSS = """
<style id="mobile-pdf-a4-override">
  body{padding:0!important;}
</style>
"""

CANONICAL_ORIGIN = "https://yingkui.com"

# Runs on the live post page before we extract HTML: rewrite every in-site link
# (root-relative "/x", "./x", "../x", bare "x") to an absolute
# https://yingkui.com/... URL so the links work from inside the PDF.
PREP_JS = r"""
(origin) => {
  const basePath = location.pathname;
  document.querySelectorAll('.markdown a[href]').forEach(a => {
    const raw = a.getAttribute('href');
    if (!raw) return;
    if (/^(https?:)?\/\//i.test(raw)) return;               // absolute / protocol-relative
    if (/^(mailto:|tel:|data:|javascript:|#)/i.test(raw)) return;  // non-navigational / in-page
    try { a.setAttribute('href', new URL(raw, origin + basePath).href); } catch (e) {}
  });
}
"""

SPLIT_JS = r"""
(splitTag) => {
  const md = document.querySelector('.markdown');
  if (!md) return null;
  const titleEl = document.querySelector('.post-header h1.title, .post-header .title');
  const dayEl = document.querySelector('.post-header .meta .date .day');
  const restEl = document.querySelector('.post-header .meta .date .rest');
  const title = titleEl ? titleEl.textContent.trim() : document.title;
  const date = [dayEl && dayEl.textContent.trim(), restEl && restEl.textContent.trim()]
                 .filter(Boolean).join(' ');
  const els = [...md.children];
  const tag = splitTag ? splitTag.toUpperCase() : null;
  const whole = { title, date, sections: [md.innerHTML] };
  if (!tag) return whole;
  const marks = els.filter(e => e.tagName === tag);
  if (marks.length === 0) return whole;
  let pre = '';
  for (const e of els) { if (e.tagName === tag) break; pre += e.outerHTML; }
  const sections = [];
  for (let i = 0; i < marks.length; i++) {
    let html = marks[i].outerHTML;
    let n = marks[i].nextElementSibling;
    while (n && n.tagName !== tag) { html += n.outerHTML; n = n.nextElementSibling; }
    if (i === 0) html = pre + html;
    sections.push(html);
  }
  return { title, date, sections };
}
"""


def header_html(title: str, date: str, canonical_href: str, canonical_text: str) -> str:
    import html as _html

    bits = []
    if date:
        bits.append(f"<span class='date'>{_html.escape(date)}</span>")
    bits.append(
        f"<a href='{_html.escape(canonical_href)}'>{_html.escape(canonical_text)}</a>"
    )
    meta = "<span class='sep'>·</span>".join(bits)
    return (
        f"<div class='pdf-head'>"
        f"<h1 class='pdf-title'>{_html.escape(title)}</h1>"
        f"<div class='pdf-meta'>{meta}</div>"
        f"</div>"
    )


def build_doc(url: str, head_html: str, header: str, inner: str, extra_css: str = "") -> str:
    return (
        f"<!doctype html><html><head><base href='{url}'>{head_html}{OVERRIDE_CSS}{extra_css}"
        f"</head><body><div class='container wrapper'><div class='post'>"
        f"{header}"
        f"<div class='markdown'>{inner}</div></div></div></body></html>"
    )


def render_post(page, url, out_path: Path, width: int, split: str, fmt: str, workdir: Path):
    from urllib.parse import urlsplit

    page.set_viewport_size({"width": width, "height": 900})
    page.goto(url, wait_until="networkidle")
    page.wait_for_timeout(1200)  # KaTeX / late layout

    path = urlsplit(url).path or "/"
    canonical_href = CANONICAL_ORIGIN + path
    canonical_text = (CANONICAL_ORIGIN + path).split("://", 1)[1].rstrip("/")
    page.evaluate(PREP_JS, CANONICAL_ORIGIN)

    head_html = page.evaluate("document.head.innerHTML")
    data = page.evaluate(SPLIT_JS, None if split == "none" else split)
    if data is None:
        die(f"{url}: no .markdown container found (unexpected theme layout)")
    sections = data["sections"]
    header = header_html(data["title"], data["date"], canonical_href, canonical_text)

    page.emulate_media(media="screen")
    extra_css = A4_OVERRIDE_CSS if fmt == "a4" else ""
    parts = []
    for i, inner in enumerate(sections, 1):
        page.set_content(build_doc(url, head_html, header if i == 1 else "", inner, extra_css),
                         wait_until="networkidle")
        page.wait_for_timeout(700)
        part = workdir / f"{out_path.stem}-{i:02d}.pdf"
        if fmt == "a4":
            # standard A4 paper with real margins; Chrome paginates normally
            page.pdf(
                path=str(part),
                format="A4",
                print_background=True,
                margin={"top": "18mm", "bottom": "18mm", "left": "16mm", "right": "16mm"},
            )
        else:
            h = page.evaluate("Math.ceil(document.body.getBoundingClientRect().height) + 4")
            page.pdf(
                path=str(part),
                width=f"{width}px",
                height=f"{h}px",
                print_background=True,
                margin={"top": "0", "bottom": "0", "left": "0", "right": "0"},
                prefer_css_page_size=False,
            )
        parts.append(part)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    if len(parts) == 1:
        shutil.copyfile(parts[0], out_path)
    else:
        r = subprocess.run(["pdfunite", *map(str, parts), str(out_path)],
                           capture_output=True, text=True)
        if r.returncode != 0:
            die("pdfunite failed:\n" + r.stderr)
    for p in parts:
        p.unlink(missing_ok=True)
    return len(sections)


# --------------------------------------------------------------------------- #
# main
# --------------------------------------------------------------------------- #
def main():
    ap = argparse.ArgumentParser(
        description="Generate mobile-reading PDFs for posts in this Hugo site.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    ap.add_argument("targets", nargs="+", metavar="POST",
                    help="post slug(s), path(s) to .md, or the literal 'all'")
    ap.add_argument("-o", "--output", type=Path, help="output file (single post only)")
    ap.add_argument("--outdir", type=Path, help="output directory (default: beside source)")
    ap.add_argument("-f", "--format", choices=["mobile", "a4"], default="mobile",
                    help="mobile = phone-width borderless pages (default); "
                         "a4 = standard A4 print pages")
    ap.add_argument("--width", type=int, default=None,
                    help=f"page width in CSS px (default {DEFAULT_WIDTH} for mobile, "
                         f"{A4_WIDTH} for a4)")
    ap.add_argument("--scale", type=int, default=DEFAULT_SCALE)
    ap.add_argument("--split", choices=["h2", "h1", "none"], default=None,
                    help="where to break pages (default h2 for mobile, none for a4)")
    ap.add_argument("--drafts", action="store_true")
    ap.add_argument("--port", type=int, default=8899)
    ap.add_argument("--no-build", action="store_true")
    ap.add_argument("--keep", action="store_true")
    args = ap.parse_args()
    if args.width is None:
        args.width = A4_WIDTH if args.format == "a4" else DEFAULT_WIDTH
    if args.split is None:
        args.split = "none" if args.format == "a4" else "h2"

    need("hugo")
    need("pdfunite", "install poppler (brew install poppler)")
    try:
        from playwright.sync_api import sync_playwright  # noqa
    except ImportError:
        die("python package `playwright` not installed (pip install playwright)")

    base_url = f"http://127.0.0.1:{args.port}/"

    posts = load_post_index()
    targets = resolve_targets(args, posts, base_url)

    if args.output and len(targets) != 1:
        die("-o/--output only works with a single post")

    if args.no_build:
        site_root = REPO / "public"
        if not site_root.exists():
            die("./public does not exist; drop --no-build to build it")
        # rewrite base_url to whatever public was built with? assume localhost served
        print(f"serving existing {site_root}")
    else:
        site_root = build_site(base_url, args.keep)

    serve(site_root, args.port)

    workdir = Path(tempfile.mkdtemp(prefix="mobilepdf-parts-"))
    atexit.register(lambda: shutil.rmtree(workdir, ignore_errors=True))

    from playwright.sync_api import sync_playwright

    made = []
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome")
        ctx = browser.new_context(
            viewport={"width": args.width, "height": 900},
            device_scale_factor=args.scale,
        )
        page = ctx.new_page()

        for src, url, stem in targets:
            if args.output:
                out_path = args.output
            else:
                out_dir = args.outdir or src.parent
                out_path = out_dir / f"{stem}-{SUFFIX[args.format]}.pdf"
            print(f"→ {stem}  ({url})")
            n = render_post(page, url, out_path, args.width, args.split, args.format, workdir)
            size = out_path.stat().st_size / 1e6
            print(f"  {n} page(s), {size:.1f} MB  -> {out_path}")
            made.append(out_path)

        browser.close()

    print(f"\ndone: {len(made)} PDF(s)")


if __name__ == "__main__":
    main()
