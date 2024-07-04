from src.objects.functionality.general_search import GeneralSearch
from src.objects.pagination.main_page import MainPage
from src.utils.config_reader import read_config
from src.utils.custom_utilities import CustomUtilities


class ElementsInitiation:

    def __init__(self, driver):
        self.load_timeout = read_config('DEFAULT', 'TIMEOUT')
        self.main_page = MainPage(driver, self.load_timeout)
        self.custom_utilities = CustomUtilities(driver)
        self.search = GeneralSearch(driver, self.load_timeout)
