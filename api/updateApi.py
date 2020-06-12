import requests
import app


class UpdateApi(object):
    def __init__(self):
        self.update_url = app.URL + "/api/company/department/"

    # 修改方法
    def update(self, params_param, headers_param,json_data):
        return requests.put(url=self.update_url+params_param, headers=headers_param,json=json_data)
