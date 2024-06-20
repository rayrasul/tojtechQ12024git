from selenium.webdriver.common.by import By


class ShopPage:
    add_to_cart_button = (By.XPATH, "(//span[text()='Add to cart'])[1]")
    cart_button = (By.CLASS_NAME, "wc-block-mini-cart__button ")
    view_my_cart_button = (By.XPATH, "//span[contains(text(), 'View')]")
    checkout_page_button = (By.CLASS_NAME, "wc-block-components-button")

    def __init__(self, driver):
        self.driver = driver

    def get_add_to_cart_button(self):
        return self.driver.find_element(*ShopPage.add_to_cart_button)

    def get_cart_button(self):
        return self.driver.find_element(*ShopPage.cart_button)

    def get_view_my_cart_button(self):
        return self.driver.find_element(*ShopPage.view_my_cart_button)

    def get_checkout_page_button(self):
        return self.driver.find_element(*ShopPage.checkout_page_button)
