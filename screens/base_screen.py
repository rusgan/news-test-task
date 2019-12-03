from time import sleep

from selenium.common.exceptions import NoSuchElementException, WebDriverException, StaleElementReferenceException
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BaseScreen:

    def __init__(self, driver):
        self.driver = driver

    # get elements
    def get_element(self, locator):
        method = locator[0]
        values = locator[1]
        return self.get_element_by_type(method, values)

    def get_element_by_type(self, method, value):
        if method == 'accessibility_id':
            return self.driver.find_element_by_accessibility_id(value)
        elif method == 'android':
            return self.driver.find_element_by_android_uiautomator('new UiSelector().%s' % value)
        elif method == 'ios':
            return self.driver.find_element_by_ios_uiautomation(value)
        elif method == 'class_name':
            return self.driver.find_element_by_class_name(value)
        elif method == 'id':
            return self.driver.find_element_by_id(value)
        elif method == 'xpath':
            return self.driver.find_element_by_xpath(value)
        elif method == 'name':
            return self.driver.find_element_by_name(value)
        else:
            raise Exception('Invalid locator method.')

    def get_elements(self, locator):
        method = locator[0]
        value = locator[1]
        self.wait_until_visible(locator)
        return self.get_elements_by_type(method, value)

    def get_elements_by_type(self, method, value):
        if method == 'accessibility_id':
            return self.driver.find_elements_by_accessibility_id(value)
        elif method == 'android':
            return self.driver.find_elements_by_android_uiautomator(value)
        elif method == 'ios':
            return self.driver.find_elements_by_ios_uiautomation(value)
        elif method == 'class_name':
            return self.driver.find_elements_by_class_name(value)
        elif method == 'id':
            return self.driver.find_elements_by_id(value)
        elif method == 'xpath':
            return self.driver.find_elements_by_xpath(value)
        elif method == 'name':
            return self.driver.find_elements_by_name(value)
        else:
            raise Exception('Invalid locator method.')

    # element visible
    def is_visible(self, locator):
        try:
            self.get_element(locator).is_displayed()
            return True
        except NoSuchElementException:
            return False

    # clicks and taps
    def click(self, locator):
        element = self.wait_until_visible(locator)
        element.click()

    # send keys
    def send_keys(self, locator, text):
        element = self.wait_until_visible(locator)
        element.send_keys(text)

    def get_text(self, locator):
        element = self.wait_until_visible(locator)
        return element.text

    def long_press(self, locator, duration=1000):
        element = self.get_element(locator)
        action = TouchAction(self.driver)
        action.long_press(element, None, None, duration).perform()

    def hide_keyboard(self):
        try:
            sleep(1)
            self.driver.hide_keyboard()
        except WebDriverException:
            pass

    def toggle_wifi(self):
        self.driver.toggle_wifi()

    def close_app(self):
        self.driver.close_app()

    def launch_app(self):
        self.driver.launch_app()

    def wait_until_visible(self, locator):

        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.visibility_of_element_located(locator))

    def wait_until_stale(self, element):

        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.staleness_of(element))

    def scroll_down(self):
        actions = TouchAction(self.driver)
        window_size = self.driver.get_window_size()
        half = window_size["height"] / 2
        quarter = window_size["height"] / 4
        actions.press(x=10, y=half).move_to(x=10, y=quarter).release().perform()

    def scroll_down_until_invisible(self, locator):
        while self.is_visible(locator):
            self.scroll_down()
