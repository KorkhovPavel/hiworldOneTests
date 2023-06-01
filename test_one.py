from time import sleep

from playwright.sync_api import expect
import requests
import re


def test_pages_open(page):
    """
    testing open pages
    links from sitemap
    """
    item = requests.get('https://hiworld.one/sitemap.xml')
    pattern = r'(?<=<loc>).{1,}(?=</loc>)'
    links = re.findall(pattern, item.text)
    for link in links:
        page.goto(link)
        expect(page).to_have_url(link)




