# -*- coding: utf-8 -*-


class HTTPError(Exception):
    '''An exception to handle the http error.'''
    def __init__(self, code, message=None):
        self.code = code
        self.message = message

    def __str__(self):
        return 'Http {0}: {1}'.format(self.code, self.message)
