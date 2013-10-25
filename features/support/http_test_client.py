from pymongo import MongoClient
import requests
from features.support.support import App, BaseClient


class HTTPTestClient(BaseClient):
    def __init__(self, database_name):
        self.database_name = database_name
        self._claim_app = App("5000")
        self._start()

    def get(self, url, headers=None, allow_redirects=False):
        response = requests.get(self._claim_app.url(url), headers=headers, allow_redirects=allow_redirects)
        return HTTPTestResponse(response)

    def post(self, url, **message):
        headers = dict(message.get("headers", []))
        if "data" in message:
            headers.update({"Content-type": message['content_type']})
            response = requests.post(
                self._claim_app.url(url),
                data=message['data'],
                headers=headers,
                timeout=60,
            )
        else:
            raise Exception("Incorrect message")
        return HTTPTestResponse(response)

    def storage(self):
        return MongoClient('localhost', 27017)[self.database_name]

    def spin_down(self):
        self._claim_app.stop()

    def _start(self):
        try:
            self._claim_app.start()
        except:
            self.spin_down()
            raise


class HTTPTestResponse:
    def __init__(self, response):
        self.status_code = response.status_code
        self.data = response.text
        self.headers = response.headers
