from selenium.common import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from src.utils.custom_utilities import CustomUtilities


class Verifications(CustomUtilities):

    def verify_true(self, condition, error_message):
        assert condition, error_message

    def verify_strings(self, actual_string, expected_string):
        assert actual_string.lower() == expected_string.lower(), actual_string + " is not equal " + expected_string

    def if_element_present(self, element_locator, locator_type):
        try:
            expected_conditions.presence_of_element_located((self.get_by_type(locator_type), element_locator))
            return True
        except NoSuchElementException:
            return False
