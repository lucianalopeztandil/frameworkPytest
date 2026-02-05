from PythonFramework.data.dataTest import USERNAME, PASSWORD
from PythonFramework.selectors.selectors import SELECTOR_USERNAME, SELECTOR_PASSWORD, SELECTOR_BTN_LOGIN


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.input_username = SELECTOR_USERNAME
        self.input_password = SELECTOR_PASSWORD
        self.btn = SELECTOR_BTN_LOGIN

    def login(self):
        self.driver.get("https://rahulshettyacademy.com/loginpagePractise/")
        self.driver.find_element(*self.input_username).send_keys(USERNAME)
        self.driver.find_element(*self.input_password).send_keys(PASSWORD)
        self.driver.find_element(*self.btn).click()
