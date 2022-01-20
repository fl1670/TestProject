import time

from TESTS.WebTests.WebTestBase import WebTestBase


class TestMainPage(WebTestBase):

    def test_search_result(self):
        self.APP.web_main_page.input_text_in_search('Test')
        self.APP.web_main_page.click_button_submit()

        time.sleep(2)

        search_result_text = self.APP.web_search.get_search_result_text()

        for text in search_result_text:
            assert 'Тест' in text


