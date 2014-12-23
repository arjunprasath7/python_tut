#!/usr/bin/env python
import urllib2
import json
requestUrl = urllib2.Request('https://api.github.com/users/mralexgray/repos')
response = urllib2.urlopen(requestUrl)
dataResponse = response.read()
getData=json.loads(dataResponse)
print "Expected Output As Follows :"
for i in getData:
	isFork=i["fork"]
	if(isFork==False):
		print i["name"]