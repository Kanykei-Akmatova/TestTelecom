from pages.add_tariff_page_locators import AddTariffPageLocators
from pages.base_page import BasePage
from pages.index_page_locators import IndexPageLocators
from resources.constants import MAX_WAIT_INTERVAL


class IndexPage(BasePage):

    def wait_and_click_register_button(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, IndexPageLocators.REGISTER_LINK).click()

    def wait_and_click_add_customer_button(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, IndexPageLocators.ADD_CUSTOMER_LINK).click()

    def wait_and_click_add_customer_tariff_button(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, IndexPageLocators.ADD_CUSTOMER_TARIFF_LINK).click()

    def wait_and_add_tariff_button(self, customer):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, AddTariffPageLocators.CUSTOMER_ID_TEXT_BOX).click()

    def wait_and_click_submit_btn(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, AddTariffPageLocators.CUSTOMER_ID_TEXT_BOX).click()

    def wait_and_click_select_radio_button(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, AddTariffPageLocators.TARIFF_PLAN_LINK).click()
