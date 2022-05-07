from homework3.code.test_api.base import BaseApi
import pytest

class TestApi(BaseApi):

    @pytest.mark.API
    def test_valid_login(self):
        self.api_client.post_login_target()
        answer = self.api_client._request('GET', location='https://target.my.com/profile/contacts', jsonify=False)
        assert answer.status_code == 200

    @pytest.mark.API
    def test_create_campaign(self, repo_root):
        answer, campaign_id = self.api_client.post_create_campaign(repo_root, name=self.randStr())
        assert answer.status_code == 200
        check_campaign = self.api_client.check_campaign_id(campaign_id)
        assert check_campaign['id'] == campaign_id
        answer = self.api_client.post_delete_compaign(campaign_id)
        assert answer.status_code == 204

    @pytest.mark.API
    def test_create_segment(self):
        answer, segment_id = self.api_client.post_create_segment(name=self.randStr())
        assert answer.status_code == 200
        response, segment_id = self.api_client.open_segment(segment_id)
        assert segment_id == segment_id

    @pytest.mark.API
    def test_delete_segment(self):
        answer, segment_id = self.api_client.post_create_segment(name=self.randStr())
        assert answer.status_code == 200
        assert self.api_client.delete_segment(segment_id).status_code == 200

