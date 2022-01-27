import allure

from FW.API.APIBase import APIBase


class ApiUser(APIBase):

    @allure.step('get_users')
    def get_users(self, params=None):
        url = f'{self.manager.data.branch}/api/users'
        return self.request_get(url, params)

    @allure.step('add_user')
    def add_user(self, body):
        url = f'{self.manager.data.branch}/api/users'
        return self.request_post(url, body)

    @allure.step('edit_user')
    def edit_user(self, user_id, body, params=None):
        url = f'{self.manager.data.branch}/api/users/{user_id}'
        return self.request_put(url, body, params=params)
