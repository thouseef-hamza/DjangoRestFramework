import requests

endpoint = "http://localhost:8000/api/products/"

data={
    "title":"This Field Is Done",
    "price":32.99,
}

get_response=requests.post(endpoint,json=data) #HTTP Request
print(get_response.json())  
