from test_api.base import BaseApi
import pytest

class TestApi(BaseApi):

    @pytest.mark.API
    def test_valid_login(self):
        self.api_client.post_login_target()
        answer = self.api_client._request('GET', location='https://target.my.com/profile/contacts', jsonify=False)
        assert answer.status_code == 200

    @pytest.mark.API
    def test_create_campaign(self):
        answer, compaign_id = self.api_client.post_create_campaign(name=self.randStr(digist=False))
        assert answer.status_code == 200
        answer = self.api_client.post_delete_compaign(compaign_id)
        assert answer.status_code == 204

    @pytest.mark.API
    def test_create_segment(self):
        answer, segment_id = self.api_client.post_create_segment(name=self.randStr(digist=False))
        assert answer.status_code == 200
        response = self.api_client.open_segment(segment_id)
        assert response['items'][-1]['id'] == segment_id

    @pytest.mark.API
    def test_delete_segment(self):
        answer, segment_id = self.api_client.post_create_segment(name=self.randStr(digist=False))
        assert answer.status_code == 200
        self.api_client.delete_segment(segment_id).status_code == 200

        response = self.api_client.open_segment(segment_id)
        assert response['items'][-1]['id'] != segment_id
