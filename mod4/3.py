import unittest
from reg import app

class RegistrationFormTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_valid_email(self):
        response = self.app.post('/registration', data=dict(
            email='test@example.com',
            phone=1234567890,
            name='John Doe',
            address='123 Main St',
            index=12345
        ))
        self.assertEqual(response.status_code, 200)

    def test_invalid_email(self):
        response = self.app.post('/registration', data=dict(
            email='invalid_email',
            phone=1234567890,
            name='John Doe',
            address='123 Main St',
            index=12345
        ))
        self.assertEqual(response.status_code, 400)

    def test_valid_phone(self):
        response = self.app.post('/registration', data=dict(
            email='test@example.com',
            phone=1234567890,
            name='John Doe',
            address='123 Main St',
            index=12345
        ))
        self.assertEqual(response.status_code, 200)

    def test_invalid_phone(self):
        response = self.app.post('/registration', data=dict(
            email='test@example.com',
            phone=123,
            name='John Doe',
            address='123 Main St',
            index=12345
        ))
        self.assertEqual(response.status_code, 400)

    def test_valid_name(self):
        response = self.app.post('/registration', data=dict(
            email='test@example.com',
            phone=1234567890,
            name='John Doe',
            address='123 Main St',
            index=12345
        ))
        self.assertEqual(response.status_code, 200)

    def test_invalid_name(self):
        response = self.app.post('/registration', data=dict(
            email='test@example.com',
            phone=1234567890,
            name='',
            address='123 Main St',
            index=12345
        ))
        self.assertEqual(response.status_code, 400)

    def test_valid_address(self):
        response = self.app.post('/registration', data=dict(
            email='test@example.com',
            phone=1234567890,
            name='John Doe',
            address='123 Main St',
            index=12345
        ))
        self.assertEqual(response.status_code, 200)

    def test_invalid_address(self):
        response = self.app.post('/registration', data=dict(
            email='test@example.com',
            phone=1234567890,
            name='John Doe',
            address='',
            index=12345
        ))
        self.assertEqual(response.status_code, 400)

    def test_valid_index(self):
        response = self.app.post('/registration', data=dict(
            email='test@example.com',
            phone=1234567890,
            name='John Doe',
            address='123 Main St',
            index=12345
        ))
        self.assertEqual(response.status_code, 200)

    def test_invalid_index(self):
        response = self.app.post('/registration', data=dict(
            email='test@example.com',
            phone=1234567890,
            name='John Doe',
            address='123 Main St',
            index=-1
        ))
        self.assertEqual(response.status_code, 400)

    def test_valid_comment(self):
        response = self.app.post('/registration', data=dict(
            email='test@example.com',
            phone=1234567890,
            name='John Doe',
            address='123 Main St',
            index=12345,
            comment='This is a valid comment'
        ))
