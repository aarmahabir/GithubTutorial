import time

from pom.home_page_elements import HomePage
from playwright.sync_api import Playwright, sync_playwright


def test_about_us_section_verbiage(login_set_up) -> None:
    # Assess - Given
    # page = login_set_up

    page = login_set_up

    # browser = playwright.chromium.launch(headless=False, slow_mo=500)
    # context = browser.new_context()
    # page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    # page.get_by_role("link", name="Home").click()

    assert page.is_visible(HomePage.celebrating_beauty_header)
    # Click text=playwright-practice was founded by a group of like-minded fashion devotees
    assert page.is_visible(HomePage.celebrating_beauty_body)


# @pytest.mark.regression
# def test_about_us_section_verbiage_2(login_set_up) -> None:
#     # Assess - Given
#     page = login_set_up
#
#     assert page.is_visible(HomePage.celebrating_beauty_header)
#     # Click text=playwright-practice was founded by a group of like-minded fashion devotees, dete
#     assert page.is_visible(HomePage.celebrating_beauty_body)

# with sync_playwright() as playwright:
#     about_us_section_verbiage(playwright)
