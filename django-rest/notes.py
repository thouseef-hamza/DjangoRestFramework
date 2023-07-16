



#  What is Application Programming Interface (API)=================================>
"""
An Api is a software intermediary that allows two or more applications to talk to each other

! Private - It can be used within the organizatioin.
! Partner - It can be used within Business Partners.
! Public  - It can be used any third party Developers.
"""
#  What  is Web API ? =============================================================>
"""
~ An API,which is interface for web is called Web API.
~ It may consist of one or more endpoint to define request and response.

! HOW IT WORKS?
~ client makes HTTP Request to API -> API Will communicate to Web applications/Database (if needed)
-> Web application/Database provides required data to API -> API returns data to client

! NOTE :- JSON DATA OR XML DATA 
=================== How to use Web API ? ===============================
~ Register or SignUp to API
~ API may provide API Key for Authentication Purpose
~ Whenever you need to communicate with server make request to API with API key
~ If API Key 
"""

# What is REST ? ============================================================>
"""
~ It is an architectural guideline to develop Web API
"""
# What is REST API/RESTful API ==============================================>
"""
The API which is developed using REST is known as REST API / RESTful API.
"""
#  Django REST Framework =====================================================>
"""
DRF is a powerful and flexible toolkit for building WEB API's

~ Authentication Policies including packages for OAuth1 and OAuth2.
~ Serialization that supports both ORM and non-ORM data sources.
~  
"""
# <=============================================== 1 :- Serializer And Serialization in DRF =========================================>

#  JSON ========================================================>
"""
~ dumps() - convert python object into string
  {'name':'Sonam','roll':101} -> {"name":"Sonam","roll":101}

~ loads() - to parse json string.
  {"name":"Sonam","roll":101} -> {'name':'Sonam','roll':101}
  
  Python --> JSON == dumps
  JSON --> Python == loads
"""

# Serializers ===================================================>
"""
In DRF,serializers are responsible for converting complex data such as querysets,
model instances to native python datatypes(called serialization)
that can then be easily rendered into JSON,XML or other content types which is 
understandable by frontend

Serializer are also responsible for deserialization which means it allows parsed data 
to be converted back into complex types,after validating the incoming data
"""

# Serializer Class ==============================================>
"""
A serializer class is very similiar to a django form and model form class,and includes 
similiar validation flags on the various fields,such as required,max_length and default

DRF provides a serializer class which gives you a powerful,generic way to control the 
output of your responses,as well as ModelSerializer class which provides a useful
shortcut for creating serializers that deal with model instances and querysets
"""
# Serialization =================================================>
"""
The process of converting complex data such as querysets and model instances to 
native Python datatypes are called Serialization in DRF
"""
# JSON Renderer =================================================>
"""
This is used to render Serialized data into JSON which is understandable by Frontend
~ JSONRenderer().render(serializer.data) => Render the data into JSON

============================================================================================

[Complex Datatype]                       [Python Native Datatype]
Model Object       -------------------->      Python Dict       ---------------------------> Json data
                     (Serialization)                                 (Render into JSON)
============================================================================================
"""

# JsonResponse() ===========================================================================>
"""
JsonResponse(data,encoder=DjangoJSONEncoder,safe=True,json_dumps_params=None,**kwargs)

~ An HttpResponse subclass that helps to create JSON-encoded response.It inherits most
  behaviour from its superclass with a couple differnces:
    <> Its default Content-Type header is set to application/json.
    <> The first parameter,data should be a dict instance.If the safe parameter is set to
       False it can be any JSON-serializable object
    <> The safe boolean parameter defaults to True.If it's set to False,any object can be
       passed for serialization (otherwise only dict instances are allowed).If safe is True
       and a non-dict object is passed as the first argument,a TypeError will be raised
    <> The json_dumps_params parameter is a dictionary of keyword arguments to pass the 
       json.dumps() call used to generate the response.
"""
# Serializer Field ==========================================================================>

"""
Serializer Field handle converting between primitive values and internal datatypes.
They also deal with validating input values,as well as retrieving and setting the 
values from their parent objects.
"""
# Deserialization ===========================================================================>
"""
Deserialization allows parsed data to be converted back into complex types,after first validating the incoming data.

==================================================================================================

Json data ---------------> [Python Native Datatype]-----------------------> [Complex Datatype] 
           (Parse Data)                               (DeSerialization)  
             
==================================================================================================
"""
# BytesIO() Method ============================================================================>
"""
A Stream implementation using an in-memory bytes buffer.It inherits BufferedIOBase.
The Buffer is discarded when the close() method is called.

import io
stream = io.BytesIO(json_data)
"""

# JSONParser() ================================================================================>
"""
This is used to parse data to python native datatype.

JSONParser().parse(stream)
"""
 