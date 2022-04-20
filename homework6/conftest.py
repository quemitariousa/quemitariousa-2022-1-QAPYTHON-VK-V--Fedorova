import pytest

from homework6.mysql.client import MysqlClient


def pytest_configure(config):
    mysql_client = MysqlClient(user='root', password='pass', db_name='TEST_SQL')
    if not hasattr(config, 'workerinput'):
        mysql_client.create_db()
    mysql_client.connect(db_created=True)
    if not hasattr(config, 'workerinput'):
        mysql_client.create_table("TotalCount")
        mysql_client.create_table("TotalNumberOfRequestsByType")
        mysql_client.create_table("Top10MostFrequentRequests")
        mysql_client.create_table("TopClientErrors")
        mysql_client.create_table("TopServerErrors")
    config.mysql_client = mysql_client


@pytest.fixture(scope='session')
def mysql_client(request) -> MysqlClient:
    client = request.config.mysql_client
    yield client
    client.connection.close()
