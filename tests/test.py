#-*- coding: utf-8 -*-
import unittest
from .constants import CONST

from framework.exceptions import HTTPError

class TestCase(unittest.TestCase):
    '''Creates a TestCase template to help test.'''


class HTTPErrorTest(TestCase):
    '''Tests the HTTPError class.'''

    def setUp(self):
        '''Sets up the parameters'''
        self.code = CONST.NUMBER
        self.message = CONST.STRING
        self.http_error = HTTPError(self.code, self.message)

    def test_http_error(self):
        '''Tests the httperror'''
        self.assertEqual(self.http_error.code, self.code)
        self.assertEqual(self.http_error.message, self.message)

