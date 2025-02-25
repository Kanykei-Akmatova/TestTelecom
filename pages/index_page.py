from pages.add_tariff_page_locators import AddTariffPageLocators
from pages.base_page import BasePage
from pages.index_page_locators import IndexPageLocators
from pages.pay_billing_page_locators import PayBillingPageLocators
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
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, AddTariffPageLocators.SELECT_TARIFF_PLAN_BUTTON).click()

    def wait_and_click_submit_button(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,
                                              PayBillingPageLocators.ENTER_YOUR_CUSTOMER_ID_BOX).click()

    def wait_and_click_pay_billing_button(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, IndexPageLocators.PAY_BILLING_LINK).click()

    def wait_and_get_index_image_src(self):
        index_image = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, IndexPageLocators.INDEX_IMAGE_LINK)
        return index_image.get_attribute("src")
