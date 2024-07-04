from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from src.utils.custom_utilities import CustomUtilities


class Waitings(CustomUtilities):

    def wait_for_visibility_element(self, driver, timeout_sec, element_locator, locator_type, element_name):
        return WebDriverWait(driver, timeout_sec).until(
            expected_conditions.visibility_of_element_located((self.get_by_type(locator_type), element_locator)),
            message=str(element_name) + ' element is not visible after wait (sec): ' + str(timeout_sec), )

    def wait_for_invisibility_element(self, driver, timeout_sec, element_locator, locator_type, element_name):
        try:
            WebDriverWait(driver, float(timeout_sec)).until(
                expected_conditions.invisibility_of_element_located((self.get_by_type(locator_type), element_locator)),
                message=element_name + ' is still visible after wait (sec): ' + str(timeout_sec), )
        except NoSuchElementException:
            pass

    def wait_for_present_element(self, driver, timeout_sec, element_locator, locator_type, element_name):
        return WebDriverWait(driver, timeout_sec).until(
            expected_conditions.presence_of_element_located((self.get_by_type(locator_type), element_locator)),
            message=str(element_name) + ' element is not present after wait (sec): ' + str(timeout_sec), )

    def get_elements_list(self, driver, element_locator, locator_type):
        return driver.find_elements(self.get_by_type(locator_type), element_locator)

    def get_element_within_element(self, base_element, element_locator, locator_type):
        return base_element.find_element(self.get_by_type(locator_type), element_locator)
