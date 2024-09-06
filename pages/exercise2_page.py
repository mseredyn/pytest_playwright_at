from pages.common_page import CommonPage


class Exercise2Page(CommonPage):
    T14_INPUT_AREA = "#t14"
    B1_BUTTON = "#btnButton1"

    def __init__(self, driver):
        super().__init__(driver)

    def fill_t14_input_with_value(self, value):
        self.fill_by(self.T14_INPUT_AREA, value)

    def click_b1_button(self):
        self.click_by(self.B1_BUTTON)
