from __future__ import annotations

from contextlib import contextmanager
from typing import Iterator

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions


@contextmanager
def chrome_driver(headless: bool = True) -> Iterator[webdriver.Chrome]:
    options = ChromeOptions()
    if headless:
        options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    try:
        yield driver
    finally:
        driver.quit()
