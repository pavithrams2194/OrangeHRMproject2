import time
import unittest

from selenium.common import NoSuchElementException

from TestPages.LoginPage import LoginPage
from TestPages.ResetPasswordPage import ResetPasswordPage
from TestPages.ResetSuccessfullPage import ResetSuccessfullPage
from Utility_files.Utilities_mod import Utilities

# TC_PIM_01
# Forgot Password link validation on login page


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.utility_obj = Utilities()
        self.driver = self.utility_obj.initialize_driver()
        self.loginpage_obj = LoginPage(self.driver)
        self.reset_pswd_obj = ResetPasswordPage(self.driver)
        self.reset_success_obj = ResetSuccessfullPage(self.driver)

    def test_ResetPassword(self):
        self.loginpage_obj.click_forgot_password()
        self.assertEqual(True,self.reset_pswd_obj.check_page_loaded())
        self.reset_pswd_obj.enter_username("Admin")
        self.reset_pswd_obj.click_reset_button()
        self.assertEqual(True,self.reset_success_obj.check_page_loaded())
        self.utility_obj.take_screenshot()

    def test_username_required_tip(self):
        self.loginpage_obj.click_forgot_password()
        self.reset_pswd_obj.click_reset_button()
        self.assertEqual(True, self.reset_pswd_obj.check_required_visiblity())
        self.reset_pswd_obj.enter_username("admin123")

        try:
            self.assertEqual(True, self.reset_pswd_obj.check_required_visiblity())
        except NoSuchElementException:
            self.assertEqual(True,True)

        self.reset_pswd_obj.click_reset_button()
        self.assertEqual(True,self.reset_success_obj.check_page_loaded())
        self.utility_obj.take_screenshot()

    def test_cancel_button(self):
        self.loginpage_obj.click_forgot_password()
        self.reset_pswd_obj.enter_username("Admin")
        self.reset_pswd_obj.click_cancel_button()
        self.assertEqual(True,self.loginpage_obj.check_page_loaded())
        self.utility_obj.take_screenshot()


if __name__ == '__main__':
    unittest.main()
