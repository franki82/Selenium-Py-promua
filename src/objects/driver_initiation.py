from selenium import webdriver
from selenium.webdriver.common.by import By

from src.utils.config_reader import read_config


class DriverInitiation:

    def __init__(self):
        grid_url = read_config('DEFAULT', 'GRID_URL')
        options = webdriver.ChromeOptions()
        options.add_argument('–disable-extensions')
        options.add_argument('start-maximized')
        self._driver = webdriver.Remote(command_executor=grid_url, options=options)

    def get_driver(self):
        return self._driver

    def driver_quite(self):
        self._driver.quit()
