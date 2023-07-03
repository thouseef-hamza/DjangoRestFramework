import requests

# endpoint = "https://httpbin.org/status/200/"
endpoint = "https://httpbin.org/anything"

get_response=requests.get(endpoint,json={"query":"Hello World"}) #HTTP Request
print(get_response.text) #Print Raw Text Response

"""
HTTP Request -> HTML
REST API HTTP Request -> JSON Sometimes in XML Format
-----------------------------------------------------
JavaScript Object Notation (JSON) ~ Python dictionary
"""

print(get_response.json()) 
print(get_response.status_code) 