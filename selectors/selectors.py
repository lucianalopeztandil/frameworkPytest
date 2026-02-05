from selenium.webdriver.common.by import By

#selectores pantalla login

SELECTOR_USERNAME = (By.ID, "username")
SELECTOR_PASSWORD = (By.NAME, "password")
SELECTOR_BTN_LOGIN = (By.ID, "signInBtn")

#selectores pantalla seleccion producto

SELECTOR_PRODUCTS = (By.CSS_SELECTOR, 'app-card')
SELECTOR_PRODUCT_NAME = (By.XPATH, ".//div/div/h4")
SELECTOR_ADD_BTN = (By.XPATH, ".//div/div/button")
SELECTOR_CHECKOUT_BTN = (By.CLASS_NAME, "btn-primary")

SELECTOR_CONFIRM_OPERATION = (By.CLASS_NAME, "btn-success")
SELECTOR_SELECTED_ELEMENT = (By.CSS_SELECTOR, "h4")

#selectores pantalla final, compra producto

SELECTOR_COUNTRY = (By.ID, "country")
SELECTOR_PRESENCE_ELEMENT = (By.LINK_TEXT, "India")
SELECTOR_COUNTRIES_SUGGESTION = (By.CSS_SELECTOR, ".suggestions ul li a")
SELECTOR_CHECKBOX_PURCHASE = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
SELECTOR_PURCHASE_BTN = (By.CLASS_NAME, "btn-success")
SELECTOR_SUCCESS_MESSAGE = (By.CLASS_NAME, "alert-success")
