import random
import string
import pytest

from utils.builder import Builder


class BaseApi:
    BLOG_ID = 403

    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, api_client):
        self.api_client = api_client
        self.builder = Builder()

        if self.authorize:
            self.api_client.post_login_target()

    def randStr(self, chars=string.ascii_uppercase + string.digits, N=10, digist=False):
        if digist:
            return ''.join(random.choice(string.digits) for _ in range(N))
        else:
            return ''.join(random.choice(chars) for _ in range(N))

