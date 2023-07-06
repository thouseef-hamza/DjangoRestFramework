import requests


headers =  { 
    'Authorization' : 'Bearer d14cec886b6b17273a04c4c1f33984b02ffdeb2f'
}

endpoint = "http://localhost:8000/api/products/"

data={
    "title":"This Field Is Done",
    "price":32.99,
}

get_response=requests.post(endpoint,json=data,headers=headers) #HTTP Request
print(get_response.json())  

