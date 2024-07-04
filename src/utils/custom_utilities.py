from datetime import datetime
from pathlib import Path

from selenium.webdriver.common.by import By


class CustomUtilities:

    def __init__(self, driver):
        self.driver = driver
        self.counter_errors_in_class = 0

    def log_error_and_create_screenshot(self, class_element):
        if hasattr(class_element._outcome, 'errors'):
            result = class_element.defaultTestResult()
            class_element._feedErrorsToResult(result, class_element._outcome.errors)
        else:
            result = class_element._outcome.result
        for typ, errors in (('ERROR', result.errors), ('FAIL', result.failures)):
            for test, text in errors:
                if test is class_element:
                    msg = [x for x in text.split('\n')[1:]
                           if not x.startswith(' ')][0]
                    print("\n%s: %s\n     %s" % (typ, class_element.id(), msg))
                    self._create_screenshot()

    def _create_screenshot(self):
        project_path = Path(__file__).parent.parent.parent
        path_to_log = str(project_path) + '/log/'
        screenshot_file_name = "screenshot" + str(datetime.now()) + ".png"
        self.driver.save_screenshot(path_to_log + screenshot_file_name)
        print("screenshot: " + screenshot_file_name)

    def verify_count_of_errors_and_create_screenshot(self, current_counter_of_error):
        if current_counter_of_error > self.counter_errors_in_class:
            self.counter_errors_in_class = current_counter_of_error
            self._create_screenshot()

    def get_by_type(self, locator_type):
        _by_type = None
        match locator_type.lower():
            case 'xpath':
                _by_type = By.XPATH
            case 'id':
                _by_type = By.ID
            case 'name':
                _by_type = By.NAME
            case 'link_text':
                _by_type = By.LINK_TEXT
            case 'partial_link_text':
                _by_type = By.PARTIAL_LINK_TEXT
            case 'tag_name':
                _by_type = By.TAG_NAME
            case 'class_name':
                _by_type = By.CLASS_NAME
            case 'css_selector':
                _by_type = By.CSS_SELECTOR
            case 'css_selector':
                _by_type = By.CSS_SELECTOR
        return _by_type
