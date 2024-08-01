""" Fixtures and UI tests"""
import time

import pytest
import selenium.webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from assertpy import assert_that


@pytest.fixture
def browser_setup_teardown():
    brs = selenium.webdriver.Chrome()
    brs.implicitly_wait(15)
    yield brs
    brs.implicitly_wait(15)
    brs.quit()


def test_browser_button_test(browser_setup_teardown):
    url_string = 'https://www.saucedemo.com/'
    svar = "test string"
    browser_setup_teardown.get(url_string)
    try:
        time.sleep(2)
        browser_setup_teardown.find_element(By.ID, 'user-name').send_keys("hello")
        assert browser_setup_teardown.find_element(By.ID, 'login-button').is_enabled()
        browser_setup_teardown.find_element(By.ID, 'login-button').click()
        time.sleep(2)
    except NoSuchElementException:
        print("element not found")


def test_browser_title_test(browser_setup_teardown):
    url_string = 'https://www.saucedemo.com/'
    svar = "test string"
    browser_setup_teardown.get(url_string)
    cookie_list = browser_setup_teardown.get_cookies()
    for cookie in cookie_list:
        print("cookie", cookie)
        time.sleep(2)

    assert_that(browser_setup_teardown.title).contains('Labs')
