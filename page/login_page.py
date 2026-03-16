import time
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

class LoginPage:
    __username:[str,str]
    __password:[str,str]
    __submit_button:[str,str]
    __error_message:[str,str]

    def __init__(self,driver):
        self.driver=driver
        self.__username=(By.ID,"username")
        self.__password=(By.ID,"password")
        self.__submit_button=(By.ID,"submit")
        self.__error_message=(By.ID,"error")

    def set_username(self,un):
        print("enter username as",un)
        self.driver.find_element(*self.__username).send_keys(un)

    def set_password(self,pw):
        print("enter password as",pw)
        self.driver.find_element(*self.__password).send_keys(pw)

    def click_submit_button(self):
        print("click the submit button",self.__submit_button)
        self.driver.find_element(*self.__submit_button).click()

    def verify_error_message(self, wait: WebDriverWait):
        try:
            wait.until(expected_conditions.visibility_of_element_located(self.__error_message))
            print("error message is displayed")
            print(self.__error_message.text)
            return True
        except:
            print('error message is not displayed')
            return False

# driver = Chrome()
# driver.get("https://practicetestautomation.com/practice-test-login/")
# LoginPage=LoginPage(driver)
# LoginPage.set_username("student")
# LoginPage.set_password("Password123")
# LoginPage.click_submit_button()
# time.sleep(3)