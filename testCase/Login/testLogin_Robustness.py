from configHttp import *

class testLogin_Robustness(unittest.TestCase):
    mytest = ConfigHttp()

    def test_R_003(self):
        self.mytest.run("testLogin_Robustness", "1")

    def test_R_004(self):
        self.mytest.run("testLogin_Robustness", "2")

    def test_R_005(self):
        self.mytest.run("testLogin_Robustness", "3")

    def test_R_006(self):
        self.mytest.run("testLogin_Robustness", "4")

    def test_R_007(self):
        self.mytest.run("testLogin_Robustness", "5")

    def test_R_008(self):
        self.mytest.run("testLogin_Robustness", "6")

    def test_R_009(self):
        self.mytest.run("testLogin_Robustness", "7")

    def test_R_010(self):
        self.mytest.run("testLogin_Robustness", "8")

    def test_R_011(self):
        self.mytest.run("testLogin_Robustness", "9")

    def test_R_012(self):
        self.mytest.run("testLogin_Robustness", "10")


