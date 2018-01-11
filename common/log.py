import logging
from datetime import datetime
import threading
import os
import sys
from readconfig import proDir

global logPath, resultPath

class Log:
    logPath=""
    def __init__(self):
        self.resultPath = os.path.join(proDir, "result")
        # 检查报告文件夹存在与否
        if not os.path.exists(self.resultPath):
            os.mkdir(self.resultPath)

        # 定义文件名(时间)
        self.logPath = os.path.join(self.resultPath, str(datetime.now().strftime("%Y%m%d%H%M%S")))
        # 创建报告文件
        if not os.path.exists(self.logPath):
            os.mkdir(self.logPath)

        # 定义日志
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)

        # 日志文件
        handler = logging.FileHandler(os.path.join(self.logPath, "output.log"))
        # defined formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # defined formatter
        handler.setFormatter(formatter)
        # add handler
        self.logger.addHandler(handler)

    def get_result(self):
        return self.logPath

    def get_report_path(self):
        return(self.logPath)


class MyLog:
    log = None
    mutex = threading.Lock()

    def __init__(self):
        pass

    @staticmethod
    def get_log():

        if MyLog.log is None:
            MyLog.mutex.acquire()
            MyLog.log = Log()
            MyLog.mutex.release()

        return MyLog.log
