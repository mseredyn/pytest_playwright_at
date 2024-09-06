from pages.common_page import CommonPage


class Exercise3Page(CommonPage):
    DROP_DOWN = "#s13"

    def __init__(self, driver):
        super().__init__(driver)

    def select_option_in_s13(self, option_to_select):
        self.select_option_in_dropdown(self.DROP_DOWN, option_to_select)


