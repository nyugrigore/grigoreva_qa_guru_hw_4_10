from selene import browser
import pytest


@pytest.fixture(scope='session')
def browser_configs():
    browser.config.window_width = 800
    browser.config.window_height = 900
