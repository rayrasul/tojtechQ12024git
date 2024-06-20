from time import sleep

import self
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from pageObjects.shoppage import ShopPage
from utilities.baseclass import BaseClass


class TestEndToEnd(BaseClass):
    def test_end_to_end(self):
        shop_page = ShopPage(self.driver)
        shop_page.get_add_to_cart_button().click()
        shop_page.get_cart_button().click()
        shop_page.get_checkout_page_button().click()
        sleep(3)
        list_of_countries = self.driver.find_elements(By.CSS_SELECTOR, "#components-form-token-input-0")
        for country in list_of_countries:
            if country.text == "United Kingdom (UK)":
                country.click()
                break

        self.driver.quit()
        print("this is a newly created message for git session")

