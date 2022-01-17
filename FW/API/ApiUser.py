from FW.API.APIBase import APIBase


class ApiUser(APIBase):

    def get_users(self, params=None):
        url = f'{self.manager.data.branch}/api/users'
        return self.request_get(url, params)

    def add_user(self, body):
        url = f'{self.manager.data.branch}/api/users'
        return self.request_post(url, body)

    def edit_user(self, user_id, body, params=None):
        url = f'{self.manager.data.branch}/api/users/{user_id}'
        return self.request_put(url, body, params=params)
