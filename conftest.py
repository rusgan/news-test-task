import pytest
import os
from appium import webdriver

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


@pytest.fixture(scope='session', autouse=True)
def driver_setup(request):
    capabilities = {
        'platformName': 'Android',
        'deviceName': 'pixel3',
        'app': PATH('app/news.apk'),
        'avd': 'pixel3'
    }
    url = 'http://localhost:4723/wd/hub'
    driver = webdriver.Remote(url, capabilities)

    def teardown():
        driver.quit()
    request.addfinalizer(teardown)
    return driver
