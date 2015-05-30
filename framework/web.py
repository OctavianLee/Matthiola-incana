# -*- coding: utf-8 -*-


class HTTPError(Exception):
    '''An exception to handle the http error.'''
    def __init__(self, code, message=None):
        self.code = code
        self.message = message

    def __str__(self):
        return 'Http {0}: {1}'.format(self.code, self.message)


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
