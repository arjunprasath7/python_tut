#!/usr/bin/env python
import tasklib
import sys, traceback
import re
getInput=raw_input("Please Enter Two Input Numbers (,) Separator : ")
checkAlpha=re.search('[a-zA-Z]+',getInput)
if(checkAlpha==None):
	unBoundData=getInput.split(',')
	var1=unBoundData[0]
	var2=unBoundData[1]
	if(len(unBoundData)>2):
		print "Please enter only two parameters"
		sys.exit(0)
	else:
		getOperationType=raw_input(" 1.Addition \n 2.Subtraction \n 3.Mulitplication \n 4.Division \n Please Enter Your Choice : ")
		getOperationTy=float(getOperationType)
		if(getOperationTy==1):
			getData=tasklib.addfun(var1,var2)
		elif(getOperationTy==2):
			getData=tasklib.subfun(var1,var2)
		elif(getOperationTy==3):
			getData=tasklib.mulfun(var1,var2)
		elif(getOperationTy==4):
			getData=tasklib.divfun(var1,var2)
		else:
			print " Please Enter An Valid Option "
else:
	print "Only Numbers Are Allowed"

