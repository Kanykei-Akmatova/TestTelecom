from pages.pay_data_billing_locators import PayDataBillingPageLocators
from pages.base_page import BasePage


class PayDataBillingPage(BasePage):

    def get_customer_data_label(self):
        customer_data_label = self.find_element(PayDataBillingPageLocators.CUSTOMER_DATA_TEXT).text
        return customer_data_label

    def get_pay_billing_label(self):
        pay_billing_label = self.find_element(PayDataBillingPageLocators.PAY_BILLING_TEXT).text
        return pay_billing_label

    def get_tariff_plan_amount_label(self):
        tariff_plan_amount_label = self.find_element(PayDataBillingPageLocators.TARIFF_DATA_TEXT).text
        return tariff_plan_amount_label

    def get_usage_charges_label(self):
        usage_charges_label = self.find_element(PayDataBillingPageLocators.USAGE_CHARGES_TEXT).text
        return usage_charges_label

    def get_total_bill_label(self):
        total_bill_label = self.find_element(PayDataBillingPageLocators.TOTAL_BILL_TEXT).text
        return total_bill_label
