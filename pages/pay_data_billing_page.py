from pages.pay_data_billing_locators import PayDataBillingPageLocators
from pages.base_page import BasePage


class PayDataBillingPage(BasePage):

    def get_customer_data_label(self):
        customer_data_label = self.find_element(PayDataBillingPageLocators.CUSTOMER_DATA_TEXT).text
        return customer_data_label

    def get_pay_billing_label(self):
        pay_billing_label = self.find_element(PayDataBillingPageLocators.PAY_BILLING_TEXT).text
        return pay_billing_label
