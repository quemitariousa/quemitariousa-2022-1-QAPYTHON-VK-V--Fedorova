import pytest
from base import BaseCase
from ui.locators import base_page_locators
from selenium.webdriver.support.ui import WebDriverWait



class Test(BaseCase):

    @pytest.mark.UI
    def test_login(self, auth):
        assert self.driver.current_url == "https://target.my.com/dashboard"

    @pytest.mark.UI
    def test_logout(self, auth):
        self.logout()
        assert self.driver.current_url == "https://target.my.com/"

    @pytest.mark.UI
    def test_edit(self, auth):
        name = self.randStr()
        phone = self.randStr()
        self.click(base_page_locators.PROFILE)
        WebDriverWait(self.driver, timeout=5).until(
            lambda d: self.driver.current_url == "https://target.my.com/profile/contacts")
        self.send_value(base_page_locators.PROFILE_NAME_INPUT, name)
        self.send_value(base_page_locators.PROFILE_PHONE_INPUT, phone)
        self.click(base_page_locators.PROFILE_SAVE)
        self.driver.refresh()
        assert name == self.wait_find(base_page_locators.PROFILE_NAME_INPUT).get_attribute("value")
        assert phone == self.wait_find(base_page_locators.PROFILE_PHONE_INPUT).get_attribute("value")

    @pytest.mark.UI
    @pytest.mark.parametrize("page_link_path,page_url", [(base_page_locators.AUDIENCE, "https://target.my.com"
                                                                                       "/segments/segments_list"),
                                                         (base_page_locators.PROFILE, "https://target.my.com/profile"
                                                                                      "/contacts")])
    def test_url_parametrize(self, auth, page_link_path, page_url):
        self.click(page_link_path)
        WebDriverWait(self.driver, timeout=5).until(lambda d: self.driver.current_url == page_url)
        assert page_url == self.driver.current_url
