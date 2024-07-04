from selenium.webdriver.common.by import By

from src.utils.verifications import Verifications
from src.utils.waitings import Waitings


class GeneralSearch(Waitings, Verifications):

    def __init__(self, driver, timeout_sec):
        self.driver = driver
        self.timeout_sec = timeout_sec

    _search_input_xpath = "//input[@name='search_term']"
    _start_search_button_not_active_xpath = "//button[@data-qaid='search_btn' and @disabled]"
    _start_search_button_active_xpath = "//button[@data-qaid='search_btn' and not(@disabled)]"
    _clear_search_button_xpath = "//button[@data-qaid='clear_search']"
    _search_results_element_xpath = "//div[@data-qaid='product_gallery']"
    _search_results_items_xpath = "//div[@data-qaid='product_gallery']/div"
    _product_description_xpath = "div//span[@data-qaid='product_name']"

    def simple_search(self, search_value):
        _search_input = self.wait_for_visibility_element(self.driver, self.timeout_sec, self._search_input_xpath,
                                                         "xpath", "search input")
        self.wait_for_visibility_element(self.driver, self.timeout_sec, self._start_search_button_not_active_xpath,
                                         "xpath", "start search button (not active)")
        _search_input.send_keys(search_value)
        self.wait_for_visibility_element(self.driver, self.timeout_sec, self._clear_search_button_xpath,
                                         "xpath", "clear search button")
        _start_search_button_active = self.wait_for_visibility_element(self.driver, self.timeout_sec,
                                                                       self._start_search_button_active_xpath,
                                                                       "xpath", "start search button (active)")
        _start_search_button_active.click()
        print("Start search by value " + str(search_value))

    def get_product_plates(self):
        self.wait_for_visibility_element(self.driver, self.timeout_sec, self._search_results_element_xpath,
                                         "xpath", "search results element")
        return self.get_elements_list(self.driver, self._search_results_items_xpath, "xpath")

    def get_product_description(self, plate_element):
        return self.get_element_within_element(plate_element, self._product_description_xpath, "xpath").text
