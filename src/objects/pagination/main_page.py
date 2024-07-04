from src.utils.verifications import Verifications
from src.utils.waitings import Waitings


class MainPage(Waitings, Verifications):
    _main_page_url = None

    def __init__(self, driver, timeout_sec):
        self.driver = driver
        self.timeout_sec = timeout_sec

    _promua_promo_panel_xpath = "//div[@data-qaid='promo_panel']"
    _promua_main_logo_xpath = "//a[@title='prom.ua']/img"
    _promua_main_logo1_xpath = "//a[@title='prom1.ua']/img"
    _menu_preview_element_xpath = "//div[@data-qaid='menu_preview']"
    _menu_preview_items_xpath = "//div[@data-qaid='menu_preview']//li/a"
    _actual_banner_image_xpath = "//a[@data-qaid='banner_link']/img"
    _recommended_categories_element_xpath = "//div[@data-qaid='recommended_categories']"
    _recommended_categories_images_xpath = "//div[@data-qaid='recommended_categories']//li//picture"
    _recommended_categories_descriptions_xpath = "//div[@data-qaid='recommended_categories']//li//span/a"
    _personal_feed_element_xpath = "//div[@data-qaid='personal_feed_block']"
    _personal_feed_images_xpath = "//div[@data-qaid='personal_feed_block']//picture"
    _personal_feed_descriptions_xpath = "//div[@data-qaid='personal_feed_block']//a/span"
    _personal_feed_buy_buttons_xpath = "//div[@data-qaid='personal_feed_block']//a[@role='button']"
    _promua_footer_element_xpath = "//div[@data-qaid='footer_links']"

    def set_default_page_url(self, url):
        self._main_page_url = url

    def open_default_page(self):
        self.driver.get(self._main_page_url)

    def verify_default_main_page(self):
        self.wait_for_present_element(self.driver, self.timeout_sec, self._promua_promo_panel_xpath, "xpath",
                                         "promo panel")
        self.wait_for_invisibility_element(self.driver, self.timeout_sec, self._promua_main_logo1_xpath, "xpath",
                                           "main logo 1")
        self.wait_for_visibility_element(self.driver, self.timeout_sec, self._promua_main_logo_xpath, "xpath",
                                         "main logo")
        self.wait_for_visibility_element(self.driver, self.timeout_sec, self._menu_preview_element_xpath, "xpath",
                                         "menu preview element")
        self.wait_for_visibility_element(self.driver, self.timeout_sec, self._actual_banner_image_xpath, "xpath",
                                         "actual banner image")
        self.wait_for_visibility_element(self.driver, self.timeout_sec, self._recommended_categories_element_xpath,
                                         "xpath", "recommended categories element")
        self.wait_for_visibility_element(self.driver, self.timeout_sec, self._personal_feed_element_xpath, "xpath",
                                         "personal feed element")
        print("Main page elements verified")
