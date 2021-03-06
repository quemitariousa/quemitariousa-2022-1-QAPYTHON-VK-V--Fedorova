import logging
import os

import faker
import requests

from homework3.code.files import userdata
from homework3.code.utils.builder import fake

logger = logging.getLogger('test')

MAX_RESPONSE_LENGTH = 300


class InvalidLoginException(Exception):
    pass


class RespondErrorException(Exception):
    pass


class ResponseStatusCodeException(Exception):
    pass


fake = faker.Faker()


class ApiClient:

    def __init__(self, user, password):
        self.user = user
        self.password = password

        self.session = requests.Session()

        self.csrf_token = None
        self.sessionid_gtp = None

    #  общий метод для осуществления get и post запросов
    def _request(self, method, location, headers=None, data=None, expected_status=200, jsonify=True, params=None):
        # Формируем URL
        # url = urljoin(self.base_url, location)
        url = location

        # Делаем запрос
        response = self.session.request(method=method, url=url, headers=headers, data=data, params=params)

        # Проверяем код возврата
        if response.status_code != expected_status:
            raise ResponseStatusCodeException(f'Got {response.status_code} {response.reason} for URL "{url}"')

        if jsonify:
            # Приводим к словарю, если стоит флаг jsonify
            json_response = response.json()
            if json_response.get('bStateError', False):
                error = json_response['sErrorMsg'] or 'Unknown'
                raise RespondErrorException(f'Request {url} returned error {error}!')

            return json_response

        return response

    # получение токена
    def get_token(self):
        location = 'https://target.my.com/csrf/'
        res = self._request('GET', location, jsonify=False)
        headers = res.headers['Set-Cookie'].split(';')
        token_header = [c for c in headers if 'csrftoken' in c]
        if not token_header: raise Exception('csrf_token not found')
        token_header = token_header[0]
        csrf_token = token_header.split('=')[-1]

        return csrf_token

    def post_login_target(self):
        url = 'https://auth-ac.my.com/auth?lang=ru&nosavelogin=0'

        headers = {
            'Origin': 'https://target.my.com',
            'Referer': 'https://target.my.com/',
        }

        data = {
            'email': userdata.login,
            'password': userdata.password,
            'continue': 'https://target.my.com/auth/mycom?state=target_login%3D1%26ignore_opener%3D1#email',
            'failure': 'https://account.my.com/login/'
        }

        result = self._request('POST', url, headers=headers, data=data, jsonify=False)
        self.csrf_token = self.get_token()

        return result

    def post_create_segment(self, name, pass_condition=1, object_type='remarketing_player', left=365, right=0,
                            seg_type='positive'):
        location = "https://target.my.com/api/v2/remarketing/segments.json"
        headers = {
            'X-CSRFToken': self.csrf_token}
        data = {
            "name": f"{name}",
            "pass_condition": pass_condition,
            "relations": [{"object_type": object_type, "params": {"left": left, "right": right, "type": seg_type}}]
        }
        response = self.session.post(url=location, headers=headers, json=data)
        response_data = response.json()
        segment_id = response_data['id']
        return response, segment_id

    def open_segment(self, segment_id):
        url = "https://target.my.com/api/v2/remarketing/segments.json?limit=100"

        headers = {
            'X-Requested-With': 'XMLHttpRequest'
        }

        params = {'id': segment_id}

        response = self._request('GET', location=url, headers=headers, params=params)
        segment_id = response['items'][-1]['id']
        return response, segment_id

    def delete_segment(self, segment_id):
        url = "https://target.my.com/api/v1/remarketing/mass_action/delete.json"

        headers = {'Referer': 'https://target.my.com/segments/segments_list',
                   'X-CSRFToken': self.csrf_token}

        data = [{"source_id": segment_id, "source_type": "segment"}]

        result = self.session.post(url=url, headers=headers, json=data)
        return result

    def post_create_campaign(self, repo_root, name, objective='reach',
                             package_id=960):

        response_picture = self.post_create_picture(repo_root).json()
        id_picture = response_picture['id']

        url_id = self.post_create_url_id(fake.url()).json()
        url_id = url_id['id']
        location = "https://target.my.com/api/v2/campaigns.json"
        headers = {
            "X-CSRFToken": self.csrf_token}

        data = {
            "banners": [{"content": {"image_240x400": {"id": id_picture}},
                         "urls": {"primary": {"id": url_id}}}],
            "name": name,
            "objective": objective,
            "package_id": package_id,
            "budget_limit": 100000,
            "budget_limit_day": 100500
        }
        response = self.session.post(url=location, headers=headers, json=data)
        response_data = response.json()
        campaign_id = response_data['id']
        return response, campaign_id

    def post_delete_compaign(self, campaign_id):
        location = f"https://target.my.com/api/v2/campaigns/{campaign_id}.json"
        headers = {
            "X-CSRFToken": self.csrf_token
        }
        response = self.session.post(url=location, headers=headers)
        return response

    def post_create_picture(self, repo_root):
        file = os.path.join(repo_root, 'files', 'picture.jpg')
        file = open(file, "rb")
        file = {"file": file}
        location = "https://target.my.com/api/v2/content/static.json"
        headers = {
            "X-CSRFToken": self.csrf_token
        }
        response = self.session.post(url=location, headers=headers, files=file)
        return response

    def check_campaign_id(self, campaign_id):
        url = f"https://target.my.com/api/v2/campaigns/{campaign_id}.json"
        response = self.session.get(url=url).json()
        return response

    def post_create_url_id(self, target_url):
        location = f"https://target.my.com/api/v1/urls/?url={target_url}"
        headers = {
            "X-CSRFToken": self.csrf_token
        }
        response = self.session.get(url=location, headers=headers)
        return response
