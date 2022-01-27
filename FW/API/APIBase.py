import allure
import requests
from FW.FWBase import FWBase


class APIBase(FWBase):

    @allure.step('request_get')
    def request_get(self, url, params=None):
        get = requests.get(url, params=params, headers=self.manager.data.head)
        return get.json()

    @allure.step('request_post')
    def request_post(self, url, body, params=None):
        post = requests.post(url, body, params=params)
        return post.json()

    @allure.step('request_put')
    def request_put(self, url, body, params=None):
        put = requests.patch(url, body, params=params)
        return put.json()

    @allure.step('get_single_user')
    def get_single_user(self, user_id):
        urn = '/api/users/' + str(user_id)
        uri = self.manager.data.branch + urn
        params = {}

        put = requests.get(uri, params=params)
        return put.json()
