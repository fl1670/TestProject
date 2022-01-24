from FW.FWBase import FWBase


class AnyPage(FWBase):

    def GetDriver(self):
        if self.manager.driver_instance.driver is None:
            self.manager.driver_instance.get_driver()
        return self.manager.driver_instance.driver

    def goto_url(self, url):
        self.GetDriver().get(url)
