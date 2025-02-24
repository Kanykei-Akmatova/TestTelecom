from pages.add_tariff_success_locators_page import AddTariffSuccessPageLocators
from pages.base_page import BasePage
from pages.customer_access_details_page_locators import CustomerAccessDetailsPageLocators
from resources.constants import MAX_WAIT_INTERVAL

class AddTariffSuccessPage(BasePage):
    def get_customer_id(self):
        lbl_customer_id_txt = self.explicitly_wait_and_find_element(
            MAX_WAIT_INTERVAL, AddTariffSuccessPageLocators.CUSTOMER_ID_TEXT).text
        return lbl_customer_id_txt

