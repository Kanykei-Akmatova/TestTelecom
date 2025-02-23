from selenium.webdriver.common.by import By


class SignInPage:
    def __init__(self, driver):
        self.driver = driver
        self.sign_in_link = (By.XPATH, "//a[contains(text(), 'Sign')]")
        self.username_field = (By.NAME, "username")
        self.password_field = (By.NAME, "password")
        self.submit_button = (By.NAME, "submit")
        self.success_message = (By.XPATH, "//h2[contains(text(), 'Login Successfully')]")

    def wait_and_type_user_name(self, username_password):
        # Implement the logic to wait for the username field and type the username
        self.wait_for_element(self.username_field)  # Assuming `self.username_field` is a defined locator
        self.username_field.send_keys(username_password[0])  # Assuming the first element is the username

    def open_sign_in_page(self):
        self.driver.find_element(*self.sign_in_link).click()

    def enter_credentials(self, username, password):
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)

    def submit_form(self):
        self.driver.find_element(*self.submit_button).click()

    def is_login_successful(self):
        return self.driver.find_element(*self.success_message).is_displayed()

    def submit_login(self):
        pass
