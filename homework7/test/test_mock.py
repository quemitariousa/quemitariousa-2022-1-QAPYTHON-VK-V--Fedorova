import pytest




class TestGet:

    def test_get(self, mock_client):
        resp = mock_client.get_user_count_dog("Lera")
        assert resp[0].split(' ')[1] == '200'

    def test_get_not_exist_user(self, mock_client):
        resp = mock_client.get_user_count_dog("Tihon")
        assert resp[0].split(' ')[1] == '405'


class TestPut:
    def test_put_user(self, mock_client):
        resp = mock_client.change_user_count_dog("Lera", 5)
        assert resp[0].split(' ')[1] == '200'

    def test_put_not_user(self, mock_client):
        resp = mock_client.change_user_count_dog("Lalala", 5)
        assert resp[0].split(' ')[1] == '404'


class TestDelete:
    def test_delete_user(self, mock_client):
        resp = mock_client.delete_user("Lena")
        assert resp[0].split(' ')[1] == '200'
        resp = mock_client.delete_user("Lena")
        assert resp[0].split(' ')[1] == '404'


class TestPost:

    def test_post_user(self, mock_client):
        resp = mock_client.create_user('Mishanya', 4)
        assert resp[0].split(' ')[1] == '200'
        resp = mock_client.create_user('Mishanya', 4)
        assert resp[0].split(' ')[1] == '400'
