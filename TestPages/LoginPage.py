from selenium.webdriver.common.by import By

from Utility_files import Driverwait


class LoginPage:

    def __init__(self,driver):
        self.forgot_password_locator = "//p[contains(.,'Forgot your password')]"
        self.username_locator = "//*[@name='username']"
        self.password_locator = "//*[@name='password']"
        self.login_button_locator = "//button[text()=' Login ']"
        self.loginpage_driver = driver

    def click_forgot_password(self):
        Driverwait.driver_wait_until_visible(self.loginpage_driver, 5, self.forgot_password_locator)
        self.loginpage_driver.find_element(By.XPATH, self.forgot_password_locator).click()

    def check_page_loaded(self):
        Driverwait.driver_wait_until_visible(self.loginpage_driver, 5, self.forgot_password_locator)
        self.loginpage_driver.find_element(By.XPATH, self.forgot_password_locator)
        return True

    def enter_username(self, username_text):
        Driverwait.driver_wait_until_visible(self.loginpage_driver, 5, self.username_locator)
        self.loginpage_driver.find_element(By.XPATH, self.username_locator).send_keys(username_text)

    def enter_password(self, password_text):
        Driverwait.driver_wait_until_visible(self.loginpage_driver, 5, self.password_locator)
        self.loginpage_driver.find_element(By.XPATH, self.password_locator).send_keys(password_text)

    def click_login_button(self):
        Driverwait.driver_wait_until_visible(self.loginpage_driver, 5, self.login_button_locator)
        self.loginpage_driver.find_element(By.XPATH, self.login_button_locator).click()



