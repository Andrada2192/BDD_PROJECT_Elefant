import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from browser import Browser


class TestSearchBar(Browser):
    SEARCH_BAR = (By.CSS_SELECTOR, 'input[name="SearchTerm"]')
    SEARCH_BUTTON = (By.CSS_SELECTOR, 'button[name="search"]')
    PRODUCT_LIST = (By.CSS_SELECTOR, 'body .search-product-list .product-list')
    ERROR_MESSAGE = (By.CSS_SELECTOR, 'h1.h2')

    def navigate_to_login_page(self):
        self.driver.get("https://www.elefant.ro/")
        time.sleep(5)

        try:
            cookie_button = self.driver.find_element(By.CSS_SELECTOR, 'button#CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll')
            if cookie_button.is_displayed():
                cookie_button.click()
        except NoSuchElementException:
            pass


    def search_bar_field(self, item):
        self.driver.find_element(*self.SEARCH_BAR).send_keys(item)

    def click_search_button(self):
        self.driver.find_element(*self.SEARCH_BUTTON).click()

    def product_list(self):
        return self.driver.find_element(*self.PRODUCT_LIST).find_elements(By.CSS_SELECTOR, '.product-title')

    def get_error_message(self):
        return self.driver.find_element(*self.ERROR_MESSAGE).text

