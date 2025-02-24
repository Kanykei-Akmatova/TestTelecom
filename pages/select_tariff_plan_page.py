from pages.select_tariff_plan_page_locators import SelectTariffPlanPageLocators
from resources.constants import MAX_WAIT_INTERVAL
from pages.base_page import BasePage
from resources.constants import MAX_WAIT_INTERVAL


class SelectTariffPlanPage(BasePage):

    def click_add_tariff_plan(self):
        self.find_element(SelectTariffPlanPageLocators.ADD_BUTTON).click()
