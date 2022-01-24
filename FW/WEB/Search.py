from FW.WEB.AnyPage import AnyPage
from selenium.webdriver.common.by import By


class Search(AnyPage):

    def get_search_result_text(self):
        text_mass = []
        title_content = self.GetDriver().find_elements(By.XPATH, '//*[@id="search-result"]/li//span[contains(@class, "OrganicTitleContentSpan")]')

        for element in title_content:
            text_mass.append(element.text)
        return text_mass

