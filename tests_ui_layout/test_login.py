import time

from playwright.sync_api import Playwright, sync_playwright, expect


def test_login(login_set_up) -> None:
    # we dont need this code any more:
    """
    # slow-mo slows down the execution
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()
    # you can set the default time out for the whole test
    # This will now timeout after 10 seconds if not found
    # page.set_default_timeout(10000)
    # this steps pauses the code. Its possible to play your code step by step.
    # page.pause()

    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    time.sleep(1)
    """

    # login_issue = True
    # while login_issue:
    #     if not page.is_visible("[data-testid=\"sign.Up.switchToSignUp\"]"):
    #         # time.sleep(1)
    #         page.get_by_role("button", name="Log In").click()
    #     else:
    #         login_issue = False
    # time.sleep(1)
    # print(login_issue)

    page = login_set_up
    page.click("[aria-label='symon.storozhenko account menu']")
    assert page.is_visible("text=My Orders")
