import random
import string
import uuid

import pytest
from homework3.code.utils.builder import Builder


class BaseApi:
    BLOG_ID = 403

    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, api_client):
        self.api_client = api_client
        self.builder = Builder()

        if self.authorize:
            self.api_client.post_login_target()

    def randStr(self):
        namespace = uuid.NAMESPACE_URL
        return str(namespace)

