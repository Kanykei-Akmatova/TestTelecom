from selenium.webdriver.common.by import By


class PayDataBillingPageLocators:
    CUSTOMER_DATA_TEXT = (By.XPATH, '//*[@id="main"]/div/h3')
    PAY_BILLING_TEXT = (By.XPATH, '//*[@id="main"]/div/header/h1')

    FIRST_NAME_TEXT_BOX = (By.ID, "fname")
