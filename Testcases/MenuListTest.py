import unittest

from TestPages.DashboardPage import DashboardPage
from Utility_files import Utilities_mod
from Utility_files.Utilities_mod import Utilities


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.utility_obj = Utilities()
        self.driver = self.utility_obj.initialize_driver()
        self.utility_obj.login_into_orangehrm()
        self.dashboardpage_obj = DashboardPage(self.driver)

    #TC_PIM_03
    #Main menu Validation on Admin Page

    def test_menu_list(self):
        self.dashboardpage_obj.check_is_dashboard_page()
        menu_list=self.dashboardpage_obj.get_menu_list()
        test_list = self.utility_obj.get_test_data().get("menu_list")
        self.assertEqual(True, Utilities_mod.compare_list(menu_list,test_list))  # add assertion here
        self.utility_obj.take_screenshot()


if __name__ == '__main__':
    unittest.main()
