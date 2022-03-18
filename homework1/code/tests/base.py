import pytest
from homework1.code.ui.locators import base_page_locators
from selenium.common.exceptions import StaleElementReferenceException, ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from files import userdata

import random
import string


CLICK_RETRY = 3


class BaseCase:

    driver = None
    config = None

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config):
        self.driver = driver
        self.config = config

    @pytest.fixture(scope='function', autouse=True)
    def auth(self, setup):
        login = userdata.login
        password = userdata.password
        self.click(base_page_locators.PROFILE_LOGIN)
        email_input = self.find(base_page_locators.EMAIL_INPUT)
        password_input = self.find(base_page_locators.PASSWORD_INPUT)
        email_input.clear()
        email_input.send_keys(login)
        password_input.clear()
        password_input.send_keys(password)
        self.click(base_page_locators.LOGIN_BUTTON)
        WebDriverWait(self.driver, timeout=2).until(EC.url_changes("https://target.my.com"))
        assert self.driver.current_url == "https://target.my.com/dashboard"
        return self.driver.current_url

    def find(self, locator):
        return self.driver.find_element(*locator)

    def wait_find(self, locator):
        WebDriverWait(self.driver, timeout=5).until(
            lambda d: self.find(locator))
        return self.find(locator)

    def click(self, locator):
        self.wait_find(locator)
        for i in range(CLICK_RETRY):
            try:
                self.find(locator).click()
                break
            except StaleElementReferenceException:
                pass
            except ElementClickInterceptedException:
                pass

    def send_value(self, locator, value):
        input_element = self.wait_find(locator)
        input_element.clear()
        input_element.send_keys(value)

    def logout(self):
        current_url = self.driver.current_url
        time.sleep(1)
        self.click(base_page_locators.LOGIN_OUT)
        self.click(base_page_locators.PROFILE_LOGIN_LOGOUT)
        WebDriverWait(self.driver, timeout=2).until(EC.url_changes(current_url))

    def randStr(self, chars=string.ascii_uppercase + string.digits, N=10):
        return ''.join(random.choice(chars) for _ in range(N))

