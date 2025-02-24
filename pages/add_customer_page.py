from pages.base_page import BasePage
from pages.add_customer_page_locators import AddCustomerPageLocators
from resources.constants import MAX_WAIT_INTERVAL


class AddCustomerPage(BasePage):

    def wait_and_click_background_check(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, AddCustomerPageLocators.FIRST_NAME_TEXT_BOX).click()

    def wait_and_type_first_name(self, customer_data):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, AddCustomerPageLocators.FIRST_NAME_TEXT_BOX).send_keys(
            customer_data[0])

    def wait_and_type_last_name(self, customer_data):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, AddCustomerPageLocators.LAST_NAME_TEXT_BOX).send_keys(
            customer_data[1])

    def wait_and_type_email(self, customer_data):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, AddCustomerPageLocators.EMAIL_TEXT_BOX).send_keys(
            customer_data[2])

    def wait_and_type_address(self, customer_data):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, AddCustomerPageLocators.ADDRESS_TEXT_BOX).send_keys(
            customer_data[3])

    def wait_and_type_telephone(self, customer_data):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, AddCustomerPageLocators.TELEPHONE_TEXT_BOX).send_keys(
            customer_data[4])

    def click_submit_btn(self):
        self.find_element(AddCustomerPageLocators.SUBMIT_BUTTON).click()
