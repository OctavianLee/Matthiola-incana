# -*- coding: utf-8 -*-
import re


class Route(object):

    def __init__(self, maps=None):
        """Initializes the class.

        Args:
            maps: the dictionary of the pairing of the url's patterns and
                handlers.
        """
        if maps:
            self.maps = maps
        else:
            self.maps = []


    def add(self, path, handler):
        """Adds a handler to a path.

        Args:
            path: a url path.
            handler: a handler.

        Returns:
            mapping: the tuple of the paring of a path and a handler.
        """
        regex = self.__parser(path)
        compiled_regex = re.compile(regex)
        mapping = (compiled_regex, handler)
        self.maps.append(mapping)
        return mapping

    def __parser(self, path):
        """Convert a route path into a regular expression's pattern.

        Args:
            path: a url path.( '/paths/{path_name}/12/{int:number}')

        Returns:
            parser_regex: a regular expression's pattern.
                ^\/paths\/(?P<path_name>\w+)\/12\/(?P<number>\d+)$
        """
      
        rule = re.compile(r"/({(?:int:)?(?: )*[a-zA-Z_]\w*})")
        url_raw_list = rule.split(path)
        url_list = filter(lambda x: x, url_raw_list)
        parser_regex = '^'
        for elem in url_list:
            parser_regex += "\\"
            if elem.startswith('/'):
                parser_regex += elem
            elif elem.startswith('{'):
                new_elem = elem.replace(' ', '')
                parser_regex += '/'
                if new_elem[1:5] == 'int:':
                    parser_regex += '(?P<{0}>\d+)'.format(
                        new_elem[5:len(new_elem)-1])
                else:
                    parser_regex += '(?P<{0}>\w+)'.format(
                        new_elem[1:len(new_elem)-1])
            else:
                pass
        parser_regex += "$"
        return parser_regex
