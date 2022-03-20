import allure
import pytest
from tests.base import BaseCase


class Test(BaseCase):
    @allure.epic('UI tests')
    @allure.feature('Authorization')
    @allure.title('Test login with wrong password')
    @pytest.mark.UI
    def test_login_wrong_password(self, login_page):
        login_page.negative_auth('quemitariousa6@gmail.com', '3423')
        assert "https://account.my.com/login/?error_code" in self.driver.current_url

    @allure.epic('UI tests')
    @allure.title('Test login with wrong email')
    @pytest.mark.UI
    def test_login_wrong_email(self, login_page):
        login_page.negative_auth('yatakustala@gmail.com', 'heyhey')
        assert self.driver.current_url != "https://target.my.com/dashboard"

    @allure.epic('UI tests')
    @allure.feature('Company')
    @allure.title('Test create company')
    @pytest.mark.UI
    def test_create_company(self, company_page):
        company_page.create_company()
        assert company_page.wait_find(company_page.locators.MY_COMPANY_NAME_IN_LIST)

    @allure.epic('UI tests')
    @allure.feature('Segment')
    @allure.title('Test create segment')
    @pytest.mark.UI
    def test_create_segment(self, segments_page):
        name_for_delete = segments_page.create_segment()
        assert segments_page.wait_find(segments_page.locators.MY_SEGMENT_NAME_IN_LIST)
        segments_page.delete_this_segment(name_for_delete)

    @allure.epic('UI tests')
    @allure.feature('Segment')
    @allure.title('Test delete segment')
    @pytest.mark.UI
    def test_delete_segment(self, segments_page):
        segments_page.delete_segment()
        assert segments_page.wait_find(segments_page.locators.CREATE_FIRST_SEGMENT)
