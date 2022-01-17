import pytest
from TESTS.TestBase import TestBase


class TestRequests(TestBase):
    test_data = [
    {
        'page': 3,
        "per_page": 3,
    },
    {
        'page': 1,
        "per_page": 2,
    },
    {
        'page': 3,
        "per_page": 2,
    }
    ]

    @pytest.mark.parametrize('params', test_data)
    def test_request_get(self, params):

        request = self.APP.api_user.get_users(params)
        assert params['page'] == request['page']
        assert params['per_page'] == request['per_page']

    test_data2 = [
        {
            'page': 1,
            "per_page": 2,
        },
        {
            'page': 1,
            "per_page": 10,
        },
        {
            'page': 1,
            "per_page": 12,
        },
    ]

    @pytest.mark.parametrize('params', test_data2)
    def test_request_get2(self, params):
        request = self.APP.api_user.get_users(params)
        assert params['per_page'] == len(request['data'])

    def test_edit_user(self):
        user = self.APP.api_user.get_users({'page': 3, "per_page": 1})
        user_id = user['data'][0]['id']

        body = {
            "email": "tobias",
            "first_name": "Tobias",
            "last_name": "Funke",
            "avatar": "https"
        }
        edit_user = self.APP.api_user.edit_user(user_id, body)
        print(edit_user)

        assert body["email"] == edit_user['email']
        assert body["first_name"] == edit_user['first_name']
        assert body["last_name"] == edit_user['last_name']
        assert body["avatar"] == edit_user['avatar']

    def test_add_user(self):
        body = {
            "name": "Name",
            "job": "leader"
        }
        request = self.APP.api_user.add_user(body)
        assert body["name"] == request['name']
        assert body["job"] == request['job']
        assert 'id' in request







