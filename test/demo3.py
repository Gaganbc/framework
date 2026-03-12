import time
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
class LoginPage:
    username:[str]  #declaration

    def __init__(self,driver):
        self.driver = driver
        self.username = (By.ID,'username')  # initialization

    def set_username(self,un):
        self.driver.find_element(*self.username).send_keys(un) #utilization

driver = Chrome()
driver.get("https://practicetestautomation.com/practice-test-login/")
time.sleep(3)
LoginPage=LoginPage(driver)
LoginPage.set_username("student")
time.sleep(3)