import requests
import app


class LoginApi(object):
    def __init__(self):

        self.login_url = app.URL + "/api/sys/login"

    def login(self, json_data, headers_data):
        response = requests.post(url=self.login_url, json=json_data, headers=headers_data)
        app.token = "Bearer " + response.json().get("data")
