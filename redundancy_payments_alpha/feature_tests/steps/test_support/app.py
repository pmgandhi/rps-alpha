import os
import subprocess
import time
import requests


def wait_until(condition, timeout, interval):
    deadline = time.time() + timeout
    while time.time() < deadline:
        if condition():
            return
        else:
            time.sleep(interval)
    raise RuntimeError("Timed out when starting app (timeout=%d)" % timeout)


class app(object):
    def __init__(self):
        self._port = 8000

    def run(self):
        self._subprocess = subprocess.Popen(
            ["python", "start_app.py"],
            preexec_fn=os.setsid,
            stderr=subprocess.STDOUT,
            stdout=subprocess.PIPE
        )
        wait_until(self._is_running, timeout=15, interval=0.1)

    def stop(self):
        if self._subprocess is None:
            raise RuntimeWarning("Attempted to stop the "
                                 "app before it was started")
        os.killpg(self._subprocess.pid, 9)
        self._subprocess.communicate()

    def _is_running(self):
        try:
            return requests.get(self._status_url).status_code == 200
        except Exception as _:
            return False

    @property
    def _status_url(self):
        return "http://localhost:{port}/_status".format(port=self._port)
