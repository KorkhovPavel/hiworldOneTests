from playwright.sync_api import expect
import requests
import re


def get_sitemap_links():
    """
    get links from sitemap
    :return: list links
    """
    sitemap = requests.get('https://hiworld.one/sitemap.xml')
    pattern = r'(?<=<loc>).{1,}(?=</loc>)'
    return re.findall(pattern, sitemap.text)


def test_pages_open(page):
    """
    Testing open pages.
    Links from sitemap.
    """
    for link in get_sitemap_links():
        page.goto(link)
        expect(page).to_have_url(link)


def test_search_post(page):
    """
    Testing search posts.
    On pages(links) from sitemap.
    """
    for link in get_sitemap_links():
        page.goto(link)
        page.get_by_placeholder("Enter value...").click()
        page.get_by_placeholder("Enter value...").fill("Sitemap")
        page.get_by_placeholder("Enter value...").press("Enter")
        expect(page.get_by_text("Python Flask Sitemap Example")).to_be_visible()


def get_title_page(link):
    """
    From link  - get title
    :param link: link page
    :return: title
    """

    title = link.split('/')[-1].replace('-', ' ')
    return title


def test_title_pages(page):
    """
    Testing title pages.
    On pages(links) from sitemap.
    """
    for link in get_sitemap_links():
        page.goto(link)
        title = get_title_page(link)
        if title == '':
            title = title.replace('', 'hiWorld.one')
        expect(page).to_have_title(title)


def test_link_logo(page):
    """
    Testing link transitions logo.
    On pages(links) from sitemap.
    """
    for link in get_sitemap_links():
        page.goto(link)
        page.locator(".logo").filter(has_text='.hiWorld').click()
        expect(page).to_have_url('https://hiworld.one/')


def test_page_404(page):
    """
    Check text 'Page not found' in page 404
    """
    page.goto('https://hiworld.one/njkhf834893')
    expect(page).to_have_url('https://hiworld.one/njkhf834893')
    loc404 = page.locator('.page_404')
    expect(loc404).to_have_text('Page not found')


def test_notification_cookie(page):
    """
    Check text on cookie-btn
    """
    page.goto('https://hiworld.one/')
    expect(page).to_have_url('https://hiworld.one/')
    loc404 = page.locator('.cookie-btn')
    expect(loc404).to_have_text('I agree')
