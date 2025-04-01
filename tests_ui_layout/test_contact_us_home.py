import time
import pytest

from playwright.sync_api import Playwright, sync_playwright
from pom.contact_us_page import ContactUsPage


def test_submit_form(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    search_page = ContactUsPage(page)
    search_page.navigate()
    search_page.submit_form("Arun", "Teststreet 123", "test@gmail.com", "123-456-789", "test-subject", "test_message Blabla")


# with sync_playwright() as playwright:
#     test_submit_form(playwright)
#     time.sleep(5)
