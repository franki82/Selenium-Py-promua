import unittest
from src.objects.driver_initiation import DriverInitiation
from src.objects.elements_initiation import ElementsInitiation
from src.utils.config_reader import read_config
from ddt import ddt, data


@ddt
class PromUaSmokeTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver_obj = DriverInitiation()
        cls.elements = ElementsInitiation(cls.driver_obj.get_driver())
        cls.elements.main_page.set_default_page_url(read_config('DEFAULT', 'URL'))

    def setUp(self):
        self.elements.main_page.open_default_page()

    @data("18650", "21700")
    def test_smoke_search_verification_01(self, search_value):
        print("testcase: " + str(search_value))
        self.elements.main_page.verify_default_main_page()
        self.elements.search.simple_search(search_value)
        list_plates = self.elements.search.get_product_plates()
        self.elements.main_page.verify_true(len(list_plates) > 0, "list plates are empty")
        for this_plate in list_plates:
            product_description = self.elements.search.get_product_description(this_plate)
            print("product description: " + product_description)
            self.elements.main_page.verify_true(search_value in product_description,
                                                "product description is not contains " + search_value)

    def tearDown(self):
        self.elements.custom_utilities.log_error_and_create_screenshot(self)

    @classmethod
    def tearDownClass(cls):
        cls.driver_obj.driver_quite()


if __name__ == "__main__":
    unittest.main(verbosity=2)
