from selenium.webdriver.common.by import By

class ResultPage:
    RESULT_TEXT = (By.ID, "result")

    def __init__(self, driver):
        self.driver = driver

    def get_result(self):
        return self.driver.find_element(*self.RESULT_TEXT).text
