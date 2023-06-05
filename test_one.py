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
    title_replace = {'Postgresql': 'PostgreSQL', 'Github': 'GitHub'}
    title = link.split('/')[-1].replace('-', ' ').title()
    for k, i in title_replace.items():
        if k in title:
            title = title.replace(k, i)
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
