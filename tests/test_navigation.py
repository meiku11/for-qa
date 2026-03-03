import re
import pytest
from playwright.sync_api import expect
from pages.home_page import HomePage


def test_can_open_control_panel_link_if_present(page):
    home = HomePage(page)
    home.open_home()
    home.accept_cookies_if_present()

    candidates = [
        page.get_by_role("link", name="Панель управления"),
        page.get_by_role("link", name="Войти"),
        page.get_by_role("link", name="Личный кабинет"),
    ]

    clicked = False
    for link in candidates:
        try:
            if link.is_visible(timeout=700):
                link.click()
                clicked = True
                break
        except Exception:
            continue

    if not clicked:
        pytest.skip("Не найдена ссылка на панель управления/вход (возможно, изменился UI)")

    expect(page).to_have_url(re.compile(r".*(my\.selectel\.ru|login).*"))