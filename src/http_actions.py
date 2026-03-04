from urllib.parse import urlencode
from selenium.webdriver.common.by import By
from .browser import chrome_driver


def perform_get(url: str, params: dict) -> None:
    """
    Perform a GET request with query parameters.
    """

    query = urlencode(params)
    final_url = f"{url}?{query}" if query else url

    with chrome_driver(headless=True) as driver:
        driver.get(final_url)

        body = driver.find_element(By.TAG_NAME, "body")
        print(body.text)

def perform_post(url: str, data: dict) -> None:
    """
    Submit a form on the given page.
    """

    with chrome_driver(headless=True) as driver:
        driver.get(url)

        for key, value in data.items():
            driver.find_element(By.NAME, key).send_keys(value)

        driver.find_element(By.CSS_SELECTOR, "form").submit()

        body = driver.find_element(By.TAG_NAME, "body")
        print(body.text)