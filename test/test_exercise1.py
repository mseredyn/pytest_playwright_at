import pytest

from helpers.url_helper import get_exercise_full_url_by_exercise_number
from pages.exercise1_page import Exercise1Page


class TestExercise1:

    @pytest.fixture(scope="function", autouse=True)
    def go_to(self, opened_page):
        opened_page.goto(get_exercise_full_url_by_exercise_number(1))

    def test_three_buttons(self, opened_page):
        exercise_1_page = Exercise1Page(opened_page)

        exercise_1_page.click_b2_button()
        exercise_1_page.assert_trail_by_value("b2")
        exercise_1_page.click_b1_button()
        exercise_1_page.assert_trail_by_value("b2b1")
        exercise_1_page.click_b2_button()
        exercise_1_page.assert_trail_by_value("b2b1b2")

        exercise_1_page.click_check_solution_button()
        exercise_1_page.assert_trail_by_value("OK. Good answer")
