import json

import app
from api.loginApi import LoginApi


# 定义登陆的方法 完成token的初始化
def login_success():
    login_api = LoginApi()
    headers = {"Content-Type": "application/json"}
    with open(file=app.BASE_DIR + "/data/login_data.json", encoding="utf-8") as f:
        jsondata = json.load(f).get("success_login")
    login_api.login(headers_data=headers, json_data=jsondata)


# 定义读取数据的方法
def read_data(file_name):
    with open(file=file_name, encoding="utf-8") as f:
        json_load = json.load(f)
        login_list = []
        for ele in list(json_load.values()):
            login_list.append(tuple(ele.values()))
        return login_list


# 定义crud通用的断言方法
def assert_common(self,status,code,message,response):
    self.assertEqual(status, response.status_code)
    self.assertEqual(code, response.json().get("code"))
    self.assertEqual(message, response.json().get("message"))