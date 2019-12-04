from flask import Flask
import pyodbc 
import json

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=10.20.10.25;'
                      'Database=attendince;'
                      'UID=sa;'
                      'PWD=@admin00;')

cursor = conn.cursor()

data = cursor.execute('SELECT * FROM empdetails')
data_dict =[]
for row in data:
    data_dict.append(list(row))

# print (data_dict)
# print (data_dict)
data_json = json.dumps(data_dict)
print (data_json)


app = Flask(__name__)
# print (all_data)
@app.route('/')
def example():
   
   return data_json


if __name__ == '__main__':
   app.run(host='0.0.0.0',port='5000')