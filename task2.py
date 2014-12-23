#!/usr/bin/env python
import os
import datetime
import sys, traceback
import time
time = time.time()
try:
	getInputFileSize = os.path.getsize("test.txt")
	print "The File Size : ",getInputFileSize,"kb"
	if(getInputFileSize<1000000):
		try:
			currentTime = datetime.datetime.fromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S')
			contents = open("test.txt").read()
			checkExist=os.path.isfile('newfile.txt')
			if(checkExist==True):
				os.remove('newfile.txt')
			with open('newfile.txt', 'a') as f:
			    f.write(contents)
			    f.write(currentTime)
			    print "Data has been transferred to new file & created as newfile.txt"
		except Exception, e:
			print "Exception Thrown ", e		
except Exception, e:
	print "Exception Thrown ", e