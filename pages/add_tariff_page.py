from pages.add_tariff_page_locators import AddTariffPageLocators
from pages.base_page import BasePage
from resources.constants import MAX_WAIT_INTERVAL


class AddTariffPage(BasePage):
    def wait_and_enter_customer_id(self, customer):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, AddTariffPageLocators.CUSTOMER_ID_TEXT_BOX).send_keys(
            customer[0])

    def click_submit_btn(self):
        self.find_element(AddTariffPageLocators.SUBMIT_BUTTON).click()

    def get_inactive_label_value(self):
        inactive_value = self.find_element(AddTariffPageLocators.INACTIVE_TEXT).text
        return inactive_value

    def get_inactive_label_color(self):
        index_image = self.find_element(AddTariffPageLocators.INACTIVE_TEXT)
        return index_image.get_attribute("color")


