
from configHttp import *

class testLogin_Normal(unittest.TestCase):
    mytest = ConfigHttp()

    def test_N_001(self):
        try:
            self.mytest.run("testLogin_Normal", "1")
        except:
            self.mytest.run("dbserver", "1")
            ''''''

    def test_N_002(self):
        try:
            self.mytest.run("testLogin_Normal", "2")
        except:
            self.mytest.run("dbserver", "1")


