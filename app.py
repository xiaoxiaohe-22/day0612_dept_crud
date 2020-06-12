import logging
from  logging import  handlers
import os
# 定义全部变量URL
URL = "http://ihrm-test.itheima.net"

# 获取项目的根路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 定义令牌
token = None
# 定义一个添加成功后的部门id
gl_dep_id = None

# 编写初始化日志的代码
# 1 首先定义一个初始化日志的函数
def init_logging():
    # 2 在函数中，设置日志器
    logger = logging.getLogger()
    # 3 设置日志等级
    logger.setLevel(logging.INFO)
    # 4 设置控制台处理器
    sh = logging.StreamHandler()
    # 5 设置文件处理器（文件处理的作用是设置保存日志的文件地址的：需要使用项目根目录定位到日志文件）
    log_path = BASE_DIR + "/log/ihrm_dept.log"
    fh = logging.handlers.TimedRotatingFileHandler(log_path,
                                                   when='M',
                                                   interval=1,
                                                   backupCount=3,
                                                   encoding='utf-8')
    # 6 设置格式化器
    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(fmt)
    # 7 将格式化器添加到文件处理器和控制台处理当中
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)
    # 8 将文件处理器和控制台处理器添加到日志器当中
    logger.addHandler(sh)
    logger.addHandler(fh)
