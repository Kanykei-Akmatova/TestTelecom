from pages.base_page import BasePage
from pages.tariff_plan_success_locators import TariffPlanSuccessPageLocators


class TariffPlanSuccessPage(BasePage):

    def get_assigned_label(self):
        lbl_assigned_txt = self.find_element(TariffPlanSuccessPageLocators.ASSIGNED_SUCCESS_LBL).text
        return lbl_assigned_txt
