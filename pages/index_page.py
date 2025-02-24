from pages.base_page import BasePage
from pages.index_page_locators import IndexPageLocators
from resources.constants import MAX_WAIT_INTERVAL


class IndexPage(BasePage):

    def wait_and_click_register_button(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, IndexPageLocators.REGISTER_LINK).click()

    def wait_and_click_sign_in_button(self):
        pass

    def wait_and_click_add_customer_button(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, IndexPageLocators.ADD_CUSTOMER_LINK).click()

    # def wait_and_click_submit_btn(self):
    #     pass

    # def wait_and_click_approve_tariff_button(self):
    # self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, IndexPageLocators.SELECT_RADIO_BUTTON_LINK).click()

    # def wait_and_click_add_tariff_plan_btn(self):
    # pass
