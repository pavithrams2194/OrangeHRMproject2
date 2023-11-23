from selenium.webdriver.common.by import By

from Utility_files import Driverwait


class ResetPasswordPage:
    def __init__(self,driver):
        self.reset_pswd_driver = driver
        self.username_locator = "//input[@name = 'username']"
        self.reset_pswd_locator = "//button[text()=' Reset Password ']"
        self.cancel_button_locator = "//button[text()=' Cancel ']"
        self.page_locator = "//*[text()='Reset Password']"
        self.required_locator="//*[text()='Required']"

    def enter_username(self,username_text):
        Driverwait.driver_wait_until_visible(self.reset_pswd_driver, 5, self.username_locator)
        self.reset_pswd_driver.find_element(By.XPATH, self.username_locator).send_keys(username_text)

    def click_reset_button(self):
        Driverwait.driver_wait_until_clickable(self.reset_pswd_driver, 5, self.reset_pswd_locator)
        self.reset_pswd_driver.find_element(By.XPATH,self.reset_pswd_locator).click()

    def click_cancel_button(self):
        self.reset_pswd_driver.find_element(By.XPATH,self.cancel_button_locator).click()

    def check_page_loaded(self):
        Driverwait.driver_wait_until_visible(self.reset_pswd_driver, 5, self.page_locator)
        return True

    def check_required_visiblity(self):
        self.reset_pswd_driver.find_element(By.XPATH,self.required_locator)
        return True




