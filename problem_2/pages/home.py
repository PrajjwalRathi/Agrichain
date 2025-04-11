from selenium.webdriver.common.by import By

class HomePage:
    URL = "https://agrichain.com/qa/input"
    INPUT_FIELD = (By.ID, "inputString")
    SUBMIT_BUTTON = (By.ID, "submitBtn")

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    def enter_input(self, input_text):
        input_element = self.driver.find_element(*self.INPUT_FIELD)
        input_element.clear()
        input_element.send_keys(input_text)

    def click_submit(self):
        self.driver.find_element(*self.SUBMIT_BUTTON).click()
