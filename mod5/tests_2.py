import unittest

from app_2 import app


class TestRemoteCodeUsage(unittest.TestCase):
    def setUp(self) -> None:
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()

    def test_ok(self):
        data = {
            'code': 'print("hello")',
            'time': '5'
        }
        response = self.app.post('/run_code', json=data)
        self.assertTrue('False' in response.text)

    def test_timeout_is_lower_than_working_time(self):
        data = {
            'code': 'import time; time.sleep(15)',
            'time': '5'
        }
        response = self.app.post('/run_code', json=data)
        self.assertTrue('True' in response.text)

    def test_incorrect_form_data(self):
        data = {
            'code': 'print("uwu")',
            'time': 'print("owo")'
        }
        response = self.app.post('/run_code', json=data)
        self.assertTrue('Invalid input' in response.text)

    def test_unprotected_code(self):
        data = {
            'code': "from subprocess import run; run(['./kill_the_system.sh'])",
            'time': '1'
        }
        response = self.app.post('/run_code', json=data)
        self.assertTrue('Resource temporarily unavailable' in response.text)
