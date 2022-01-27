from FW.APP import ApplicationManager


class Base:

    APP = ApplicationManager()

    def setup_class(self):
        pass

    def setup_method(self):
        pass

    def teardown_class(self):
        pass

    def teardown_method(self):
        pass

