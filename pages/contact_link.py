import os
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from browser import Browser


class ContactLink(Browser):
    # CONTACT_LINK = (By.LINK_TEXT, 'Contact')
    ORDER_NUMBER_FIELD = (By.CSS_SELECTOR, 'input[name="order_number"]')
    CONTACT_DESCRIPTION = (By.CSS_SELECTOR, 'textarea[name="contact_description"]')
    UPLOAD_FILES = (By.CSS_SELECTOR, 'div[class="o-exp-upload-title"]')
    SUBMIT_BUTTON = (By.XPATH, '//div[contains(text(), "Trimite")]')
    LIST_ERRORS = (By.CSS_SELECTOR, 'div.o-lead-form')


    def navigate_to_contact_page(self):
        self.driver.get('https://www.elefant.ro/helpdesk/contact-us')


    def enter_order_number(self, order_number):
        self.driver.find_element(*self.ORDER_NUMBER_FIELD).send_keys(order_number)


    def enter_contact_description(self, description):
        description_element = self.driver.find_element(*self.CONTACT_DESCRIPTION)
        action = ActionChains(self.driver)
        action.context_click(description_element).send_keys(description)


    def click_on_upload_files(self):
        directory = r"C:\Users\andra\Downloads"
        file = "clipart1069648.png"
        complete_path = os.path.join(directory, file)


    def click_on_submit_button(self):
        self.driver.find_element(*self.SUBMIT_BUTTON).click()


    def get_error_messages(self):
        return self.driver.find_element(*self.LIST_ERRORS).find_elements(By.CSS_SELECTOR, '.omni-error-AG29978')






