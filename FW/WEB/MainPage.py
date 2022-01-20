from FW.WEB.AnyPage import AnyPage
from selenium.webdriver.common.by import By


class MainPage(AnyPage):

    def input_text_in_search(self, text):
        element = self.driver.find_element(By.XPATH, '//input[@name="text"]')
        element.send_keys(text)

    def click_button_submit(self):
        self.driver.find_element(By.XPATH, '//button[@type="submit"]').click()
