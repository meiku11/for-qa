from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def open(self, url: str):
        self.page.goto(url, wait_until="domcontentloaded")

    def assert_title_contains(self, text: str):
        expect(self.page).to_have_title(lambda t: text.lower() in t.lower())

    def assert_url_contains(self, part: str):
        expect(self.page).to_have_url(lambda u: part in u)