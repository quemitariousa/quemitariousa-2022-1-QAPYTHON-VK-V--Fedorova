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
        count_lines = self.builder.total_count()
        assert 1 == len(self.mysql.session.query(TotalCountModel).all())
        for i in self.mysql.session.query(TotalCountModel).all():
            assert count_lines == i.total_count

    def test_total_number_of_request_by_type(self):
        self.builder.method_count()
        assert 5 == len(self.mysql.session.query(TotalNumberOfRequestsByTypeModel).all())

    def test_top_most_frequent_requests_most_frequent_requests(self, top=5):
        self.builder.top_most_frequent_requests(top)
        assert top == len(self.mysql.session.query(TopMostFrequentRequestsModel).all())

    def test_top_client_errors(self, top=5):
        self.builder.top_4xx(top)
        assert top == len(self.mysql.session.query(TopClientErrorsModel).all())
        for i in self.mysql.session.query(TopClientErrorsModel).all():
            assert '4' == i.status_client_error[0]

    def test_top_server_errors(self, top=5):
        self.builder.top_5xx(top)
        assert top == len(self.mysql.session.query(TopServerErrorsModel).all())
        for i in self.mysql.session.query(TopServerErrorsModel).all():
            assert '5' == i.status_server_error[0]
