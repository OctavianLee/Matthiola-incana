#-*- coding: utf-8 -*-
import re
import unittest
from .constants import CONST
from test import TestCase

from framework.routing import Route, Map
from framework.web import Handler
from framework.exceptions import HTTPError


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


class MapTest(TestCase):
    '''Tests the Map class.'''

    def setUp(self):
        '''Sets up'''
        self.normal_name = CONST.STRING
        int_name = CONST.STRING
        str_name = CONST.STRING
        handler_name = CONST.STRING
        self.handler = type(handler_name, (Handler,), {}) 
        path = '/' + self.normal_name + '/{'+ str_name + '}/{int:' + int_name + '}'
        route = Route()
        route.add(path, self.handler)
        self.map = Map(route.maps)

    def test_delegate(self):
        url = '/{0}/{1}/{2}'.format(
            self.normal_name, CONST.STRING, CONST.NUMBER)
        handler = self.map.delegate(url)
        self.assertEqual(type(handler), self.handler)
        url += '/{0}'.format(CONST.STRING)
        with self.assertRaises(HTTPError):
            self.map.delegate(url)

