import requests

# endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"

get_response=requests.post(endpoint,json={"title":None,"content":"Hello World"}) #HTTP Request
# print(get_response.text) #Print Raw Text Response
# print(get_response.status_code) 
"""
HTTP Request -> HTML
REST API HTTP Request -> JSON Sometimes in XML Format
-----------------------------------------------------
JavaScript Object Notation (JSON) ~ Python dictionary
"""

print(get_response.json())  
# print(get_response.status_code)     

