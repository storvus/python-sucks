#!/usr/bin/env python3
"""
Export a markdown post to dev.to

Usage:
    python scripts/export_to_devto.py <filename> [--publish] [--canonical]

Options:
    --publish    Publish immediately (default: save as draft)
    --canonical  Set canonical_url to https://blog.storv.us/posts/<slug>

Environment:
    DEVTO_API_KEY  Your dev.to API key (dev.to → Settings → Extensions → DEV API Keys)

Example:
    DEVTO_API_KEY=xxx python scripts/export_to_devto.py mutable-immutable.md --publish --canonical
"""

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

POSTS_DIR = Path(__file__).parent.parent / "src" / "content" / "posts"
SITE_URL = "https://blog.storv.us"
DEVTO_API = "https://dev.to/api/articles"


def parse_frontmatter(content: str) -> tuple[dict, str]:
    match = re.match(r"^---\n(.*?)\n---\n(.*)", content, re.DOTALL)
    if not match:
        raise ValueError("No YAML frontmatter found in file")

    yaml_block, body = match.group(1), match.group(2).strip()
    meta: dict = {}

    for line in yaml_block.splitlines():
        colon = line.find(":")
        if colon == -1:
            continue
        key = line[:colon].strip()
        raw = line[colon + 1 :].strip()

        if raw.startswith("[") and raw.endswith("]"):
            # Inline array: ["a", "b"] or ['a', 'b']
            meta[key] = json.loads(raw.replace("'", '"'))
        else:
            # Scalar: strip surrounding quotes
            meta[key] = raw.strip("'\"")

    return meta, body


def export_to_devto(filename: str, publish: bool, canonical: bool) -> dict:
    file_path = POSTS_DIR / filename
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    content = file_path.read_text(encoding="utf-8")
    meta, body = parse_frontmatter(content)

    api_key = os.environ.get("DEVTO_API_KEY")
    if not api_key:
        raise EnvironmentError(
            "DEVTO_API_KEY is not set.\n"
            "Get your key at: https://dev.to/settings/extensions (DEV API Keys section)"
        )

    slug = file_path.stem

    article: dict = {
        "title": meta["title"],
        "body_markdown": body,
        "published": publish,
        "tags": meta.get("tags", [])[:4],
    }
    if meta.get("description"):
        article["description"] = meta["description"]
    if canonical:
        article["canonical_url"] = f"{SITE_URL}/posts/{slug}"

    status_label = "" if publish else " (as draft)"
    print(f'Posting "{article["title"]}" to dev.to{status_label}...')

    payload = json.dumps({"article": article}).encode("utf-8")
    req = urllib.request.Request(
        DEVTO_API,
        data=payload,
        headers={
            "Content-Type": "application/json",
            "api-key": api_key,
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as exc:
        error_body = exc.read().decode("utf-8")
        raise RuntimeError(f"API error {exc.code}: {error_body}") from exc


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Export a markdown post to dev.to",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Example:\n"
            "  DEVTO_API_KEY=xxx python scripts/export_to_devto.py mutable-immutable.md"
            " --publish --canonical"
        ),
    )
    parser.add_argument("filename", help="Markdown filename inside src/content/posts/")
    parser.add_argument(
        "--publish",
        action="store_true",
        help="Publish immediately (default: save as draft)",
    )
    parser.add_argument(
        "--canonical",
        action="store_true",
        help=f"Set canonical_url pointing back to {SITE_URL}",
    )
    args = parser.parse_args()

    try:
        post = export_to_devto(args.filename, args.publish, args.canonical)
    except (FileNotFoundError, ValueError, EnvironmentError, RuntimeError) as exc:
        print(f"\nError: {exc}", file=sys.stderr)
        sys.exit(1)

    status = "Published" if post.get("published") else "Draft saved"
    print(f"\n{status}:")
    print(f"  Title : {post['title']}")
    print(f"  URL   : {post['url']}")
    print(f"  ID    : {post['id']}")


if __name__ == "__main__":
    main()
