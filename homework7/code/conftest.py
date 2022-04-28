import logging
import os
import shutil
import sys

import pytest
import time
import settings
import requests
from requests.exceptions import ConnectionError

from mock import flask_mock
from serv_http.client import HttpClient


def wait(host=None, port=None, name=None):
    if host is None or port is None or name is None:
        raise TypeError(f'Something is NoneType: host - {host}, port - {port}, name - {name}')
    started = False
    st = time.time()
    while time.time() - st <= 5:
        try:
            requests.get(f'http://{host}:{port}')
            started = True
            break
        except ConnectionError:
            pass

    if not started:
        raise RuntimeError(f'{name} did not started in 5s!')


def start_mock():
    flask_mock.run_mock()
    wait(host=settings.MOCK_HOST, port=settings.MOCK_PORT, name=start_mock.__name__)


def stop_mock():
    requests.get(f'http://{settings.MOCK_HOST}:{settings.MOCK_PORT}/shutdown')


def pytest_configure(config):
    if not hasattr(config, 'workerinput'):
        start_mock()


def pytest_unconfigure(config):
    if not hasattr(config, 'workerinput'):
        stop_mock()


@pytest.fixture(scope='function')
def mock_client():
    return HttpClient(settings.MOCK_HOST, int(settings.MOCK_PORT))

