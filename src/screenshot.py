from __future__ import annotations

from selenium.common.exceptions import WebDriverException

from .browser import chrome_driver


def take_screenshot(url: str, screenshot_file: str) -> str:
    """
    Open the given URL and save a screenshot to the given file path.
    Returns a human-readable status message.
    """
    try:
        with chrome_driver(headless=True) as driver:
            driver.get(url)

            ok = driver.save_screenshot(screenshot_file)
            if not ok:
                raise RuntimeError("save_screenshot() returned False.")

        return f"Screenshot saved to {screenshot_file}"

    except WebDriverException as e:
        raise RuntimeError(f"Failed to access URL '{url}' or take screenshot. ({e.__class__.__name__})")