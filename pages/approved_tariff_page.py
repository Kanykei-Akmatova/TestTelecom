from pages.add_tariff_page_locators import AddTariffPageLocators
from pages.base_page import BasePage
from pages.add_customer_page_locators import AddCustomerPageLocators
from resources.constants import MAX_WAIT_INTERVAL


class ApprovedTariffPageLocators:
    TARIFF_PLAN_BOX = None
    ADD_TARIFF_BUTTON = None


class ApprovedTariffPage(BasePage):

    def wait_and_click(self, tariff_plan):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, ApprovedTariffPageLocators.TARIFF_PLAN_BOX).send_keys(
            tariff_plan[0])

    def click_submit_btn(self):
        self.find_element(ApprovedTariffPageLocators.ADD_TARIFF_BUTTON).click()

    def click_add_tariff_button(self):
        pass
