import httplib, urllib
import json

data = {
    "method": "getAvailableApiList",
    "params": [],
    "id": 1,
    "version": "1.0"
}
params = urllib.urlencode({'@number': 12424, '@type':'issue', '@action':'show'})
headers = {"Content-type": "application/json"}

conn = httplib.HTTPConnection("http://192.168.122.1:8080/sony/camera")
conn.request("POST", " ", params, headers)
response = conn.getresponse()
print response.status, response.reason

data = response.read()

print data
conn.close()
