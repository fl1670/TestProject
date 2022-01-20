from TESTS.TestBase import TestBase
from selenium import webdriver


class WebTestBase(TestBase):

    def setup_class(self):
        self.driver = webdriver.Chrome()

    def setup_method(self):
        self.driver.get('https://yandex.ru/')

    def teardown_method(self):
        pass

    def teardown_class(self):
        self.driver.quit()

