import time
import unittest
from BeautifulReport import BeautifulReport
import app
# 由于是四个接口分别测试,所以这里虽然写在一个py文件但是组织四个测试套件,分别生成四个测试报告
test_suite_add = unittest.TestLoader().discover(start_dir=app.BASE_DIR + "/script/", pattern="test_01*.py")

test_suite_query = unittest.TestLoader().discover(start_dir=app.BASE_DIR + "/script/", pattern="test_02*.py")

test_suite_update = unittest.TestLoader().discover(start_dir=app.BASE_DIR + "/script/", pattern="test_03*.py")

test_suite_delete = unittest.TestLoader().discover(start_dir=app.BASE_DIR + "/script/", pattern="test_04*.py")

file_name_add = "report_add_{}.html".format(time.strftime("%Y%m%d%H%M%S"))
BeautifulReport(test_suite_add).report(description="这是增加部门接口的测试",
                                       filename=file_name_add, log_path=app.BASE_DIR + "/report/")

file_name_query = "report_query{}.html".format(time.strftime("%Y%m%d%H%M%S"))
BeautifulReport(test_suite_query).report(description="这是查询部门接口的测试",
                                       filename=file_name_query, log_path=app.BASE_DIR + "/report/")

file_name_update = "report_update{}.html".format(time.strftime("%Y%m%d%H%M%S"))
BeautifulReport(test_suite_update).report(description="这是修改部门接口的测试",
                                       filename=file_name_update, log_path=app.BASE_DIR + "/report/")
file_name_delete = "report_delete{}.html".format(time.strftime("%Y%m%d%H%M%S"))

BeautifulReport(test_suite_delete).report(description="这是删除部门接口的测试",
                                       filename=file_name_delete, log_path=app.BASE_DIR + "/report/")