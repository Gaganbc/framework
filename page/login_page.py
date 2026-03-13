
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome

class LoginPage:
    __username:[str,str]
    __password:[str,str]
    __submit_button:[str,str]


    def __init__(self,driver):
        self.driver=driver
        self.__username=(By.ID,"username")
        self.__password=(By.ID,"password")
        self.__submit_button=(By.ID,"submit")

    def set_username(self,un):
        self.driver.find_element(*self.__username).send_keys(un)

    def set_password(self,pw):
        self.driver.find_element(*self.__password).send_keys(pw)

    def click_submit_button(self):
        self.driver.find_element(*self.__submit_button).click()

driver = Chrome()
driver.get("https://practicetestautomation.com/practice-test-login/")
LoginPage=LoginPage(driver)
LoginPage.set_username("student")
LoginPage.set_password("Password123")
LoginPage.click_submit_button()
time.sleep(3)