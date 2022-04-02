import string
import time

import allure

from files import userdata
from ui.locators.base_locators import BasePageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException, ElementClickInterceptedException, \
    ElementNotInteractableException
import random


class PageNotOpenedException(Exception):
    pass


CLICK_RETRY = 5


class BasePage(object):
    locators = BasePageLocators
    url = 'https://target.my.com/'

    def __init__(self, driver):
        self.driver = driver

    def is_opened(self, timeout=15):
        started = time.time()
        while time.time() - started < timeout:
            if self.driver.current_url == self.url:
                return True
        raise PageNotOpenedException(f'{self.url} did not open in {timeout} sec, current url {self.driver.current_url}')

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.driver, timeout=timeout)

    @allure.step('Looking for an element...')
    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    @allure.step('Click on an element...')
    def click(self, locator, timeout=5) -> WebElement:
        self.find(locator, timeout=timeout)
        elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
        elem.click()

    @allure.step('Sending value...')
    def send_value(self, locator, value):
        input_element = self.wait_find(locator)
        input_element.clear()
        input_element.send_keys(value)

    def wait_find(self, locator):
        WebDriverWait(self.driver, timeout=5).until(
            lambda d: self.find(locator))
        return self.find(locator)

    def randStr(self, chars=string.ascii_uppercase + string.digits, N=10):
        return ''.join(random.choice(chars) for _ in range(N))

    @allure.step("Send file...")
    def send_file(self, locator, file):
        input_element = self.wait_find(locator)
        for i in range(CLICK_RETRY):
            try:
                input_element.send_keys(file)
            except ElementNotInteractableException:
                pass

    @allure.step("Log in...")
    def auth(self):
        self.click(self.locators.PROFILE_LOGIN)
        self.send_value(self.locators.EMAIL_INPUT, userdata.login)
        self.send_value(self.locators.PASSWORD_INPUT, userdata.password)
        self.click(self.locators.LOGIN_BUTTON)
        WebDriverWait(self.driver, timeout=2).until(EC.url_changes("https://target.my.com"))
        return self.driver
