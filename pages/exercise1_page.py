from pages.common_page import CommonPage


class Exercise1Page(CommonPage):
    B1_BUTTON = "#btnButton1"
    B2_BUTTON = "#btnButton2"

    def __init__(self, page):
        super().__init__(page)

    def click_b1_button(self):
        self.click_by(self.B1_BUTTON)

    def click_b2_button(self):
        self.click_by(self.B2_BUTTON)
