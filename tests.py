import unittest
from main import app
from flask.testing import FlaskClient


class CurrencyConverterTests(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()

#��������� ������������ ����������� ������� ��������
    def test_function_works(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('��������� ������ �����', response.data.decode())

#��������� ��������� ������������ ������
    def test_wrong_data(self):
        data = {
            'base_currency': '123',
            'target_currency': 'USD',
            'amount': '100'
        }
        response = self.client.post('/convert', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('�������� ������: 123', response.data.decode())

#���������, ������������ �� �� �������� ��������� ����� ��� ��������� ������ ��� ����������� ������
    def test_custom_case(self):
        data = {
            'base_currency': 'EUR',
            'target_currency': 'JPY',
            'amount': '50'
        }
        response = self.client.post('/convert', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('�������� ������: EUR', response.data.decode())
        self.assertIn('������ ������: JPY', response.data.decode())
        self.assertIn('����������: 50.0', response.data.decode())
        self.assertIn('���������������� �����:', response.data.decode())

if __name__ == '__main__':
    unittest.main()