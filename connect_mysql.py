import json 
from flask import Flask
import mysql.connector 

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="toorpoor",
  database="homework1"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

print (json.dumps(myresult))

