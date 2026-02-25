from __future__ import annotations

from typing import Optional

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from .browser import chrome_driver


def scrape_tag_text(url: str, tag_name: str) -> Optional[str]:
    # Loads the site via selenium and scrapes the text of the first found html-tag.
    tag_name = tag_name.strip().lower()
    if not tag_name:
        return None

    with chrome_driver(headless=True) as driver:
        driver.get(url)

        try:
            el = driver.find_element(By.TAG_NAME, tag_name)
        except NoSuchElementException:
            return None

        if tag_name == "title":
            return driver.title.strip() or None

        text = (el.text or "").strip()
        return text or None