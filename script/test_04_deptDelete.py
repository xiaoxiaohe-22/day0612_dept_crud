import logging
import unittest
from parameterized import parameterized
import app
import utils
from api.deleteApi import DeleteApi


class TestDeptDelete(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 调用登陆成功的方法 完成token的初始化
        utils.login_success()
        # 实例化修改部门的接口
        cls.delete_api = DeleteApi()

        # 定义变量,查询部门的请求头
        cls.delete_headers = {"Authorization": app.token}

    delete_data = utils.read_data(app.BASE_DIR + "/data/delete.json")

    # 参数化增加部门的方法
    @parameterized.expand(delete_data)
    def test_01_dept_add(self, params, status, code, message):
        response = self.delete_api.delete(params_param=params, headers_param=self.delete_headers)
        logging.info("删除部门后返回的响应结果为:{}".format(response.json()))
        self.assertEqual(status, response.status_code)
        self.assertEqual(code, response.json().get("code"))
        self.assertEqual(message, response.json().get("message"))
