from generic.base_test import Base_Test
from page.login_page import LoginPage

class Test_InvalidLogin(Base_Test):
    def test_invalid_login(self):
        #1. enter the invalid username
        login_page=LoginPage(self.driver)
        login_page.set_username("abcd")
        #2. enter the invalid password
        login_page.set_password("123")
        #3. click on submit button
        login_page.click_submit_button()
        print("Current URL:", self.driver.current_url)
        #4. verify that err message is displayed
        result=login_page.verify_error_message_displayed(self.wait)
        assert result




