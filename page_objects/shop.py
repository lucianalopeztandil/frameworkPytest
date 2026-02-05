from selenium.webdriver.common.by import By

from PythonFramework.selectors.selectors import SELECTOR_PRODUCTS, SELECTOR_PRODUCT_NAME, SELECTOR_ADD_BTN, \
    SELECTOR_CHECKOUT_BTN, SELECTOR_CONFIRM_OPERATION, SELECTOR_SELECTED_ELEMENT


class ShopPage:

    def __init__(self, driver):
        self.driver = driver
        self.products = SELECTOR_PRODUCTS
        self.product_name = SELECTOR_PRODUCT_NAME
        self.addBtn = SELECTOR_ADD_BTN
        self.checkoutBtn = SELECTOR_CHECKOUT_BTN
        self.checkoutConfirm = SELECTOR_CONFIRM_OPERATION
        self.textElement = SELECTOR_SELECTED_ELEMENT

    def selectProduct(self):
        products = self.driver.find_elements(*self.products)
        print(len(products))

        for product in products:
            productName = product.find_element(*self.product_name).text
            print(productName)
            if productName == 'Blackberry':
                print("The element was found")
                product.find_element(*self.addBtn).click()
                break

        self.driver.find_element(*self.checkoutBtn).click()

    def checkout(self):
        print("The selected element is: " + self.driver.find_element(*self.textElement).text)
        self.driver.find_element(*self.checkoutConfirm).click()