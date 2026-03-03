from playwright.sync_api import expect
from .base_page import BasePage


class HomePage(BasePage):
    URL = "https://selectel.ru/"

    def open_home(self):
        self.open(self.URL)

    def accept_cookies_if_present(self):
        candidates = [
            self.page.get_by_role("button", name="Принять"),
            self.page.get_by_role("button", name="Согласен"),
            self.page.get_by_role("button", name="Accept"),
        ]
        for btn in candidates:
            try:
                if btn.is_visible(timeout=500):
                    btn.click()
                    break
            except Exception:
                continue

    def header_is_visible(self):
        header = self.page.locator("header")
        expect(header).to_be_visible()

    def open_search_if_exists(self) -> bool:
        search_btn = self.page.locator('[aria-label*="Поиск" i], [aria-label*="search" i]')
        try:
            if search_btn.count() > 0 and search_btn.first.is_visible(timeout=500):
                search_btn.first.click()
                return True
        except Exception:
            pass
        return False