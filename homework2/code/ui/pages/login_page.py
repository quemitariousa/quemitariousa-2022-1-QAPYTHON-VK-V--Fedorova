import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from ui.locators.base_locators import LoginPageLocators
from ui.pages.base_page import BasePage
from ui.pages.company_page import CompanyPage
from files import userdata


class LoginPage(BasePage):
    locators = LoginPageLocators()
    url = 'https://target.my.com/'
    LOGIN = userdata.login
    PASSWORD = userdata.password

    @allure.step("Log in...")
    def auth(self):
        self.click(self.locators.PROFILE_LOGIN)
        self.send_value(self.locators.EMAIL_INPUT, userdata.login)
        self.send_value(self.locators.PASSWORD_INPUT, userdata.password)
        self.click(self.locators.LOGIN_BUTTON)
        WebDriverWait(self.driver, timeout=2).until(EC.url_changes("https://target.my.com"))
        return CompanyPage(self.driver)

    @allure.step("Try to negative log in...")
    def negative_auth(self, login, password):
        self.click(self.locators.PROFILE_LOGIN)
        email_input = self.find(self.locators.EMAIL_INPUT)
        password_input = self.find(self.locators.PASSWORD_INPUT)
        email_input.send_keys(login)
        password_input.send_keys(password)
        self.click(self.locators.LOGIN_BUTTON)

    def logout(self):
        current_url = self.driver.current_url
        time.sleep(1)
        self.click(self.locators.LOGIN_OUT)
        self.click(self.locators.PROFILE_LOGIN_LOGOUT)
        time.sleep(4)
        WebDriverWait(self.driver, timeout=2).until(EC.url_changes(current_url))
