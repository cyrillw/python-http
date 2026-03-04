from urllib.parse import urlencode
from typing import Dict

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, WebDriverException

from .browser import chrome_driver


def perform_get(url: str, params: Dict[str, str]) -> int:
    """
    Perform a GET request with optional query parameters.
    Returns a process-like exit code (0 = success, non-zero = error).
    """
    try:
        query = urlencode(params)
        final_url = f"{url}?{query}" if query else url

        with chrome_driver(headless=True) as driver:
            driver.get(final_url)
            body = driver.find_element(By.TAG_NAME, "body")
            print(body.text)
        return 0

    except NoSuchElementException:
        print("Error: page loaded, but <body> element was not found.")
        return 11
    except WebDriverException as e:
        print(f"Error: failed to open URL '{url}'. Details: {e.__class__.__name__}")
        return 10


def perform_post(url: str, data: Dict[str, str]) -> int:
    """
    Perform a POST-like action by submitting a form using Selenium.

    Notes:
    - This is not a raw HTTP POST (like requests.post).
    - It requires a page that contains a HTML <form> element.
    """
    try:
        with chrome_driver(headless=True) as driver:
            driver.get(url)

            # 1) Ensure there is a form
            try:
                form = driver.find_element(By.CSS_SELECTOR, "form")
            except NoSuchElementException:
                print(
                    "Error: no <form> element found on the page. "
                    "POST in this project works via HTML form submission (Selenium)."
                )
                return 20

            # 2) Try to fill fields
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

            # 3) Submit the form
            form.submit()

            body = driver.find_element(By.TAG_NAME, "body")
            print(body.text)
            return 0

    except WebDriverException as e:
        print(f"Error: failed to open URL '{url}' or submit the form. Details: {e.__class__.__name__}")
        return 21
    except NoSuchElementException:
        print("Error: page loaded, but expected elements were not found.")
        return 22