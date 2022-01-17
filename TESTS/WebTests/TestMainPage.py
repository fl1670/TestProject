import time

from TESTS.WebTests.WebTestBase import WebTestBase
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestMainPage(WebTestBase):

    def test_qwert(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://yandex.ru/')

        element = self.driver.find_element(By.XPATH, '//input[@name="text"]')

        element.send_keys('Test')

        self.driver.quit()


