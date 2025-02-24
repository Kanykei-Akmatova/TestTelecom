import time

from pages.add_customer_page import AddCustomerPage
from pages.customer_access_details_page import CustomerAccessDetailsPage
from pages.index_page import IndexPage
from resources.constants import TEST_SITE_URL


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
    # def test_add_tariff_plan(self, driver, customer):
    #     index_page = IndexPage(driver)
    #     index_page.navigate_to(TEST_SITE_URL)
    #     index_page.wait_and_click_add_customer_button()
    #
    #     add_tariff_page = AddTariffPage(driver)
    #     add_tariff_page.wait_and_add_tariff_button()
    #     add_tariff_page.click_submit_btn()
    #
    #     add_tariff_success_page = AddTariffSuccessPage(driver)
    #     customer_id_txt = add_tariff_success_page.get_customer_id()
    #     assert customer_id_txt.strip(), "Approved Tariff failed!"

    # Test Case 3 (Approved Tariff Plans)
    #def test_approved_tariff_plan(self, driver, tariff_plan):
        #index_page = IndexPage(driver)
        #index_page.navigate_to(TEST_SITE_URL)
        #index_page.wait_and_click_add_tariff_button()

        #approved_tariff_page = ApprovedTariffPage(driver)
        #approved_tariff_page.wait_and_click(tariff_plan)
        #approved_tariff_page.click_add_tariff_button()

        #customer_access_details_page = CustomerAccessDetailsPage(driver)
        #customer_id_txt = customer_access_details_page.get_customer_id()
        #assert customer_id_txt.strip(), "Add Tariff Plan to Customer failed!"
