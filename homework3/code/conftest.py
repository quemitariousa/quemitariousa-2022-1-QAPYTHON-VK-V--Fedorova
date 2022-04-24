import pytest
from selenium.webdriver.chrome import webdriver
from files import userdata
from api.client import ApiClient
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope='session')
def config(request):
    pass


@pytest.fixture(scope="function")
def api_client(config) -> ApiClient:
    api_client = ApiClient(user=userdata.login, password=userdata.password)
    return api_client
