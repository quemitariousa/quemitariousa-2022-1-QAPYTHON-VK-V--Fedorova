import os

import allure
from selenium.webdriver.common.by import By

from ui.locators.base_locators import CampaignPageLocators

from ui.pages.base_page import BasePage
from ui.pages.segments_page import SegmentPage

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os.path


def get_banner():
    banner_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    return os.path.join(banner_path, "images", "picture.png")


class CampaignPage(BasePage):
    locators = CampaignPageLocators
    url = 'https://target.my.com/dashboard'

    def go_to_segments_page(self):
        self.click(self.locators.AUDIENCE)
        time.sleep(1)
        return SegmentPage(self.driver)

    @allure.step('Creating campaign...')
    def create_campaign(self):
        name_campaign = self.randStr()
        self.click(self.locators.CREATE_NEW_СOMPAIGN)
        WebDriverWait(self.driver, timeout=5).until(EC.url_changes("https://target.my.com/dashboard"))
        self.click(self.locators.NEW_СOMPAIGN_TRAFFIC)
        self.send_value(self.locators.INPUT_URL, "https://www.python.org/")
        WebDriverWait(self.driver, timeout=6).until(
            EC.element_to_be_clickable(self.locators.INPUT_BUDGET_PER_DAY)
        )
        self.send_value(self.locators.NAME_СOMPAIGN, name_campaign)
        self.send_value(self.locators.INPUT_BUDGET_PER_DAY, "10000")
        self.send_value(self.locators.INPUT_BUDGET_ALL, "100500")

        self.click(self.locators.FORMAT_СOMPAIGN)
        self.send_file(self.locators.TEST_FILE_INPUT, get_banner())
        WebDriverWait(self.driver, timeout=6).until(
            EC.element_to_be_clickable(self.locators.SAVE_UPLOAD_PICTURE)
        )
        self.click(self.locators.SAVE_UPLOAD_PICTURE)
        self.click(self.locators.SAVE_СOMPAIGN)
        WebDriverWait(self.driver, timeout=10).until(
            lambda d: self.driver.current_url == "https://target.my.com/dashboard#")
        self.locators.MY_CAMPAIGN_NAME_IN_LIST = (By.XPATH, f"//*[contains(text(), '{name_campaign}')]")
