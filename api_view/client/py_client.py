import requests
import json

URL = "http://127.0.0.1:8000/student_api/"

def get_data(id=None):
     data = {}
     header={'content-Type':'application/json'}
     if id is not None:
          data = {'id':id}
     json_data = json.dumps(data)
     r = requests.get(url=URL,data=json_data,headers=header)
     data = r.json()
     print(data)

# get_data(2)

def post_data():
     header={'content-Type':'application/json'}
     data = {
          'name' : 'thousi',
          'roll' : 105,
          'city' : 'kasargod'
     }
     json_data = json.dumps(data)
     r = requests.post(url=URL,data=json_data,headers=header)
     data = r.json()
     print(data) 
     
# post_data()

def update_data():
     header={'content-Type':'application/json'}
     data = {
          'id' : 2,
          'name' : 'Safiya',
          'city' : 'Bengaluru'
     }
     json_data = json.dumps(data)
     r = requests.put(url=URL,data=json_data,headers=header)
     data = r.json()
     print(data) 
     
# update_data()

def delete_data():
     header={'content-Type':'application/json'}
     data = {'id' : 5}
     json_data = json.dumps(data)
     r = requests.delete(url=URL,data=json_data,headers=header)
     data = r.json()
     print(data) 
     
delete_data()
