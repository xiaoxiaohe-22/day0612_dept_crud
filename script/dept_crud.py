import logging
import unittest

from parameterized import parameterized

import app
import utils
from api.deleteApi import DeleteApi
from api.deptAddApi import DeptAddApi
from api.queryApi import QueryApi
from api.updateApi import UpdateApi


class TestDeptCRUD(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 调用登陆成功的方法 完成token的初始化
        utils.login_success()
        # 分别实例化增查改删接口
        cls.add_api = DeptAddApi()
        cls.query_api = QueryApi()
        cls.update_api = UpdateApi()
        cls.delete_api = DeleteApi()

    @parameterized.expand(utils.read_data(app.BASE_DIR + "/data/dept_crud.json"))
    def test_dept_crud(self,request_body,status,code,message,update_request_body):
        headers_data_add = {"Content-Type": "application/json", "Authorization": app.token}
        # 调用增加部门接口完成增加部门
        response = self.add_api.dept_add(headers_data=headers_data_add, json_data=request_body)
        # 将增加成功的部门id存入全局变量gl_dept_id里面
        app.gl_dep_id = response.json().get("data").get("id")
        logging.info("增加部门后返回的部门id为:{}".format(app.gl_dep_id))
        logging.info("增加部门后返回的结果为:{}".format(response.json()))
        # 调用通用断言方式
        utils.assert_common(self,status,code,message,response)
        # 调用查询部门接口完成查询操作
        query_headers = {"Authorization": app.token}
        response = self.query_api.query(params_param=app.gl_dep_id, headers_param=query_headers)
        logging.info("修改部门后返回的结果为:{}".format(response.json()))
        # 调用通用断言方式
        utils.assert_common(self, status, code, message, response)
        # 调用修改部门接口完成修改操作
        update_headers = {"Content-Type": "application/json", "Authorization": app.token}
        response = self.update_api.update(params_param=app.gl_dep_id,headers_param=update_headers,json_data=update_request_body)
        logging.info("修改部门后返回的结果为:{}".format(response.json()))
        # 调用通用断言方式
        utils.assert_common(self, status, code, message, response)
        # 调用删除部门接口完成删除操作
        delete_headers = {"Authorization": app.token}
        response = self.delete_api.delete(params_param=app.gl_dep_id,headers_param=delete_headers)
        logging.info("删除部门后返回的结果为:{}".format(response.json()))
        # 调用通用断言方式
        utils.assert_common(self, status, code, message, response)