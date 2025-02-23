
from pages.index_page import IndexPage
from pages.register_page import RegisterPage
from pages.register_success_page import RegisterSuccessPage
from pages.sign_in_page import SignInPage
from pages.sign_out_page import SignOutPage
from resources.constants import TEST_SITE_URL



class TestGuruPage:

# Test Case 1 ( Registering the user)
    def test_add_customer(self, driver, username_password):
        index_page = IndexPage(driver)

        index_page.navigate_to(TEST_SITE_URL)
        index_page.wait_and_click_register_button()

        register_page = RegisterPage(driver)
        register_page.wait_and_type_user_name(username_password)
        register_page.type_password(username_password)
        register_page.type_confirm_password(username_password)
        register_page.click_submit_btn()

        register_success_page = RegisterSuccessPage(driver)
        register_success_lbl = register_success_page.get_register_success_label()
        assert register_success_lbl.__contains__(username_password[0]), "User registration failed!"

    # Test Case 1 ( Registering the user)
    # def test_register_new_user(self, driver, username_password):
    #     index_page = IndexPage(driver)
    #
    #     index_page.navigate_to(TEST_SITE_URL)
    #     index_page.wait_and_click_register_button()
    #
    #     register_page = RegisterPage(driver)
    #     register_page.wait_and_type_user_name(username_password)
    #     register_page.type_password(username_password)
    #     register_page.type_confirm_password(username_password)
    #     register_page.click_submit_btn()
    #
    #     register_success_page = RegisterSuccessPage(driver)
    #     register_success_lbl = register_success_page.get_register_success_label()
    #     assert register_success_lbl.__contains__(username_password[0]), "User registration failed!"

    #def test_sign_in(self, driver, username_password):
        #sign_in_page = SignInPage(driver)
        #sign_in_page.open_sign_in_page()
        #sign_in_page.enter_credentials(username_password[0], username_password[1])
        #sign_in_page.submit_login()
        #register_success_page = RegisterSuccessPage(driver)
        #register_success_lbl = register_success_page.get_register_success_label()
        #assert register_success_lbl.__contains__(username_password[0]), "Login failed, 'Sign-In Successfully' "

            # Test Case 3 (Sign out)
    #def test_sign_out(self, driver, username_password):
        #sign_in_page = SignInPage(driver)
        #sign_out_page = SignOutPage(driver)
       # sign_in_page.open_sign_in_page()
        #sign_in_page.enter_credentials(username_password[0], username_password[1])
        #sign_in_page.submit_login()
       # sign_out_page.logout()
       # assert sign_out_page.is_logged_out(), "Logout failed, 'Sign-In' link not found"


