import logging
import requests
from files import userdata
logger = logging.getLogger('test')

MAX_RESPONSE_LENGTH = 300


class InvalidLoginException(Exception):
    pass


class RespondErrorException(Exception):
    pass


class ResponseStatusCodeException(Exception):
    pass


class ApiClient:

    def __init__(self, base_url, user, password):
        self.base_url = base_url
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

    # target_авторизация
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
        print(self.csrf_token)
        headers = {'Referer': 'https://target.my.com/segments/segments_list/new/',
                   'X-CSRFToken': self.csrf_token}
        data = {
            "name": f"{name}",
            "pass_condition": pass_condition,
            "relations": [{"object_type": object_type, "params": {"left": left, "right": right, "type": seg_type}}]
        }
        response = self.session.post(url=location, headers=headers, json=data)
        response_data = response.json()
        segment_id = response_data['id']
        print(segment_id)
        return response, segment_id

    def open_segment(self, segment_id):
        url = "https://target.my.com/api/v2/remarketing/segments.json?limit=100"

        headers = {
            'Referer': 'https://target.my.com/segments/segments_list',
            'X-Requested-With': 'XMLHttpRequest',
        }

        params = {'id': segment_id}

        response = self._request('GET', location=url, headers=headers, params=params)
        return response

    def delete_segment(self, segment_id):
        url = "https://target.my.com/api/v1/remarketing/mass_action/delete.json"

        headers = {'Referer': 'https://target.my.com/segments/segments_list',
                   'X-CSRFToken': self.csrf_token}

        data = [{"source_id": segment_id, "source_type": "segment"}]

        result = self.session.post(url=url, headers=headers, json=data)
        return result

    def post_create_campaign(self, name, image_id=10259832, url_id=62507943, objective='reach',
                             package_id=960):
        location = "https://target.my.com/api/v2/campaigns.json"
        headers = {"Referer": 'https://target.my.com/campaign/new',
                   "X-CSRFToken": self.csrf_token}

        data = {
            "banners": [{"content": {"image_240x400": {"id": image_id}}, "urls": {"primary": {"id": url_id}}}],
            "name": name,
            "objective": objective,
            "package_id": package_id,
            "budget_limit": 100000,
            "budget_limit_day": 100500
        }
        response = self.session.post(url=location, headers=headers, json=data)
        response_data = response.json()
        compaign_id = response_data['id']
        print(compaign_id)
        return response, compaign_id

    def post_delete_compaign(self, compaign_id, status="deleted"):
        location = "https://target.my.com/api/v2/campaigns/mass_action.json"
        headers = {"Referer": 'https://target.my.com/dashboard',
                   "X-CSRFToken": self.csrf_token
                   }

        data = [{"id": compaign_id, "status": status}]
        response = self.session.post(url=location, headers=headers, json=data)
        return response
