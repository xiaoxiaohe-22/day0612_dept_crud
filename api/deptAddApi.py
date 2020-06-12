import requests

import app


class DeptAddApi:
    def __init__(self):
        self.add_url = app.URL + "/api/company/department"

    def dept_add(self, headers_data, json_data):
        return requests.post(url=self.add_url, headers=headers_data, json=json_data)
