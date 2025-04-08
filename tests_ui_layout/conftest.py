import os
import time
import pytest
from playwright.sync_api import Playwright, sync_playwright, expect

# pytest herkent automatisch de naam van de file conftest. Dus daarom hoef je niets te importeren
# hierin kan je fixtures definieren. Hiermee kan je code die je elke test gebruikt in neerzetten zodat je
# dat niet in elke test hoef te gebruiken maar kan aanroepen.


@pytest.fixture()
def set_up(page):

    # playwright has some ready made fixture for us to use. We dont need to create a browser and op the page.
    # so we dont need a part of the code anymore:
    """
    # test has its own page fixture so we dont need to start up the brow

    # slow-mo slows down the execution
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    # open new page
    page = context.new_page()
    # you can set the default time out for the whole test
    # This will now timeout after 10 seconds if not found
    # page.set_default_timeout(10000)
    # this steps pauses the code. Its possible to play your code step by step.
    # page.pause()
    """

    # playwright.chromium.launch(headless=False, slow_mo=500)
    # context = browser.new_context()
    # page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    time.sleep(3)

    # We zien dat we geen browser meer hebben dus we hebben geen slomo meer en ook geen headless browser.
    # Maar dat kan je wel via de terminal aanroepen

    # The yield keyword is used to return a list of values from a function.
    yield page
    page.close()

@pytest.fixture()
def login_set_up(set_up):
    # Assess - Given
    # browser = playwright.chromium.launch(headless=False)
    # context = browser.new_context()
    # # Open new page
    # page = context.new_page()

    page = set_up
    page.get_by_role("button", name="Log In").click()
    page.get_by_test_id("signUp.switchToSignUp").click()
    page.get_by_role("button", name="Log in with Email").click()
    page.get_by_test_id("emailAuth").get_by_role("textbox", name="Email").fill("symon.storozhenko@gmail.com")
    page.get_by_test_id("emailAuth").get_by_role("textbox", name="Email").press("Tab")
    # page.get_by_role("textbox", name="Password").fill("test123")
    page.fill("input[type='password']", os.environ["PASSWORD"])
    page.get_by_test_id("submit").get_by_test_id("buttonElement").click()

    # login_issue = True
    # while login_issue:
    #     if not page.is_visible("[data-testid=\"signUp.switchToSignUp\"]"):
    #         page.click("button:has-text(\"Log In\")")
    #     else:
    #         login_issue = False
    #     time.sleep(1)
    # # Click [data-testid="signUp.switchToSignUp"]
    # page.click("[data-testid=\"signUp.switchToSignUp\"]", timeout=2000)
    # # page.click(":nth-match(:text('Log In'), 2)", timeout=2000)
    # page.click("[data-testid='switchToEmailLink'] >> [data-testid='buttonElement']")
    # # page.click("[data-testid='siteMembers.container'] input[type='email']")
    # # page.fill("[data-testid='siteMembers.container'] input[type='email']", "symon.storozhenko@gmail.com")
    # page.fill('input:below(:text("Email"))', "symon.storozhenko@gmail.com")
    # page.press("[data-testid='siteMembers.container'] >> input[type='email']", "Tab")
    # page.fill("input[type='password']", PASSWORD)
    # page.click("[data-testid='submit'] >> [data-testid='buttonElement']")

    yield page


