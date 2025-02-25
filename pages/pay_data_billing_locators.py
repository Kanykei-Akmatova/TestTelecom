from selenium.webdriver.common.by import By


class PayDataBillingPageLocators:
    CUSTOMER_DATA_TEXT = (By.XPATH, '//*[@id="main"]/div/h3')
    PAY_BILLING_TEXT = (By.XPATH, '//*[@id="main"]/div/header/h1')
    TARIFF_DATA_TEXT = (By.XPATH, "//*[@id=\"main\"]/div/div/table/tbody/tr[4]/td[2]/b")
    TOTAL_BILL_TEXT = (By.XPATH, "//*[@id=\"main\"]/div/div/table/tbody/tr[6]/td[2]/b")
    USAGE_CHARGES_TEXT = (By.XPATH, "//*[@id=\"main\"]/div/div/table/tbody/tr[5]/td[2]/b")

