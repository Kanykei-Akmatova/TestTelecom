from pages.add_customer_page import AddCustomerPage
from pages.add_tariff_page import AddTariffPage
from pages.customer_access_details_page import CustomerAccessDetailsPage
from pages.index_page import IndexPage
from pages.pay_billing_page import PayBillingPage
from pages.pay_data_billing_page import PayDataBillingPage
from pages.select_tariff_plan_page import SelectTariffPlanPage
from pages.tariff_plan_success_page import TariffPlanSuccessPage
from resources.constants import TEST_SITE_URL, TARIFF_PLAN_ASSIGNED, CUSTOMER_DETAILS_TEXT, PAY_BILLING_TEXT


class TestGuruPage:

    # Test Case 1 ( Add customer)
    def test_add_customer(self, driver, customer_data):
        index_page = IndexPage(driver)
        index_page.navigate_to(TEST_SITE_URL)
        index_page.wait_and_click_add_customer_button()

        add_customer_page = AddCustomerPage(driver)
        add_customer_page.wait_and_click_background_check()
        add_customer_page.wait_and_type_first_name(customer_data)
        add_customer_page.wait_and_type_last_name(customer_data)
        add_customer_page.wait_and_type_email(customer_data)
        add_customer_page.wait_and_type_address(customer_data)
        add_customer_page.wait_and_type_telephone(customer_data)
        add_customer_page.click_submit_btn()

        customer_access_details_page = CustomerAccessDetailsPage(driver)
        customer_id_txt = customer_access_details_page.get_customer_id()
        assert customer_id_txt.strip(), "Customer registration failed! Customer ID is empty."

    # Test Case 2 ( Add tariff Page)
    def test_add_tariff_plan(self, driver, customer):
        index_page = IndexPage(driver)
        index_page.navigate_to(TEST_SITE_URL)
        index_page.wait_and_click_add_customer_tariff_button()

        add_tariff_page = AddTariffPage(driver)
        add_tariff_page.wait_and_enter_customer_id(customer)
        add_tariff_page.click_submit_btn()

        select_tariff_plan_page = SelectTariffPlanPage(driver)
        select_tariff_plan_page.click_add_tariff_plan()

        tariff_plan_success_page = TariffPlanSuccessPage(driver)
        lbl_assigned_txt = tariff_plan_success_page.get_assigned_label()
        assert lbl_assigned_txt.__contains__(TARIFF_PLAN_ASSIGNED), "Congratulations Tariff Plan assigned failed!"

    # Test Case 3 (Pay Billing)
    def test_pay_billing(self, driver, customer):
        index_page = IndexPage(driver)
        index_page.navigate_to(TEST_SITE_URL)
        index_page.wait_and_click_pay_billing_button()

        pay_billing_page = PayBillingPage(driver)
        pay_billing_page.wait_and_enter_customer_id(customer)
        pay_billing_page.click_submit_btn()

        pay_data_billing_page = PayDataBillingPage(driver)
        customer_data_label = pay_data_billing_page.get_customer_data_label()
        pay_billing_label = pay_data_billing_page.get_pay_billing_label()

        assert customer_data_label.__contains__(CUSTOMER_DETAILS_TEXT), "Customer details are incorrect!"
        assert pay_billing_label.__contains__(PAY_BILLING_TEXT), "Pay billing label is missing!"
