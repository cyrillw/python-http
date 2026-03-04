from __future__ import annotations

import argparse
from .scraping import scrape_tag_text
from .http_actions import perform_get, perform_post
from .cookies import list_cookies

DEFAULT_URL = "https://httpbin.org"


def parse_key_values(items):
    """
    Convert ["a=1","b=2"] into {"a":"1","b":"2"}.
    """
    result = {}
    if not items:
        return result

    for item in items:
        if "=" not in item:
            raise ValueError(f"Invalid format: {item}. Use key=value")
        key, value = item.split("=", 1)
        result[key] = value

    return result


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="myproject.py",
        description="Python HTTP Project (Selenium) – Minimal System",
    )

    parser.add_argument("command", help="Command: <html-tag> OR get OR post OR list-cookies")
    parser.add_argument("--url", default=DEFAULT_URL, help=f"Target URL (default: {DEFAULT_URL})")

    parser.add_argument("--param", action="append", help="GET parameter in form key=value (can be used multiple times)")
    parser.add_argument("--data", action="append", help="POST form data in form key=value (can be used multiple times)")

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    cmd = args.command.strip().lower()

    try:
        get_params = parse_key_values(args.param)
        post_data = parse_key_values(args.data)
    except ValueError as e:
        print(f"Error: {e}")
        return 2

    if cmd == "get":
        return perform_get(args.url, get_params)

    if cmd == "post":
        return perform_post(args.url, post_data)

    if cmd == "list-cookies":
        list_cookies(args.url)
        return 0

    text = scrape_tag_text(url=args.url, tag_name=cmd)
    if text is None:
        print(f"No content found for tag <{cmd}> on {args.url}")
        return 3

    print(text)
    return 0