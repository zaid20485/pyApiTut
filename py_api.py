import requests
import json 

response = requests.get("http://10.20.10.25:8080")
print(response.text)

data = json.loads(response.text)

print (data)
success = data["success"]
msg = data["msg"]

print( success )
print (msg)
