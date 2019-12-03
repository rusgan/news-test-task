from unittest import result

import pytest
import os

from appium.webdriver import webdriver

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class Other:
    driver = None

    def set_up(self):
        capabilities = {
            'platformName': 'Android',
            'deviceName': 'pixel3',
            'app': PATH('app/news.apk')
        }
        url = 'http://localhost:4723/wd/hub'
        self.driver = webdriver.Remote(url, capabilities)

    def tear_down(self):
        self.driver.quit()

