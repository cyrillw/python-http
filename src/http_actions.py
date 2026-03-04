from urllib.parse import urlencode
from typing import Dict

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, WebDriverException

from .browser import chrome_driver


def perform_get(url: str, params: Dict[str, str]) -> str:
    """
    Perform a GET request with optional query parameters.
    Returns the page body text.
    """
    try:
        query = urlencode(params)
        final_url = f"{url}?{query}" if query else url

        with chrome_driver(headless=True) as driver:
            driver.get(final_url)
            body = driver.find_element(By.TAG_NAME, "body")
            return body.text

    except NoSuchElementException:
        raise RuntimeError("Page loaded, but <body> element was not found.")
    except WebDriverException as e:
        raise RuntimeError(f"Failed to open URL '{url}'. ({e.__class__.__name__})")


def perform_post(url: str, data: Dict[str, str]) -> str:
    """
    Perform a POST-like action by submitting a form using Selenium.

    Notes:
    - This is not a raw HTTP POST (like requests.post).
    - It requires a page that contains a HTML <form> element.
    """
    try:
        with chrome_driver(headless=True) as driver:
            driver.get(url)

            # Ensure there is a form
            try:
                form = driver.find_element(By.CSS_SELECTOR, "form")
            except NoSuchElementException:
                raise RuntimeError(
                    "No <form> element found on the page. "
                    "POST in this project works via HTML form submission (Selenium)."
                )

            # Fill form fields
            missing_fields = []
            for key, value in data.items():
                try:
                    driver.find_element(By.NAME, key).send_keys(value)
                except NoSuchElementException:
                    missing_fields.append(key)

            if missing_fields:
                print(
                    "Warning: the following form fields were not found (skipped): "
                    + ", ".join(missing_fields)
                )

            # Submit form
            form.submit()

            body = driver.find_element(By.TAG_NAME, "body")
            return body.text

    except WebDriverException as e:
        raise RuntimeError(f"Failed to open URL '{url}' or submit form. ({e.__class__.__name__})")
    except NoSuchElementException:
        raise RuntimeError("Page loaded, but expected elements were not found.")