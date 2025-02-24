from selenium.webdriver.common.by import By


class CustomerAccessDetailsPageLocators:
    CUSTOMER_ID_TEXT = (By.XPATH, "//*[@id=\"main\"]/div/div/table/tbody/tr[1]/td[2]/h3")
    ADD_TARIFF_ID_TEXT = (By.NAME, "//*[@id=\"customer_id\"]")


