import os
import re
from xlrd import open_workbook
from xml.etree import ElementTree as ElementTree
from log import MyLog as Log
from readconfig import proDir#
#from configHttp import  ConfigHttp
#localConfigHttp = ConfigHttp()
log = Log.get_log()
logger = log.logger


# 从excel文件中读取测试用例
def get_xls(xls_name, sheet_name):
    cls = []
    # get xls file's path
    xlsPath = os.path.join(proDir, "data", xls_name)
    # open xls file
    file = open_workbook(xlsPath)
    # get sheet by name
    sheet = file.sheet_by_name(sheet_name)
    # get one sheet's rows
    nrows = sheet.nrows

    for i in range(nrows):
        #print(sheet.row_values(i)[0])
        if sheet.row_values(i)[0] != u'TC_ID':
            cls.append(sheet.row_values(i))
    return cls

# 从xml文件中读取sql语句
database = {}
def set_xml():
    if len(database) == 0:
        sql_path = os.path.join(proDir, "testFile", "SQL.xml")
        tree = ElementTree.parse(sql_path)
        for db in tree.findall("database"):
            db_name = db.get("name")
            # print(db_name)
            table = {}
            for tb in db.getchildren():
                table_name = tb.get("name")
                # print(table_name)
                sql = {}
                for data in tb.getchildren():
                    sql_id = data.get("id")
                    # print(sql_id)
                    sql[sql_id] = data.text
                table[table_name] = sql
            database[db_name] = table

def get_xml_dict(database_name, table_name):
    set_xml()
    database_dict = database.get(database_name).get(table_name)
    return database_dict

def get_sql(database_name, table_name, sql_id):
    db = get_xml_dict(database_name, table_name)
    sql = db.get(sql_id)
    return sql

def print_msg():
    print("No use")

def check_equal(param1, param2):
    if  param1 == param2:
        return 0
    else:

        return 1

def check_code(statu):
    if re.match("2\d+", str(statu)):
        logger.info("********测试通过********")
        return 0
    elif re.match("3\d+", str(statu)):
        logger.info("********测试失败: 需要重定向********")
        return 1
    elif re.match("4\d+", str(statu)):
        logger.info("********测试失败: 客户端错误********")
        return 1
    elif re.match("5\d+", str(statu)):
        logger.info("********测试失败: 服务器错误********")
        return 1

def check_contents(expected_content, obtained_contents):
     obtained_contents = obtained_contents.replace("\n","").replace("\t","").replace("\r","").replace(" ","").replace("\"","")
     expected_content = expected_content.replace("\n","").replace("\t","").replace("\r","").replace(" ","").replace("\"","")
     if  expected_content in obtained_contents:
         print("[MSG]服务器返回页面验证通过")
         return  0
     else:
         print("[MSG]服务器返回页面验证失败")
         return 1

def write_excel(statu):
    print("begin write excel")
