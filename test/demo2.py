import time
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome


driver = Chrome()
driver.get("https://practicetestautomation.com/practice-test-login/")
driver.maximize_window()
a=By.ID
b="username"
tuple1=(a,b)
# list1=[a,b]
# driver.find_element(list1[0],list1[1]).send_keys("student")
driver.find_element(*tuple1).send_keys("student")
# driver.find_element(*list1).send_keys("student")
time.sleep(2)
driver.quit()