from FW.API.APIBase import APIBase


class ApiUser(APIBase):

    def get_users(self, params=None):
        url = f'{self.manager.data.branch}/api/users'
        return self.request_get(url, params)

    def add_user(self):
        urn = '/api/users'
        uri = self.manager.data.branch + urn
        body = {
            "name": "test 12",
            "job": "leader"
        }
        return self.request_post(uri, body)
