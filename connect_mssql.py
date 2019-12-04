import pyodbc


import json
import simplejson
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
data_json = json.dumps(data)
print (data_json)

