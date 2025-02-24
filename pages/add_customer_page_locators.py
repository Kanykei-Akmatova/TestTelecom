from selenium.webdriver.common.by import By


class AddCustomerPageLocators:
    BACKGROUND_RADIO_BOX = (By.NAME, "active")
    FIRST_NAME_TEXT_BOX = (By.ID, "fname")
    LAST_NAME_TEXT_BOX = (By.ID, "lname")
    EMAIL_TEXT_BOX = (By.ID, "email")
    ADDRESS_TEXT_BOX = (By.NAME, "addr")
    TELEPHONE_TEXT_BOX = (By.ID, "telephoneno")
    SUBMIT_BUTTON = (By.NAME, "submit")
