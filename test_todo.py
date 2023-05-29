from playwright.sync_api import expect


def test_home_page_open(page):
    page.goto('https://hiworld.one')
    expect(page).to_have_url("https://hiworld.one/")


