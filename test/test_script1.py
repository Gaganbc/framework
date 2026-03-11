from generic.base_test import Base_Test
from generic.utility import Utility

from test.xldemo import get_xl_data


class Test_A(Base_Test):

    def test_a1(self):
        print("test_a1")
        print('title is', self.driver.title)
        d=Utility.get_xl_data('./../Data/Akshara.xlsx','Sheet1',1,1)
        print(d)

