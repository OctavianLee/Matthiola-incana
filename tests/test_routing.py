#-*- coding: utf-8 -*-
import re
import unittest
from .constants import CONST
from test import TestCase

from framework.routing import Route


class RouteTest(TestCase):
    '''Tests the Route class.'''

    def setUp(self):
        '''Sets up'''
        self.route = Route()

    def test_add(self):
        '''Tests the method of 'add'.'''
        normal_name = CONST.STRING
        int_name = CONST.STRING
        str_name = CONST.STRING
        handler_name = CONST.STRING
        path = '/' + normal_name + '/{'+ str_name + '}/{int:' + int_name + '}'
        regex = '^\/{0}\/(?P<{1}>\w+)\/(?P<{2}>\d+)$'.format(
            normal_name, str_name, int_name)
        self.route.add(path, handler_name)
        self.assertEqual(self.route.maps[0][0].pattern, regex)
        self.assertEqual(self.route.maps[0][1], handler_name)
