import os

import appium.webdriver.extensions.remote_fs
import pytest
from appium import webdriver
from appium.options.windows import WindowsOptions


@pytest.fixture
def app_setup_teardown():
    winoptions = WindowsOptions()

    winoptions.app = "Microsoft.WindowsCalculator_8wekyb3d8bbwe!App"
    appium_session = webdriver.Remote(f"http://127.0.0.1:4723", options=winoptions)
    yield appium_session
    appium_session.quit()


def test_calculate_test(app_setup_teardown):
    assert True
