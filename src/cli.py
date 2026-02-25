import argparse
from .scraping import scrape_tag_text


DEFAULT_URL = "https://the-internet.herokuapp.com"


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="myproject.py",
        description="Python HTTP Project (Selenium)",
    )

    # Allows usage like: python myproject.py title
    p.add_argument(
        "command_or_tag",
        help='Either an HTML tag name (e.g. "title") OR later a command such as get/post/list-cookies',
    )

    # Optional URL argument
    p.add_argument(
        "--url",
        default=DEFAULT_URL,
        help=f"Target URL (default: {DEFAULT_URL})",
    )

    return p


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    cmd = args.command_or_tag.strip().lower()

    # Minimal system feature:
    # Display the content of a specific HTML tag
    # (Later this can be extended with commands like get, post, list-cookies, etc.)
    text = scrape_tag_text(url=args.url, tag_name=cmd)

    if text is None:
        print(f"No content found for tag <{cmd}> on {args.url}")
        return 2

    print(text)
    return 0