import unittest
from utils.HTMLTestRunner_PY3 import HTMLTestRunner
from log import *
from configEmail import MyEmail as email


log = MyLog.get_log()
logger = log.logger

class interface_test:
    caseListFile="TC_list.txt"
    caseList=[]

    def set_case_list(self):
           fb = open(self.caseListFile)
           for value in fb.readlines():
               data = str(value)
               if data != '' and not data.startswith("#"):
                   self.caseList.append(data.replace("\n", ""))
           fb.close()

    def set_case_suite(self):
            self.set_case_list()
            test_suite = unittest.TestSuite()
            suite_model = []

            for case in self.caseList:

                Last_folder = case.split("/")[0]
                case_folder = os.path.join(proDir, "testCase")
                case_path = os.path.join(case_folder, Last_folder)
                case_name = case.split("/")[-1]
                discover = unittest.defaultTestLoader.discover(case_path, pattern=case_name + '.py', top_level_dir=None)
                suite_model.append(discover)

            if len(suite_model) > 0:
                for suite in suite_model:
                    for test_name in suite:
                        test_suite.addTest(test_name)
            else:
                return None
            return test_suite

    def run(self, report_folder,on_off):
            try:
                suit =self.set_case_suite()

                if suit is not None:
                    logger.info("********TEST START********")
                    fp = open(report_folder+"\\report.html", 'wb')
                    runner = HTMLTestRunner(stream=fp, title='接口测试报告', description='接口测试报告')
                    runner.run(suit)
                else:
                    logger.info("Have no case to test.")
            except Exception as ex:
                logger.error(str(ex))
            finally:
                logger.info("*********TEST END*********")

            #邮件模块
            if int(on_off) == 0:
                email.get_email().send_email()
            elif int(on_off) == 1:
                logger.info("Doesn't send report email.")
            else:
                logger.info("Unknow state.")

if __name__ == '__main__':

    mylog= Log()
    my_test = interface_test()
    my_test.run(mylog.get_result(),0)