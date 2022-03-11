import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def pytest_addoption(parser):
    parser.addoption('--url', default='https://target.my.com/')
    parser.addoption('--browser', default='chrome')
    parser.addoption('--browser_ver', default='latest')


@pytest.fixture(scope='session')
def config(request):
    url = request.config.getoption('--url')
    browser = request.config.getoption('--browser')
    version = request.config.getoption('--browser_ver')

    return {'browser': browser, 'version': version, 'url': url}


@pytest.fixture(scope='function')
def driver(config):
    url = config['url']
    # browser = webdriver.Chrome(executable_path='C:\Program Files\Python39\chromedriver.exe')
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(url)
    browser.set_window_size(1400, 1000)
    yield browser
    browser.close()
