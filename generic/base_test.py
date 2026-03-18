import os
import pytest
from selenium.webdriver import Chrome
from selenium.webdriver import Safari
from selenium.webdriver.support.ui import WebDriverWait
from generic.utility import Utility
from selenium.webdriver import Remote
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.safari.options import Options as SafariOptions


class Base_Test:

    @pytest.fixture(autouse=True, params=['Chrome','Safari'])
    def precondition(self, request):
        BROWSER=request.param
        # path='config.properties'
        generic=os.path.dirname(__file__)
        path=generic+'/../config.properties'
        self.xl_path=generic+'/../Data/Akshara.xlsx'
        print('-----',path,'-----')
        GRID=Utility.get_property(path,'GRID')
        GRIDURL=Utility.get_property(path,'GRIDURL')
        # BROWSER=Utility.get_property(path,'BROWSER')
        APPURL = Utility.get_property(path, 'APPURL')
        ITO = Utility.get_property(path, 'ITO')
        ETO = Utility.get_property(path, 'ETO')

        if GRID=='yes':
            print('using grid, open the browser in remote system')
            if BROWSER == 'Chrome':
                print("open the Chrome browser in remote system")
                Chrome_Options = ChromeOptions()
                self.driver = Remote(GRIDURL,options=Chrome_Options)
            elif BROWSER == 'Safari':
                print("open the Safari browser in remote system")
                Safari_Options = SafariOptions()
                self.driver = Remote(GRIDURL,options= Safari_Options)
            else:
                print("error")


        else:
            print('not using grid, open browser in local system')

        if BROWSER == 'Chrome':
            print("open the Chrome browser in local system")
            self.driver = Chrome()
        elif BROWSER == 'Safari' :
            print("open the Safari browser in local system")
            self.driver = Safari()
        else:
            print("error")

        print("enter the url", APPURL)
        self.driver.get(APPURL)
        print("maximize the browser")
        self.driver.maximize_window()
        print("set ITO",ITO)
        self.driver.implicitly_wait(ITO)
        print("set ETO",ETO)
        self.wait=WebDriverWait(self.driver, ETO)

    @pytest.fixture(autouse=True)
    def postcondition(self):
        yield
        print("close the browser")
        self.driver.close()