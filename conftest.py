import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture
def browser_fixture():
    """
    open and close new windows browser
    """
    with sync_playwright() as playwright:
        # open new window browser
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        # close window browser
        page.close()
        browser.close()
