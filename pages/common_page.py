from pages.base_page import BasePage


class CommonPage(BasePage):
    CHECK_SOLUTION_BUTTON = "#solution"
    TRAIL = "#trail .wrap"

    def __init__(self, page):
        super().__init__(page)

    def click_check_solution_button(self):
        self.click_by(self.CHECK_SOLUTION_BUTTON)

    def assert_trail_by_value(self, value):
        self.assert_text_by(self.TRAIL, value)
