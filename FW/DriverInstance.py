from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class DriverInstance:

    driver = None

    def get_driver(self):
        options = webdriver.ChromeOptions()
        # options.add_argument('--headless')
        # options.add_argument('--disable-gpu')
        options.add_argument('--window-size=1920,1080')

        capabilities = DesiredCapabilities.CHROME

        self.driver = webdriver.Remote(
            command_executor='http://192.168.0.105:4444',
            proxy=None,
            options=options,
            desired_capabilities=capabilities,
        )

        return self.driver

    def stop_driver(self):
        if self.driver is not None:
            self.driver.quit()
