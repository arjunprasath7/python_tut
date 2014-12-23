#!/usr/bin/env python
getInputList=raw_input("Enter the input with (,) separator : ");
import re
checkAlpha=re.search('[a-zA-Z]+',getInputList)
if(checkAlpha==None):
	tempList=getInputList.split(',')
	results = map(float, tempList)
	sortedvalue=sorted(results)
	print "The Given Numbers are ",sortedvalue
	print "The Second Largest Number : ",sortedvalue[-2]
else:
	print "Only Numbers Are Allowed"