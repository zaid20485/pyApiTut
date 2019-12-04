import json 
from flask import Flask
import mysql.connector 

mydb = mysql.connector.connect(
  host="10.20.10.230",
  user="test",
  passwd="test",
  database="testDB"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM users")

myresult = mycursor.fetchall()

print (json.dumps(myresult))

