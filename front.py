# Fetching data from the server
import requests
import json

url = "http://127.0.0.1:8000/api/create/"
# data=requests.get(url)
data = {"id": 4, "name": "Rahul", "roll": 104, "city": "Mumbai"}
json_data = json.dumps(data)
r = requests.post(url=url, data=data)
print(r.json())
