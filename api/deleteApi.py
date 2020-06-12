import requests
import app


class DeleteApi(object):
    def __init__(self):
        self.delete_url = app.URL + "/api/company/department/"

    # 删除方法
    def delete(self, params_param, headers_param):
        return requests.delete(url=self.delete_url+params_param, headers=headers_param)
