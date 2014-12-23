#!/usr/bin/env python
import MySQLdb
db = MySQLdb.connect("localhost", "root", "mysql", "test" )
cursor=db.cursor()

print "welcome to student marks entry system"
getMarks = raw_input("Enter the student name and two marks with (,) separation :")
separateList=getMarks.split(',')
name=separateList[0]
mark1=int(separateList[1])
mark2=int(separateList[2])
total=int(separateList[1]) + int(separateList[2])

# sql="INSERT INTO `student_marklist` (`id`, `name`, `mark1`, `mark2`, `total`) VALUES (NULL,'%s', '%d', '%d','%d')" % \
       # (name,mark1,mark2,total)
# sql="INSERT INTO student_marklist(id,name,mark1,mark2,total) VALUES (NULL,'arjun',60,60,120)"
sql = """INSERT INTO student_marklist(id,
         name, mark1, mark2, total)
         VALUES (NULL, 'arjun', 20,20,40)"""
cursor.execute(sql)

sql1="""select count(*) as data from student_marklist"""
cursor.execute(sql1)
data = cursor.fetchall()
print data
# cursor.execute("INSERT INTO `test`.`student_marklist` (`id`, `name`, `mark1`, `mark2`, `total`) VALUES (NULL,'%s', '%d', '%d','%d')",(name,mark1,mark2,total))

