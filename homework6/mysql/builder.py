import os
from conftest import repo_root
from mysql.models import *


class MysqlBuilder:
    def __init__(self, client):
        self.client = client
        self.lines = self.get_lines()

    def get_lines(self):
        file = os.path.join(repo_root, 'files', 'access.log')
        file = open(file, "rb")
        lines = file.readlines()
        lines = [line.split() for line in lines]
        return lines

    def total_count(self):
        new_row = TotalCountModel(total_count=len(self.lines))
        self.client.session.add(new_row)
        self.client.session.commit()

    def method_count(self):
        set_methods = set()
        count = {}
        for line in self.lines:
            set_methods.add(line[5])
        for item in set_methods:
            count.update({item: count.get(item, 0) + 1})
        for item in set_methods:
            new_row = TotalNumberOfRequestsByTypeModel(total_number_by_requests_by_type=count.get(item),
                                                       requests_type=item
                                                       )
            self.client.session.add(new_row)

        self.client.session.commit()

    def top_10(self):
        count = {}
        counter = 0
        for line in self.lines:
            count.update({line[6]: count.get(line[6], 0) + 1})
        for item in count.keys():
                counter +=1
                new_row = Top10MostFrequentRequestsModel(
                    lines=count.get(item),
                    url_requests=item

                )
                self.client.session.add(new_row)
                if counter >= 10: break
        self.client.session.commit()

    def top_5xx(self):
        urls = []
        for line in self.lines:
            if line[8][0] == '5':
                if line[0] in [i[0] for i in urls]:
                    for k in range(len(urls)):
                        if urls[k][0] == line[0]:
                            urls[k][1] += 1
                else:
                    urls.append([line[0], 1])

        for item in sorted(urls, key=lambda i: i[1], reverse=True)[:5]:
            new_row = TopServerErrorsModel(
                IP_server_error=item[0],
                count_server_error=item[1]

            )
            self.client.session.add(new_row)
        self.client.session.commit()

    def top_4xx(self):
        urls = []
        for line in self.lines:
            if line[8][0] == '4':
                urls.append([line[6], line[8], line[9], line[0]])

        for item in sorted(urls, key=lambda i: int(i[2]), reverse=True)[:5]:
            new_row = TopClientErrorsModel(
                status_client_error=item[1],
                size_client_error=item[2],
                url_client_error=item[0],
                IP_client_error=item[3]
            )
            self.client.session.add(new_row)
        self.client.session.commit()

    def start(self):
        self.top_10()
        self.top_4xx()
        self.top_5xx()
        self.method_count()
        self.total_count()
