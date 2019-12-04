from time import sleep

import pytest
import os
from appium import webdriver

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


def pytest_configure():
    pytest.driver = None


@pytest.fixture(scope="session", autouse=True)
def driver_setup(request):
    capabilities = {
        'platformName': 'Android',
        'deviceName': 'pixel3',
        'app': PATH('app/news.apk'),
        'avd': 'pixel3'
    }
    url = 'http://localhost:4723/wd/hub'
    driver = webdriver.Remote(url, capabilities)
    pytest.driver = driver
    if driver.network_connection == 0:
        driver.toggle_wifi()

    def auto_session_resource_teardown():
        driver.quit()

    request.addfinalizer(auto_session_resource_teardown)


@pytest.fixture(scope="function", autouse=True)
def another_resource_setup_with_autouse(request):
    if pytest.driver.network_connection == 0:
        pytest.driver.toggle_wifi()
        sleep(5)
    pytest.driver.start_activity("my.deler.newstestapplication", "my.deler.newstestapplication.screens.MainActivity")

    def resource_teardown():
        print("")

    request.addfinalizer(resource_teardown)
