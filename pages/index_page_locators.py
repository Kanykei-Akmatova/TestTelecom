from selenium.webdriver.common.by import By


class IndexPageLocators:
    CUSTOMER_ID_TEXT_BOX_LINK =(By.NAME, "//*[@id=\"customer_id\"]")
    REGISTER_LINK = (By.XPATH, "//a[text()='REGISTER']")
    OK_BUTTON = (By.NAME, "btn_ok")
    ADD_CUSTOMER_LINK = (By.XPATH, "//*[@id=\"one\"]/div/div[1]/div[1]/h3/a")
    ADD_CUSTOMER_TARIFF_LINK = (By.XPATH, "//*[@id=\"one\"]/div/div[1]/div[2]/h3/a")
    SELECT_TARIFF_PLAN_BUTTON = (By.NAME, "tariff_plan")

    # ENTER_CUSTOMER_ID_LINK = (By.NAME, "//*[@id=\"customer_id\"]")
    # SELECT_RADIO_BUTTON_LINK = (By.NAME, "tariff_plan")
