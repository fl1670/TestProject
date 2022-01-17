import requests
from FW.FWBase import FWBase


class APIBase(FWBase):

    def request_get(self, url, params=None):
        get = requests.get(url, params=params, headers=self.manager.data.head)
        return get.json()

    def request_post(self, url, body, params=None):
        post = requests.post(url, body, params)
        return post.json()

    def request_put(self, user_id):
        urn = '/api/users/' + str(user_id)
        uri = self.manager.data.branch + urn
        params = {}

        body = {
            "email": "tobias",
            "first_name": "Tobias123",
            "last_name": "Funke123",
            "avatar": "https"
        }
        put = requests.patch(uri, body, params=params)
        return put.json()

    def get_single_user(self, user_id):
        urn = '/api/users/' + str(user_id)
        uri = self.manager.data.branch + urn
        params = {}

        put = requests.get(uri, params=params)
        return put.json()
