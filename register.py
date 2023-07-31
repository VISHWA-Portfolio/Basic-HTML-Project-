#!C:\Python3.11\python.exe

import cgi
import mysql.connector

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<body>")

print("<h1>Thank you for Register</h1>")
print("<a href='index.html'>Back to Home</a>")

form=cgi.FieldStorage()

fname=form.getvalue("name")
fschool=form.getvalue("school")
fmark=form.getvalue("mark")
fcontact=form.getvalue("contact")

print(fname,fschool,fmark,fcontact)

mydb=mysql.connector.connect(
	host="localhost",
	user="root",
	password="",
	database="VIT"
	)

sql="INSERT INTO data(name,school,mark,contact)VALUES(%s,%s,%s,%s)";
val=(fname,fschool,fmark,fcontact)

mycursor=mydb.cursor()

mycursor.execute(sql,val)
mydb.commit()

print("</body>")

