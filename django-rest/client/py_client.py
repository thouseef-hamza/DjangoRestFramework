import requests
import json

# URL =   "http://127.0.0.1:8000/api/"
# # print(URL) 

# r = requests.get("http://127.0.0.1:8000/api")

# data = r.json()

# print(data)

URL = "http://127.0.0.1:8000/student_create/"

data = {
    'name' : 'thgyhjerin',
    'roll' : 120,
    'city' : 'o'
}
json_data = json.dumps(data)

r = requests.post(url=URL,data=json_data)
print(r.text)
data = r.json()
print(data)