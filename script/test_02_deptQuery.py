import logging
import unittest
from parameterized import parameterized
import app
import utils
from api.queryApi import QueryApi


class TestDeptQuery(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 调用登陆成功的方法 完成token的初始化
        utils.login_success()
        # 实例化查询部门的接口
        cls.query_api = QueryApi()

        # 定义变量,查询部门的请求头
        cls.query_headers = {"Authorization": app.token}

    query_data = utils.read_data(app.BASE_DIR + "/data/query.json")

    # 参数化增加部门的方法
    @parameterized.expand(query_data)
    def test_01_dept_add(self, params, status, code, message):
        response = self.query_api.query(params_param=params, headers_param=self.query_headers)
        logging.info("查询部门后返回的响应结果为:{}".format(response.json()))
        self.assertEqual(status, response.status_code)
        self.assertEqual(code, response.json().get("code"))
        self.assertEqual(message, response.json().get("message"))
