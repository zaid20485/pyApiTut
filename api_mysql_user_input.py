import json 
from flask import Flask
import mysql.connector 

mydb = mysql.connector.connect(
  host="10.20.10.25",
  user="root",
  passwd="",
  database="test"
)

mycursor = mydb.cursor()

val = str(input ("enter the userName to insert:"))
query = "INSERT INTO `users`(`name`) VALUES (%s)"


mycursor.execute(query, (val,))

mydb.commit()
print(mycursor.rowcount, "record inserted.")
