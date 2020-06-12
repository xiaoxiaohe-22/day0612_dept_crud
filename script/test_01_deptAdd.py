import logging
import unittest
from parameterized import parameterized
import app
import utils
from api.deptAddApi import DeptAddApi


class TestDeptAdd(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 调用登陆成功的方法 完成token的初始化
        utils.login_success()
        # 实例化添加部门的接口
        cls.dept_add_api = DeptAddApi()
        # 定义变量,添加部门的请求体
        cls.add_headers = {"Content-Type": "application/json", "Authorization": app.token}

    add_data = utils.read_data(app.BASE_DIR + "/data/add.json")

    # 参数化增加部门的方法
    @parameterized.expand(add_data)
    def test_01_dept_add(self, request_body, status, code, message):
        response = self.dept_add_api.dept_add(headers_data=self.add_headers, json_data=request_body)
        logging.info("添加部门后的响应结果为:{}".format(response.json()))
        self.assertEqual(status, response.status_code)
        self.assertEqual(code, response.json().get("code"))
        self.assertEqual(message, response.json().get("message"))
