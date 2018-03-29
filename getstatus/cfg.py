import os
import inspect
import json

def getConfig():                                                        
    "get config object"                                               
    configfilename = "config.json"
    path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    configfilepath = os.path.join(path, configfilename)
    config = json.load(open(configfilepath)) 
    return config