import allure
from allure_commons.types import AttachmentType
from FW.FWBase import FWBase


class AnyPage(FWBase):

    def GetDriver(self):
        if self.manager.driver_instance.driver is None:
            self.manager.driver_instance.get_driver()
        return self.manager.driver_instance.driver

    @allure.step('goto_url - {url}')
    def goto_url(self, url):
        self.GetDriver().get(url)

    def allure_screenshot(self):
        try:
            allure.attach(self.GetDriver().get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        except Exception as e:
            print(str(e))
