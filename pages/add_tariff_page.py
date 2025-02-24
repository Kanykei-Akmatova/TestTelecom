from pages.add_tariff_page_locators import AddTariffPageLocators
from pages.base_page import BasePage
from pages.add_customer_page_locators import AddCustomerPageLocators
from resources.constants import MAX_WAIT_INTERVAL
from tests.conftest import customer


class AddTariffPage(BasePage):

    def wait_and_add_tariff_button(self):
        self.find_element(AddTariffPageLocators.CUSTOMER_ID_TEXT_BOX).send_keys(
            customer[0])

    def click_submit_btn(self):
        self.find_element(AddTariffPageLocators.SUBMIT_BUTTON).click()
        pass


