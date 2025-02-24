from selenium.webdriver.common.by import By


class PayBillingPageLocators:
    ENTER_YOUR_CUSTOMER_ID_BOX = (By.XPATH, '//*[@id="customer_id"]')
    SUBMIT_BUTTON = (By.NAME, "submit")
