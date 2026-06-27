#!/usr/bin/env python3
"""
Tweet a post title and link to X (Twitter)

Usage:
    python scripts/tweet_post.py <filename>

Environment:
    TWITTER_API_KEY              Your app's API key
    TWITTER_API_KEY_SECRET       Your app's API key secret
    TWITTER_ACCESS_TOKEN         Your account's access token
    TWITTER_ACCESS_TOKEN_SECRET  Your account's access token secret

Get credentials at: https://developer.x.com → your app → Keys and Tokens

Example:
    python scripts/tweet_post.py python-inside/en/x-equal-ten.md
"""

import os
import re
import sys
import argparse
from pathlib import Path

try:
    import tweepy
except ImportError:
    print("tweepy is required: pip install tweepy", file=sys.stderr)
    sys.exit(1)

POSTS_DIR = Path(__file__).parent.parent / "src" / "content" / "posts"
SITE_URL = "https://blog.storv.us"


def parse_title(content: str) -> str:
    match = re.match(r"^---\n(.*?)\n---\n", content, re.DOTALL)
    if not match:
        raise ValueError("No YAML frontmatter found in file")
    for line in match.group(1).splitlines():
        colon = line.find(":")
        if colon == -1:
            continue
        if line[:colon].strip() == "title":
            return line[colon + 1:].strip().strip("'\"")
    raise ValueError("No 'title' found in frontmatter")


def build_url(file_path: Path) -> str:
    # Expected structure: <category>/<lang>/<slug>.md
    parts = file_path.relative_to(POSTS_DIR).parts
    if len(parts) != 3:
        raise ValueError(
            f"Unexpected path structure: {file_path}\n"
            "Expected: <category>/<lang>/<slug>.md  (e.g. python-inside/en/x-equal-ten.md)"
        )
    cat, lang, filename = parts
    slug = Path(filename).stem
    if lang == "en":
        return f"{SITE_URL}/en/posts/{cat}/{slug}/"
    return f"{SITE_URL}/posts/{cat}/{slug}/"


def tweet_post(filename: str) -> dict:
    file_path = POSTS_DIR / filename
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    content = file_path.read_text(encoding="utf-8")
    title = parse_title(content)
    url = build_url(file_path)

    required = (
        "TWITTER_API_KEY",
        "TWITTER_API_KEY_SECRET",
        "TWITTER_ACCESS_TOKEN",
        "TWITTER_ACCESS_TOKEN_SECRET",
    )
    missing = [v for v in required if not os.environ.get(v)]
    if missing:
        raise EnvironmentError(
            f"Missing environment variables: {', '.join(missing)}\n"
            "Get credentials at: https://developer.x.com → your app → Keys and Tokens"
        )

    client = tweepy.Client(
        consumer_key=os.environ["TWITTER_API_KEY"],
        consumer_secret=os.environ["TWITTER_API_KEY_SECRET"],
        access_token=os.environ["TWITTER_ACCESS_TOKEN"],
        access_token_secret=os.environ["TWITTER_ACCESS_TOKEN_SECRET"],
    )

    text = f"{title}\n{url}"
    print(f'Tweeting "{title}"...')
    response = client.create_tweet(text=text)
    return response.data


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Tweet a post title and link to X (Twitter)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Example:\n"
            "  python scripts/tweet_post.py python-inside/en/x-equal-ten.md"
        ),
    )
    parser.add_argument("filename", help="Markdown file path inside src/content/posts/")
    args = parser.parse_args()

    try:
        data = tweet_post(args.filename)
    except (FileNotFoundError, ValueError, EnvironmentError) as exc:
        print(f"\nError: {exc}", file=sys.stderr)
        sys.exit(1)

    tweet_id = data["id"]
    print(f"\nTweeted:")
    print(f"  ID  : {tweet_id}")
    print(f"  URL : https://x.com/i/web/status/{tweet_id}")


if __name__ == "__main__":
    main()
