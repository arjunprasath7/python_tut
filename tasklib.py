#!/usr/bin/env python
import sys, traceback
def addfun(var1,var2):
	var1=float(var1)
	var2=float(var2)
	var3=var1+var2
	print var3
def subfun(var1,var2):
	var1=float(var1)
	var2=float(var2)
	var3=var1-var2
	print var3

def mulfun(var1,var2):
	var1=float(var1)
	var2=float(var2)
	var3=var1*var2
	print var3

def divfun(var1,var2):
	var1=float(var1)
	var2=float(var2)
	if (var2==0):
		print "Division By Zero Value Is Infinity"
		sys.exit(0)
	var3=var1/var2
	print var3
