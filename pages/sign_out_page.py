from selenium.webdriver.common.by import By

class SignOutPage:
    def __init__(self, driver):
        self.driver = driver
        self.sign_off_button = (By.XPATH, "//a[contains(text(),'Sign Off')]")  # Try XPath
        self.sign_on_link = (By.XPATH, "//a[contains(text(),'Sign-On')]")  # Try XPath

    def logout(self):
        self.driver.find_element(*self.sign_off_button).click()

    def is_logged_out(self):
        return len(self.driver.find_elements(*self.sign_on_link)) > 0