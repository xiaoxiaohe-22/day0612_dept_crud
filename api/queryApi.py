import requests
import app


class QueryApi(object):
    def __init__(self):
        self.query_url = app.URL + "/api/company/department/"

    # 查询方法
    def query(self, params_param, headers_param):
        return requests.get(url=self.query_url+params_param, headers=headers_param)
