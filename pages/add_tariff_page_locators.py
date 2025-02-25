from selenium.webdriver.common.by import By


class AddTariffPageLocators:
    INACTIVE_TEXT = (By.XPATH, '//*[@id="main"]/div/p/font')
    CUSTOMER_ID_TEXT_BOX = (By.NAME, "customer_id")
    SUBMIT_BUTTON = (By.NAME, "submit")
    SELECT_TARIFF_PLAN_BUTTON = (By.NAME, "tariff_plan")
    ADD_BUTTON = (By.NAME, "submit")


