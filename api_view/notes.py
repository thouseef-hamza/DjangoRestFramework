# ===============================================================================================================>
# =================================== Function Based API View ===================================================
# ===============================================================================================================
# api_view() ---------------------------->
"""
This wrapper provides you a few bits of functionality such as making sure you recieve Request instances in your view,
and adding context to Response objects so that content negotiation can be performed

The wrapper also provide behaviour such as returning 405 Method Not Allowed responses when appropriate,and handling 
any ParseError exceptions that occur when accessing request.data with malformed input

By default only GET methods will be accepted.Other methods will respond with "405 Method Not Allowed". 

@api_view(['GET','POST','PUT','DELETE'])
"""
# Request --------------->
"""
REST framework's Request objects provide flexible request parsing that allows 
you to  treat requests with JSON data or other media types in the same way 
that you would normally deal with form data 

<> request.data - request.data returns parsed content of the request body.This is 
   similiar to the standard  request.POST and request.FILES attributes except that:
   - It includes all parsed content,including file and non-file inputs.
   - It supports parsing the content of HTTP methods other than  POST,meaning that you 
     can access  the content of PUT and PATCH requests.
   - It supports REST Framework's flexible request parsing,rather than just supporting 
     form data.For example you can handle incoming JSON data in the same way that you 
     handle incoming form data
<> request.method - returns the uppercased string representation of the request's HTTP Meethod 
<> request.query_params - request.query_params is a more correctly named synonym for request.GET 
"""
# Response() ------------------>
"""
REST framework supports HTTP content negotiation by providing a Response class 
which allows you to return content that can be rendered into multiple content types,
depending on the client request.

Response objects are initialized with data, which should consist of native Python primitives.
REST framework then uses standard HTTP content negotiation to determine how it should render 
the final response content.

Response class simply provides a nicer interface for returning content-negotiated Web API responses,
that can be rendered to multiple formats

Syntax :- Response(data,status=None,template_name=None,headers=None,content_type=None) 
          <> data - The unrendered,serialized data for the response.
          <> status - A status code for the response.Defaults to 200.
          <> template_name - A template name to use only if HTML Renderer or some other 
                             custom template renderer is the accepted renderer for the response  
          <> headers - A dictionary of HTTP header to use in the response.
          <> content_type - The content_type of the response.Typically,this will be set 
                            automatically by the renderer as determined by content negotiation 
                            but there may be some cases where you need to specify
                            the content type explicitly.
                             
                            
"""
# ===============================================================================================================================================
# ============================================== Class Based API View ===========================================================================
# ===============================================================================================================================================
"""
REST Framework provides an API View class,which subclass Django's View Class

API View class different from regular View Class:-
<> Requests passed to handler methods will be REST framework's Request 
   instances,not Django's HttpRequest instances.
<> Handler method may returns REST frameworks Response,instead of Django's 
   HttpResponse.The view will manage content negotiation and setting the correct
   renderer on the response.
<> Any APIException exceptions will be caught and mediated into appropriate responses.
<> Incoming request will be authenticated and appropriate  permission and/or throttle checks
   will be run before dispatching the request to the handler method.
   get(),post(),put(),delete() 
"""