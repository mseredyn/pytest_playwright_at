import logging

from playwright.sync_api import Page, Locator, expect

LOGGER = logging.getLogger(__name__)


class BasePage:

    def __init__(self, page: Page):
        self.page = page

    def find_by(self, selector) -> Locator:
        element = self.page.locator(selector)
        return element

    def click_by(self, selector):
        self.find_by(selector).click()

    def fill_by(self, selector, value_to_fill):
        self.find_by(selector).fill(value_to_fill)

    def select_option_in_dropdown(self, selector, option_to_select):
        self.page.select_option(selector, label=option_to_select)

    def assert_text_by(self, selector, expected_value):
        expect(self.find_by(selector)).to_have_text(expected_value)
