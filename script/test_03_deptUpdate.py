import logging
from parameterized import parameterized
import unittest
import app
import utils
from api.updateApi import UpdateApi


class TestDeptUpdate(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 调用登陆成功的方法 完成token的初始化
        utils.login_success()
        # 实例化修改部门的接口
        cls.update_api = UpdateApi()

        # 定义变量,查询部门的请求头
        cls.update_headers = {"Content-Type": "application/json", "Authorization": app.token}

    update_data = utils.read_data(app.BASE_DIR + "/data/update.json")

    # 参数化增加部门的方法
    @parameterized.expand(update_data)
    def test_01_dept_add(self, params, status, code, message,json_param):
        response = self.update_api.update(params_param=params, headers_param=self.update_headers,json_data=json_param)
        logging.info("修改部门后返回的响应结果为:{}".format(response.json()))
        self.assertEqual(status, response.status_code)
        self.assertEqual(code, response.json().get("code"))
        self.assertEqual(message, response.json().get("message"))
