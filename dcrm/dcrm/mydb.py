import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'hbstudent',
	passwd = 'hbstudent'
	) 

#prepare cursor object
cursorObject= dataBase.cursor()

#create database
cursorObject.execute("CREATE DATABASE dcrmdjango")

print("all done!")
