import pytest

from helpers.url_helper import get_exercise_full_url_by_exercise_number
from pages.exercise2_page import Exercise2Page


class TestExercise2:

    @pytest.fixture(scope="function", autouse=True)
    def go_to(self, opened_page):
        opened_page.goto(get_exercise_full_url_by_exercise_number(2))

    def test_editbox(self, opened_page):
        exercise_2_page = Exercise2Page(opened_page)

        exercise_2_page.fill_t14_input_with_value("Western perhaps.")
        exercise_2_page.click_b1_button()
        exercise_2_page.assert_trail_by_value("t14:Western perhaps.b1")

        exercise_2_page.click_check_solution_button()
        exercise_2_page.assert_trail_by_value("OK. Good answer")
