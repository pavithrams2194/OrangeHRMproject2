import unittest

from selenium.common import NoSuchElementException, InvalidSelectorException
from selenium.common import TimeoutException
from TestPages.AdminPage import AdminPage
from TestPages.DashboardPage import DashboardPage
from Utility_files import Utilities_mod
from Utility_files.Utilities_mod import Utilities

#TC_PIM_02
# Header validation on Admin Page

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.utility_obj = Utilities()
        self.driver = self.utility_obj.initialize_driver()
        self.utility_obj.login_into_orangehrm()
        self.dashboardpage_obj = DashboardPage(self.driver)
        self.admin_page_obj = AdminPage(self.driver)

    def test_admin_page(self):
        try:
            self.assertEqual("OrangeHRM", self.driver.title)
            self.dashboardpage_obj.check_is_dashboard_page()
            self.dashboardpage_obj.click_admin_link()
            self.admin_page_obj.check_page_loaded()
            admin_page_options=self.admin_page_obj.get_options()
            test_data_options = self.utility_obj.get_test_data().get("options_list")
            self.assertEqual(True, Utilities_mod.compare_list(test_data_options,admin_page_options))
            self.utility_obj.take_screenshot()
        except (NoSuchElementException,TimeoutException,InvalidSelectorException) as e:
            self.utility_obj.take_failed_screenshot()
            print(e)

if __name__ == '__main__':
    unittest.main()
