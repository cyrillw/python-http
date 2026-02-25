import argparse
from .scraping import scrape_tag_text
from .http_actions import perform_get, perform_post
from .cookies import list_cookies


DEFAULT_URL = "https://httpbin.org"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="myproject.py",
        description="Python HTTP Project (Selenium)",
    )

    parser.add_argument(
        "command",
        help='Command: <html-tag> OR get OR post OR list-cookies',
    )

    # Optional URL argument
    parser.add_argument(
        "--url",
        default=DEFAULT_URL,
        help=f"Target URL (default: {DEFAULT_URL})",
    )

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    cmd = args.command.strip().lower()

    if cmd == "get":
        perform_get(args.url)

    elif cmd == "post":
        perform_post(args.url)

    elif cmd == "list-cookies":
        list_cookies(args.url)

    else:
        # default behavior = tag scraping
        text = scrape_tag_text(url=args.url, tag_name=cmd)

        if text is None:
            print(f"No content found for tag <{cmd}> on {args.url}")
            return 2

        print(text)

    return 0