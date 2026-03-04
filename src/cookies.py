from selenium.common.exceptions import WebDriverException

from .browser import chrome_driver


def list_cookies(url: str) -> str:
    """
    Retrieve all cookies stored for the current session.
    Returns a formatted string containing cookie information.
    """
    try:
        with chrome_driver(headless=True) as driver:
            driver.get(url)

            cookies = driver.get_cookies()

            if not cookies:
                return "No cookies found."

            lines = []

            for cookie in cookies:
                lines.append(f"Name: {cookie['name']}")
                lines.append(f"Value: {cookie['value']}")
                lines.append(f"Domain: {cookie['domain']}")
                lines.append("-" * 40)

            return "\n".join(lines)

    except WebDriverException as e:
        raise RuntimeError(f"Failed to access URL '{url}'. ({e.__class__.__name__})")