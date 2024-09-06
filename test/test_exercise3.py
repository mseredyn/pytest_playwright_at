import pytest

from helpers.url_helper import get_exercise_full_url_by_exercise_number
from pages.exercise3_page import Exercise3Page


class TestExercise3:

    @pytest.fixture(scope="function", autouse=True)
    def go_to(self, opened_page):
        opened_page.goto(get_exercise_full_url_by_exercise_number(3))

    def test_dropdown_list(self, opened_page):
        opened_page.goto(get_exercise_full_url_by_exercise_number(3))
        exercise_3_page = Exercise3Page(opened_page)

        exercise_3_page.select_option_in_s13("Verdoro Green")
        exercise_3_page.assert_trail_by_value("s13:v2")

        exercise_3_page.click_check_solution_button()
        exercise_3_page.assert_trail_by_value("OK. Good answer")
