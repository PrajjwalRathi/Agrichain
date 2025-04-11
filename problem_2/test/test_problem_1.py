import unittest
from utilities.driver import Driver
from pages.home import HomePage
from pages.result import ResultPage

class TestLongestSubstring(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver_manager = Driver()
        cls.driver = cls.driver_manager.initialize()
        cls.home_page = HomePage(cls.driver)
        cls.result_page = ResultPage(cls.driver)

    def test_valid_string(self):
        input_text = "abcabcbb"
        expected_result = "3"

        self.home_page.load()
        self.home_page.enter_input(input_text)
        self.home_page.click_submit()


        actual_result = self.result_page.get_result()
        self.assertEqual(
            actual_result, expected_result,
            f"Expected result to be {expected_result} but got {actual_result}"
        )

    @classmethod
    def tearDownClass(cls):
        cls.driver_manager.quit()

if __name__ == '__main__':
    unittest.main()
