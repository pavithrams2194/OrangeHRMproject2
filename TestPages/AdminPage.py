from selenium.webdriver.common.by import By

from Utility_files import Driverwait
from Utility_files import Utilities_mod


class AdminPage:

    def __init__(self,driver):
        self.page_locator = "//*[@class = 'oxd-topbar-body-nav-tab-item' and text()='User Management ']"
        self.options_locator = "//*[@class = 'oxd-topbar-body-nav-tab-item']"
        self.adminpage_driver = driver

    def check_page_loaded(self):
        Driverwait.driver_wait_until_visible(self.adminpage_driver, 5, self.page_locator)
        self.adminpage_driver.find_element(By.XPATH, self.page_locator)
        return True

    def get_options(self):
        options = self.adminpage_driver.find_elements(By.XPATH,self.options_locator)
        return Utilities_mod.get_text_from_elements(options)



