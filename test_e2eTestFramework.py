from PythonFramework.page_objects.login import LoginPage
from PythonFramework.page_objects.purchase import PurchasePage
from PythonFramework.page_objects.shop import ShopPage


def test_e2e(browserInstance):
    driver = browserInstance
    loginPage = LoginPage(driver)
    loginPage.login()

    shopPage = ShopPage(driver)
    shopPage.selectProduct()
    shopPage.checkout()

    purchase = PurchasePage(driver)
    purchase.executePurchase()
    purchase.validateMessage()