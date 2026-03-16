from generic.base_test import Base_Test
from page.login_page import LoginPage
from page.home_page import HomePage
from generic.utility import Utility

class Test_valid_login(Base_Test):

    def test_valid_login(self):
        #read data from xl
        un=Utility.get_xl_data(self.xl_path,'valid_login',2,1)
        pw=Utility.get_xl_data(self.xl_path,'valid_login',2,2)
        #1. enter valid username
        login_page = LoginPage(self.driver)
        login_page.set_username(un)
        #2. enter valid password
        login_page.set_password(pw)
        #3. click on submit button
        login_page.click_submit_button()
        #4. verify that home page is displayed
        home_page = HomePage(self.driver)
        result=home_page.verify_home_page_is_displayed(self.wait)
        assert result
