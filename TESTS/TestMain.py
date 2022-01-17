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









