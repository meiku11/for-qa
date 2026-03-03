import re
from playwright.sync_api import expect
from pages.home_page import HomePage


def test_homepage_opens_and_has_expected_url(page):
    home = HomePage(page)
    home.open_home()
    expect(page).to_have_url(re.compile(r"^https://selectel\.ru/?"))


def test_homepage_has_header(page):
    home = HomePage(page)
    home.open_home()
    home.accept_cookies_if_present()
    home.header_is_visible()
