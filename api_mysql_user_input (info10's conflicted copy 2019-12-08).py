import json 
from flask import Flask
import mysql.connector 

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="test"
)

mycursor = mydb.cursor()

# value = input ("enter the name to insert: ")
# query = "INSERT INTO `users`(`name`) VALUES (%s)"


mycursor.execute("INSERT INTO `users`(`name`) VALUES ('ali')")

mydb.commit()
print(mycursor.rowcount, "record inserted.")
