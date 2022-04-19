from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class TotalCountModel(Base):
    __tablename__ = 'TotalCount'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f"Total Count: {self.total_count}"

    id = Column(Integer, primary_key=True, autoincrement=True)
    total_count = Column(Integer)


class TotalNumberOfRequestsByTypeModel(Base):
    __tablename__ = 'TotalNumberOfRequestsByType'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f"Total number of requests by type: {self.total_number_by_requests_by_type}" \
               f"Type: {self.requests_type}"

    id = Column(Integer, primary_key=True, autoincrement=True)
    total_number_by_requests_by_type = Column(Integer)
    requests_type = Column(String(412), nullable=False)


class Top10MostFrequentRequestsModel(Base):
    __tablename__ = 'Top10MostFrequentRequests'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f"Top 10 most frequent requests: {self.id_top_10_most_frequent_requests}" \
               f"Url: {self.url_requests}" \
               f"Count: {self.count_requests}"

    id_top_10_most_frequent_requests = Column(Integer, primary_key=True, autoincrement=True)
    url_requests = Column(String(250), nullable=False)
    count_requests = Column(Integer)


class TopClientErrorsModel(Base):
    __tablename__ = 'TopClientErrors'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f"Id client error: {self.id_client_error}" \
               f"Size: {self.count_client_error}" \
               f"IP: {self.IP_client_error}" \
               f"Url: {self.url_client_error}" \
               f"Status: {self.status_client_error}"

    id_client_error = Column(Integer, primary_key=True, autoincrement=True)
    size_client_error = Column(Integer)
    status_client_error = Column(String(4), nullable=False)
    IP_client_error = Column(String(16), nullable=False)
    url_client_error = Column(String(250), nullable=False)


class TopServerErrorsModel(Base):
    __tablename__ = 'TopServerErrors'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f"Id server error: {self.id_server_error}" \
               f"Count: {self.count_server_error}" \
               f"IP: {self.IP_server_error}"

    id_server_error = Column(Integer, primary_key=True, autoincrement=True)
    count_server_error = Column(Integer)
    IP_server_error = Column(String(16), nullable=False)
