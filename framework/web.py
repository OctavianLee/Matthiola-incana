# -*- coding: utf-8 -*-

class Handler(object):
    '''The basic handler.'''


class Request(object):

    @property
    def headers(self, name, value):
        pass

    @property
    def cookies(self):
        pass

    def head(self):
        pass
    
    def get(self):
        pass

    def post(self):
        pass

    def delete(self):
        pass

    def put(self):
        pass
