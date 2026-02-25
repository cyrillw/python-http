from .browser import chrome_driver


def list_cookies(url: str) -> None:
    """
    Display all cookies stored for the current session.
    """
    with chrome_driver(headless=True) as driver:
        driver.get(url)

        cookies = driver.get_cookies()

        if not cookies:
            print("No cookies found.")
            return

        for cookie in cookies:
            print(f"Name: {cookie['name']}")
            print(f"Value: {cookie['value']}")
            print(f"Domain: {cookie['domain']}")
            print("-" * 40)