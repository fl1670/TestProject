from Tests.WebTests.WebBase import WebBase
import allure


@allure.feature('Web - Tests')
@allure.story('TestMainPage')
class TestMainPage(WebBase):

    @allure.title('test_search_result')
    def test_search_result(self):
        main_page = self.APP.web_main_page
        search = main_page.input_text_in_search('Test').click_button_submit()
        search.get_search_result_text()


        # for text in search_result_text:
        #     assert 'Тест' in text
