import pytest

from mysql.builder import MysqlBuilder
from mysql.client import MysqlClient
from mysql.models import *


class SQLBase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, mysql_client):
        self.mysql: MysqlClient = mysql_client
        self.builder: MysqlBuilder = MysqlBuilder(self.mysql)


class Test_SQL(SQLBase):

    def test_count(self):
        self.builder.total_count()
        assert 1 == len(self.mysql.session.query(TotalCountModel).all())

    def test_total_number_of_request_by_type(self):
        self.builder.method_count()
        assert 5 == len(self.mysql.session.query(TotalNumberOfRequestsByTypeModel).all())

    def test_top_10_most_frequent_requests(self):
        self.builder.top_10()
        assert 10 == len(self.mysql.session.query(Top10MostFrequentRequestsModel).all())

    def test_top_client_errors(self):
        self.builder.top_4xx()
        assert 5 == len(self.mysql.session.query(TopClientErrorsModel).all())

    def test_top_server_errors(self):
        self.builder.top_5xx()
        assert 5 == len(self.mysql.session.query(TopServerErrorsModel).all())
