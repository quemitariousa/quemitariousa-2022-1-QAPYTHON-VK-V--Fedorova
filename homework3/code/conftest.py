import os
import pytest

from homework3.code.api.client import ApiClient
from homework3.code.files import userdata


@pytest.fixture(scope='session')
def config(request):
    pass


@pytest.fixture(scope="function")
def api_client(config) -> ApiClient:
    api_client = ApiClient(user=userdata.login, password=userdata.password)
    return api_client


@pytest.fixture(scope='session')
def repo_root():
    return os.path.abspath(os.path.join(__file__, os.path.pardir))
