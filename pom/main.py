import time

from pom.home_page_elements import HomePage
from playwright.sync_api import Playwright, sync_playwright, expect


def about_us_section_verbiage(playwright: Playwright) -> None:
    # Assess - Given
    # page = login_set_up

    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    time.sleep(1)

    # assert not page.is_visible(HomePage.celebrating_beauty_header)
    # Click text=playwright-practice was founded by a group of like-minded fashion devotees, dete
    # assert page.is_visible(HomePage.celebrating_beauty_body)

    expect(HomePage.celebrating_beauty_body).to_be_visible()


# @pytest.mark.regression
# def test_about_us_section_verbiage_2(login_set_up) -> None:
#     # Assess - Given
#     page = login_set_up
#
#     assert page.is_visible(HomePage.celebrating_beauty_header)
#     # Click text=playwright-practice was founded by a group of like-minded fashion devotees, dete
#     assert page.is_visible(HomePage.celebrating_beauty_body)

with sync_playwright() as playwright:
    about_us_section_verbiage(playwright)
