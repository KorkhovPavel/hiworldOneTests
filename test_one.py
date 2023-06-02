import time
from time import sleep

from playwright.sync_api import expect
import requests
import re


def test_pages_open(page):
    """
    Testing open pages.
    Links from sitemap.
    """
    item = requests.get('https://hiworld.one/sitemap.xml')
    pattern = r'(?<=<loc>).{1,}(?=</loc>)'
    links = re.findall(pattern, item.text)
    for link in links:
        page.goto(link)
        expect(page).to_have_url(link)


def test_search_post(page):
    """
    Testing search posts.
    On pages(links) from sitemap.
    """
    item = requests.get('https://hiworld.one/sitemap.xml')
    pattern = r'(?<=<loc>).{1,}(?=</loc>)'
    links = re.findall(pattern, item.text)
    for link in links:
        page.goto(link)
        page.get_by_placeholder("Enter value...").click()
        page.get_by_placeholder("Enter value...").fill("Sitemap")
        page.get_by_placeholder("Enter value...").press("Enter")
        expect(page.get_by_text("Python Flask Sitemap Example")).to_be_visible()

