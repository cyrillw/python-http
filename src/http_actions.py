from selenium.webdriver.common.by import By
from .browser import chrome_driver


def perform_get(base_url: str) -> None:
    """
    Perform a GET request with query parameters using Selenium.
    Example: https://httpbin.org/get?name=John&role=Student
    """
    url = f"{base_url}/get?name=John&role=Student"

    with chrome_driver(headless=True) as driver:
        driver.get(url)

        body = driver.find_element(By.TAG_NAME, "body")
        print(body.text)

def perform_post(base_url: str) -> None:
    """
    Perform a POST request using a simple HTML form submission.
    """
    url = f"{base_url}/forms/post"

    with chrome_driver(headless=True) as driver:
        driver.get(url)

        # Fill form fields
        driver.find_element(By.NAME, "custname").send_keys("John Doe")
        driver.find_element(By.NAME, "custtel").send_keys("123456")
        driver.find_element(By.NAME, "custemail").send_keys("john@example.com")

        # Submit form
        driver.find_element(By.CSS_SELECTOR, "form").submit()

        body = driver.find_element(By.TAG_NAME, "body")
        print(body.text)