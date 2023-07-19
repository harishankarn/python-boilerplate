#!/usr/bin/env python
import unittest
import calculator
import app
#https://joachim8675309.medium.com/jenkins-ci-pipeline-with-python-8bf1a0234ec3
class TestHello(unittest.TestCase):

    def setUp(self):
        app.app.testing = True
        self.app = app.app.test_client()

    def test_hello(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, b'Hello World!\n')

    def test_hello_hello(self):
        rv = self.app.get('/hello/')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, b'Hello World!\n')

    def test_hello_name(self):
        name = 'Simon'
        rv = self.app.get(f'/hello/{name}')
        self.assertEqual(rv.status, '200 OK')
        self.assertIn(bytearray(f"{name}", 'utf-8'), rv.data)
    def test_addition(self):
        assert 4 == calculator.add(2, 2)
    def test_subtraction(self):
        assert 2 == calculator.subtract(4, 2)
if __name__ == '__main__':
    unittest.main()
TEST_CASES
#chmod +x new.py