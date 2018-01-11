import requests
import ssl
import operator
import unittest
ssl._create_default_https_context = ssl._create_unverified_context
from  readconfig import ReadConfig
from log import MyLog as Log
from common.functions import *
import json
localReadConfig = ReadConfig()

class ConfigHttp:
    def __init__(self):

        global timeout
        #host = #localReadConfig.get_http("baseurl")
        #port = localReadConfig.get_http("port")
        #timeout = localReadConfig.get_http("timeout")
        #for i in case_array:
        #    print(i)
        #    print("OKOK")
        self.host = {}
        self.log = Log.get_log()
        self.logger = self.log.logger
        self.headers = {}
        self.params = {}
        self.data = {


        }
        self.url = {}
        self.files = {}
        self.timeout = 0

    def run(self, sheet_name, tc_id):
        case_array =get_xls("testcases.xlsx", sheet_name)
        #print(type(case_array))
        #print(case_arra
        tc_id=int(tc_id)-1
        print("\n#用例编号:",case_array[tc_id][0])
        print("#用例描述:", case_array[tc_id][1])

        self.host =  case_array[tc_id][3]
        self.set_url(case_array[tc_id][4])
        self.set_headers(case_array[tc_id][5])
        self.set_params(case_array[tc_id][6])
        self.set_data(case_array[tc_id][7])
        self.set_files(case_array[tc_id][8])
        self.timeout = float((case_array[tc_id][9]))
        self.contents = case_array[tc_id][10]
        if case_array[tc_id][2] == "post":
            #self.headers=self.headers.replace("\n","")
            #self.headers=self.headers.replace("","")
            self.headers=json.loads(self.headers)
            result=self.post()#
            print("#期待返回码：200","服务器实际返回码:", result.status_code,)
            print("#期待返回关键字:",self.contents,"服务器实际返回内容:", result.text)
            if check_code(result.status_code) == 0:
               assert check_contents(self.contents, result.text) == 0
            else:
               assert check_code(result.status_code) == 0
               ''''''
        elif case_array[tc_id][2] == "get":
            result = self.get()
            print("#期待返回码：200","服务器实际返回码:", result.status_code,)
            print("#期待返回关键字:",self.contents,"服务器实际返回内容:", result.text)
            if check_code(result.status_code)==0:
                assert  check_contents(self.contents, result.text)==0
            else:
                assert check_code(result.status_code)==0
                ''''''
        else:
            print("Unkown")

    def set_url(self, url):
        self.url = self.host + url

    def set_headers(self, header):
        self.headers = header

    def set_params(self, param):
        self.params = param

    def set_data(self, data):
        self.data = data

    def set_files(self, file):
        self.files = file

    # 定义get方法
    def get(self):
        try:
            response = requests.get(self.url, params=self.params, headers=self.headers, timeout=self.timeout)
            response.encoding="UTF-8"
            #response.raise_for_status()
        except TimeoutError:
            self.logger.error("Time out!")
            return None
        else:
            return response

    # 定义post方法
    def post(self):
        try:
            response = requests.post(self.url, headers=self.headers, data=self.data, files=self.files, timeout=self.timeout)
            response.encoding = "UTF-8"
            # response.raise_for_status()
        except TimeoutError:
            self.logger.error("Time out!")
            return None
        else:            return response




