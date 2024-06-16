import pytest
from playwright.sync_api import sync_playwright
from logger import logger


pytest_logger = logger.Logger('test', level='DEBUG')


@pytest.fixture(params=['chrome', 'edge'], scope="function")
def browser(request):
    pytest_logger.info(f'Test "{request.node.name}" started for browser "{request.param}"')

    with sync_playwright() as playwright:
        if request.param == 'chrome':
            browser = playwright.chromium.launch(headless=False, args=["--start-maximized"])
        elif request.param == 'edge':
            browser = playwright.webkit.launch(headless=False, args=["--start-maximized"])
        else:
            raise NotImplementedError

        browser = browser.new_context(no_viewport=True)
        yield browser
        browser.close()
        pytest_logger.info(f'Test "{request.node.name}" completed.')
