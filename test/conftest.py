import pytest


@pytest.fixture(scope="function")
def opened_page(page):
    # some custom logic here (for example logging using get_user fixture)
    yield page
    page.close()


@pytest.fixture(scope="function", autouse=True)
def screenshot_handler(browser):
    context = browser.new_context(record_video_dir="./videos/")
    yield
    context.close()
