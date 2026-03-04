from __future__ import annotations

import argparse

from .cookies import list_cookies
from .http_actions import perform_get, perform_post
from .scraping import scrape_tag_text
from .screenshot import take_screenshot

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

    parser.add_argument(
        "command",
        help="Command: <html-tag> OR get OR post OR list-cookies OR screenshot",
    )
    parser.add_argument(
        "--url",
        default=DEFAULT_URL,
        help=f"Target URL (default: {DEFAULT_URL})",
    )

    parser.add_argument(
        "--param",
        action="append",
        help="GET parameter in form key=value (can be used multiple times)",
    )
    parser.add_argument(
        "--data",
        action="append",
        help="POST form data in form key=value (can be used multiple times)",
    )

    parser.add_argument(
        "--output",
        help="Write response output to a file instead of printing to console",
    )

    parser.add_argument(
        "--screenshot",
        default="screenshot.png",
        help="Screenshot file path for the 'screenshot' command (default: screenshot.png)",
    )

    return parser


def handle_output(text: str, output_file: str | None) -> None:
    """
    Either print the response to stdout or write it to a file.
    """
    if output_file:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"Response written to {output_file}")
    else:
        print(text)


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

    try:
        if cmd == "get":
            text = perform_get(args.url, get_params)
            handle_output(text, args.output)
            return 0

        if cmd == "post":
            text = perform_post(args.url, post_data)
            handle_output(text, args.output)
            return 0

        if cmd == "list-cookies":
            text = list_cookies(args.url)
            handle_output(text, args.output)
            return 0

        if cmd == "screenshot":
            text = take_screenshot(args.url, args.screenshot)
            handle_output(text, args.output)
            return 0

        # Default: treat the command as an HTML tag name to scrape
        text = scrape_tag_text(url=args.url, tag_name=cmd)
        if text is None:
            print(f"No content found for tag <{cmd}> on {args.url}")
            return 3

        handle_output(text, args.output)
        return 0

    except RuntimeError as e:
        # Friendly error handling (no stacktrace)
        print(f"Error: {e}")
        return 1