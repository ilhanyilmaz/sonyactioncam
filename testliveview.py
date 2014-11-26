#!/usr/bin/python

import sys
import json
import urllib2
from pprint import pprint
import collections

liveviewurl = "http://10.0.0.1:60152/liveview.JPG?%211234%21http%2dget%3a%2a%3aimage%2fjpeg%3a%2a%21%21%21%21%21"

params = collections.OrderedDict([
          ("method", "liveviewStatus"),
          ("params", []),
          ("id", 1),
          ("version", "1.0")])

def int_or_str(v):
    if v.lower() == "false":
        return False
    if v.lower() == "true":
        return True

    try:
        return int(v)
    except ValueError:
        return v

if len(sys.argv) > 1:
    params["method"] = sys.argv[1]
    if len(sys.argv) > 2:
        params["params"] = [int_or_str(v) for v in sys.argv[2:]]

print urllib2.urlopen("http://10.0.0.1:10000/sony/camera",
    json.dumps(params)).read()

#response =  urllib2.urlopen(liveviewurl)
#print response 



#responsejson = response.read()
#print responsejson
