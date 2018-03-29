# coding=utf8

import pprint

import json

class MyPrettyPrinter(pprint.PrettyPrinter):
    def format(self, object, context, maxlevels, level):
        if isinstance(object, unicode):
            return (object.encode('utf8'), True, False)
        return pprint.PrettyPrinter.format(self, object, context, maxlevels, level)

def printjson(json):
    MyPrettyPrinter().pprint(json)

if __name__ == "__main__":
    import sys
    for status in sys.argv[1:]:
        MyPrettyPrinter().pprint(json.load(open(status)))


