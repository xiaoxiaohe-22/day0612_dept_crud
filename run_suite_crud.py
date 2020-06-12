import time
import unittest
from BeautifulReport import BeautifulReport

import app

test_suite = unittest.TestLoader().discover(start_dir=app.BASE_DIR + "/script/", pattern="dept_crud.py")

file_name = "report_dept_crud_{}.html".format(time.strftime("%Y%m%d%H%M%S"))
BeautifulReport(test_suite).report(description="这是部门场景的测试",
                                   filename=file_name, log_path=app.BASE_DIR + "/report/")
