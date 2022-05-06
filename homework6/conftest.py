import os

import pytest

from mysql.client import MysqlClient


def pytest_configure(config):
    mysql_client = MysqlClient(user='root', password='0000', db_name='TEST_SQL')
    if not hasattr(config, 'workerinput'):
        mysql_client.create_db()
    mysql_client.connect(db_created=True)
    if not hasattr(config, 'workerinput'):
        mysql_client.create_table("TotalCount")
        mysql_client.create_table("TotalNumberOfRequestsByType")
        mysql_client.create_table("TopMostFrequentRequests")
        mysql_client.create_table("TopClientErrors")
        mysql_client.create_table("TopServerErrors")
    config.mysql_client = mysql_client


@pytest.fixture(scope='session')
def mysql_client(request) -> MysqlClient:
    client = request.config.mysql_client
    yield client
    client.connection.close()


def repo_root():
    return os.path.abspath(os.path.join(__file__, os.path.pardir))
