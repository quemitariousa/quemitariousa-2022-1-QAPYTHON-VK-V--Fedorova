import json
import socket

from urllib3.util import timeout

import settings


class HttpClient:

    def __init__(self, host, port):
        self.host = settings.MOCK_HOST
        self.port = int(settings.MOCK_PORT)
        self.client = None

    def connect(self):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(0.5)
        client.connect((self.host, self.port))
        self.client = client
        return client

    def client_recv(self):
        total_data = []
        while True:
            # читаем данные из сокета до тех пор пока они там есть
            data = self.client.recv(4096)
            if data:
                print(f'received data: {data}')
                total_data.append(data.decode())
            else:
                self.client.close()
                break
        # ^решение кривое, не делайте так
        data = ''.join(total_data).splitlines()
        return data

    def get_user_count_dog(self, name):
        self.connect()
        params = f'/get_count_dog/{name}'
        request = f'GET {params} HTTP/1.1\r\nHost:{self.host}\r\n\r\n'
        self.client.send(request.encode())
        return self.client_recv()

    def create_user(self, name, count_of_dog):
        self.connect()
        params = f'/create_user'
        body = {'name': name, 'dog': count_of_dog}
        json_data = json.dumps(body)
        resp = self.type_request('POST', params, json_data, self.host)
        return resp

    def delete_user(self, name):
        self.connect()
        params = f'/delete_user/{name}'
        body = {'name': name}
        json_data = json.dumps(body)
        resp = self.type_request('DELETE', params, json_data, self.host)
        return resp

    def change_user_count_dog(self, name, count_of_dog):
        self.connect()
        params = f'/change_dog/{name}'
        body = {'name': name, 'dog': count_of_dog}
        json_data = json.dumps(body)
        resp = self.type_request('PUT', params, json_data, self.host)
        return resp

    def type_request(self, method, params, json_data, host):
        request = f'{method} {params} HTTP/1.1\r\n' \
                  f'Content-Type: application/json\r\n' \
                  f'Content-Length:{str(len(json_data))}\r\n' \
                  f'HOST: {host}\r\n\r\n' \
                  f'{json_data}\r\n'
        self.client.send(request.encode())
        resp = self.client_recv()
        return resp

