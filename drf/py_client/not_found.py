import requests

endpoint = "http://localhost:8000/api/products/1567890"

get_response=requests.get(endpoint) #HTTP Request

print(get_response.json())  
