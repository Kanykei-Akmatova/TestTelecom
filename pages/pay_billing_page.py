from selenium.webdriver.common.by import By

from pages.pay_billing_page_locators import PayBillingPageLocators
from pages.base_page import BasePage
from resources.constants import MAX_WAIT_INTERVAL
from pages.base_page import BasePage
from pages.pay_billing_page_locators import PayBillingPageLocators


class PayBillingPage(BasePage):

    def wait_and_enter_customer_id(self, customer):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,
                                              PayBillingPageLocators.ENTER_YOUR_CUSTOMER_ID_BOX).send_keys(customer[0])

    def click_submit_btn(self):
        self.find_element(PayBillingPageLocators.SUBMIT_BUTTON).click()



