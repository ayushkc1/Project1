#Fetching data from the server
import requests
url='http://127.0.0.1:8000/student/'
data=requests.get(url)
print(data.json())