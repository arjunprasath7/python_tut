#!/usr/bin/env python
import MySQLdb
import re
import sys, traceback
db = MySQLdb.connect("localhost", "root", "mysql", "library")
cursor = db.cursor()
# try:
sql = "SELECT * FROM `bookDetails`"
cursor.execute(sql)
result = cursor.fetchall()
print "Book Details \n===========================================================================\n"
print "ids\tbookname\tauthor\tbookavailable\tedition"
print "\n===========================================================================\n"
for rows in result:
	ids = rows[0]
	bookname = rows[1]
	author = rows[2]
	bookavailable = rows[3]
	edition = rows[4]
	print ids, "\t", bookname, "\t\t", author, "\t", bookavailable, "\t\t", edition
print "\n===========================================================================\n"
print "Please select an operation to proceed\n1.Add Book\n2.Edit Book\n3.Remove Book"
getOption = raw_input("Enter The Number Here: ")
checkAlpha=re.search('[a-zA-Z]+',getOption)
if(checkAlpha==None): 
	getOption = int(getOption)
	if getOption == 1:		
		getBookName = raw_input("Enter Book Name: ")
		getAuthorName = raw_input("Enter Author Name: ")
		getBookAvailable = raw_input("Enter No. of Books: ")
		getedition = raw_input("Enter Book Edition: ")
		insertSql = "INSERT INTO `library`.`bookDetails` (`id` ,`bookname` ,`author` ,`bookavailable` ,`edition`)VALUES(NULL , '%s', '%s',%d,%d)" % \
	                (getBookName, getAuthorName,int(getBookAvailable), int(getedition))
	   	cursor.execute(insertSql)
	   	db.commit()
	elif getOption == 2:
		getBookId=raw_input("Please Enter An Valid Book ID :")
		bookId=int(getBookId)
		checkBookExist="select count(*) as num from bookDetails where id=%d" % (int(bookId))
		args=int(bookId)
		cursor.execute(checkBookExist)
		result=cursor.fetchall()
		for rows in result:
			num=rows[0]
		if num == 1:
			upBookName = raw_input("Enter Book Name: ")
			upAuthorName = raw_input("Enter Author Name: ")
			upBookAvailable = raw_input("Enter No. of Books: ")
			upedition = raw_input("Enter Book Edition: ")
			updateSql="UPDATE `bookDetails` SET `bookname` = '%s',`author` = '%s',`bookavailable` = %d,`edition` = %d WHERE `id` =%d" % \
			(upBookName,upAuthorName,int(upBookAvailable),int(upedition),bookId)
			cursor.execute(updateSql)
			db.commit()
		else:
			print "Book Doesn't Exist In Our System"
	elif getOption==3:
		getBookId=raw_input("Please Enter The Book Id You Want To Delete: ")
		bookId=int(getBookId)
		checkBookExist="select count(*) as num from bookDetails where id=%d" % (int(bookId))
		args=int(bookId)
		cursor.execute(checkBookExist)
		result=cursor.fetchall()
		for rows in result:
			num=rows[0]
		if num == 1:
			deleteSql="DELETE FROM `bookDetails` WHERE `id`=%d" % (bookId)
			cursor.execute(deleteSql)
			db.commit()
			print "Book Has Been Removed Successfully"
		else:
			print "Given Id Is Incorrect"
	else:
		print "Please Enter The Above Given Numbers"
else:
	print "Please Enter Valid Number"
# except Exception, e:
#    print "Error: unable to fecth data",e
