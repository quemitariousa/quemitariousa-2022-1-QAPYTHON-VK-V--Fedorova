import allure

from ui.locators.base_locators import SegmentPageLocators
from ui.pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from ui.locators.base_locators import By


class SegmentPage(BasePage):
    locators = SegmentPageLocators
    url = 'https://target.my.com/segments/segments_list'

    @allure.step("Create segment...")
    def create_segment(self):
        name_segment = self.randStr()
        self.click(self.locators.CREATE_SECOND_SEGMENT)
        WebDriverWait(self.driver, timeout=2).until(EC.url_changes("https://target.my.com/dashboard"))
        self.click(self.locators.APPS_AND_GAMES_SEGMENT)
        self.click(self.locators.PLAYED_AND_PAYED_BUTTON)
        self.click(self.locators.SAVE_NEW_SEGMENT)
        self.send_value(self.locators.INPUT_NAME_SEGMENT, name_segment)
        self.click(self.locators.SUBMIT_SEGMENT)
        WebDriverWait(self.driver, timeout=3).until(
            lambda d: self.driver.current_url == "https://target.my.com/segments/segments_list")
        time.sleep(2)
        self.locators.MY_SEGMENT_NAME_IN_LIST = (
            By.XPATH, f"//div//a[@title='{name_segment}']")
        return name_segment

    @allure.step("Delete segment...")
    def delete_segment(self):
        name_segment = self.create_segment()
        search_of_segments = self.find(self.locators.SEARCH_OF_SEGMENTS)
        self.send_value(self.locators.SEARCH_OF_SEGMENTS, name_segment)
        self.locators.ELEMENT_OF_SEARCH_SEGMENTS = (
            By.XPATH, f"//li[@title='{name_segment}']"
        )
        self.click(self.locators.ELEMENT_OF_SEARCH_SEGMENTS)
        self.click(self.locators.CHECKBOX_ALL_DELETE)
        self.click(self.locators.ACTION_LIST)
        self.click(self.locators.ACTION_LIST_DELETE)

    def delete_this_segment(self, name_of_segment):
        self.send_value(self.locators.SEARCH_OF_SEGMENTS, name_of_segment)
        self.locators.ELEMENT_OF_SEARCH_SEGMENTS = (
            By.XPATH, f"//li[@title='{name_of_segment}']"
        )
        self.wait_find(self.locators.ELEMENT_OF_SEARCH_SEGMENTS)
        self.click(self.locators.ELEMENT_OF_SEARCH_SEGMENTS)
        self.click(self.locators.CHECKBOX_ALL_DELETE)
        self.click(self.locators.ACTION_LIST)
        self.click(self.locators.ACTION_LIST_DELETE)