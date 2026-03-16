from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

class  HomePage:
    __logout:[str,str]

    def __init__(self,driver):
        self.driver = driver
        self.__logout=(By.XPATH, "//a[text()='Log out']")

    def verify_home_page_is_displayed(self,wait: WebDriverWait):
        try:
            wait.until(expected_conditions.visibility_of_element_located(self.__logout))
            print('Home Page is displayed')
            return True
        except:
            print('Home Page is NOT displayed')
            return False