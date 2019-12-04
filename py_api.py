import requests
import json 

response = requests.get("http://10.20.10.230:8080")
print(response.text)

data = json.loads(response.text)

print (data)
