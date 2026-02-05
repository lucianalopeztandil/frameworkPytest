from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PythonFramework.selectors.selectors import SELECTOR_COUNTRY, SELECTOR_PRESENCE_ELEMENT, \
    SELECTOR_COUNTRIES_SUGGESTION, SELECTOR_CHECKBOX_PURCHASE, SELECTOR_PURCHASE_BTN, SELECTOR_SUCCESS_MESSAGE


class PurchasePage:

    def __init__(self, driver):
        self.driver = driver
        self.country_input = SELECTOR_COUNTRY
        self.presence_option = SELECTOR_PRESENCE_ELEMENT
        self.countries = SELECTOR_COUNTRIES_SUGGESTION
        self.checkbox_option = SELECTOR_CHECKBOX_PURCHASE
        self.purchase_btn = SELECTOR_PURCHASE_BTN
        self.success_message = SELECTOR_SUCCESS_MESSAGE

    def executePurchase(self):
        self.driver.find_element(*self.country_input).send_keys("Ind")

        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located(self.presence_option))

        countries = self.driver.find_elements(*self.countries)

        for country in countries:
            if country.text == "India":
                country.click()
                break

        self.driver.find_element(*self.checkbox_option).click()
        self.driver.find_element(*self.purchase_btn).click()


    def validateMessage(self):
        successMessage = self.driver.find_element(*self.success_message).text
        print(successMessage)
        assert "Success!" in successMessage, "There was an error in the purchase operation"