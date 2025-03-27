import re
import time
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    # slow-mo slows down the execution
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()
    # you can set the default time out for the whole test
    # This will now timeout after 10 seconds if not found
    # page.set_default_timeout(10000)
    # this steps pauses the code. Its possible to play your code step by step.
    # page.pause()

    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    # time.sleep(1)
    page.get_by_role("button", name="Log In").click()

    # login_issue = True
    # while login_issue:
    #     if not page.is_visible("[data-testid=\"sign.Up.switchToSignUp\"]"):
    #         # time.sleep(1)
    #         page.get_by_role("button", name="Log In").click()
    #     else:
    #         login_issue = False
    # time.sleep(1)
    # print(login_issue)

    page.get_by_test_id("signUp.switchToSignUp").click()
    page.get_by_role("button", name="Log in with Email").click()
    page.get_by_test_id("emailAuth").get_by_role("textbox", name="Email").fill("symon.storozhenko@gmail.com")
    page.get_by_test_id("emailAuth").get_by_role("textbox", name="Email").press("Tab")
    page.get_by_role("textbox", name="Password").fill("test123")
    page.get_by_test_id("submit").get_by_test_id("buttonElement").click()
    test_1 = expect(page.get_by_role("button", name="Log In")).to_be_hidden

    # find element by index
    # as you can see on the page we have two links and the start with the same two words. So
    # we need to distinguish them.
    # There are multipple ways to do that:
    #   1.  exact is True: This will find the exact link.
    #       page.get_by_role("link", name="Shop Women", exact=True).click()
    #   2.  by index number of the found elements.
    #       page.get_by_role("link", name="Shop Women Winter").nth(0)

    page.get_by_role("link", name="Shop Women", exact=True).click()
    # page.get_by_role("link", name="Shop Women Winter").nth(1)

    # get text by xpath
    if page.locator("xpath=//*[contains(@class, 'd7xFyJ sJ6BuOp')]"):
        print("its found")

    # easy way to find the parent
    product = page.get_by_text('$85').first.locator('xpath=../../../../..')

    if product:
        print("its found_2")

    all_links = page.get_by_role("link").all()
    for link in all_links:
        if "$85" in link.text_content() == "$85":
            assert "socks" not in link.text_content()

    # Locators
    # old: page.action(selector)
    # new: page.locator(selector).action()

    check_error_btn = page.locator("text=Errors")
    print(check_error_btn)
    if check_error_btn:
        print("element found")
    else:
        print("element not found")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
