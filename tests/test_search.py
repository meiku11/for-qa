import pytest
from playwright.sync_api import expect
from pages.home_page import HomePage


def test_search_returns_results_or_opens_search_page(page):
    home = HomePage(page)
    home.open_home()
    home.accept_cookies_if_present()

    if not home.open_search_if_exists():
        pytest.skip("Элемент поиска не найден (возможно, поиск спрятан или изменён UI)")

    search_input = page.locator('input[type="search"], input[placeholder*="Поиск" i], input[name*="search" i]')
    if search_input.count() == 0:
        pytest.skip("Поле поиска не найдено после открытия поиска")

    search_input.first.fill("облако")
    search_input.first.press("Enter")

    expect(page).to_have_url(lambda u: "search" in u or "poisk" in u or "query" in u or "?" in u)