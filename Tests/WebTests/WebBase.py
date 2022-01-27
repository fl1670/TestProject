from Tests.Base import Base


class WebBase(Base):

    def setup_class(self):
        pass

    def setup_method(self):
        self.APP.web_any_page.goto_url('https://yandex.ru/')

    def teardown_method(self):
        pass

    def teardown_class(self):
        self.APP.driver_instance.stop_driver()
