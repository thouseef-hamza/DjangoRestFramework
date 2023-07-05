import json
from django.http import JsonResponse,HttpResponse
from products.models import Product
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer

# Create your views here.

""" 
def api_home(request,*args,**kwargs):
    print(request.GET) # url query params
    body = request.body # byte string of JSON data
    data={}
    try:
        data = json.loads(body) #string of JSON data -> Python dictionary
    except:
        pass
    print(data)
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers) 
    data['content_type'] = request.content_type
    return JsonResponse(data)
"""

#  model instance as API Response

""" 
def api_home(request,*args,**kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data={}
    if model_data:
        data['id'] = model_data.id
        data['title'] = model_data.title
        data['content'] = model_data.content
        data['price'] = model_data.price
        # model instance
        # turn a Python dict
        # return JSON to my client
    return JsonResponse(data)
"""

# model instance to dictionary
"""
def api_home(request,*args,**kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data={}
    if model_data:
        data = model_to_dict(model_data,fields=['id','title'])
    return JsonResponse(data)
"""

# Model Instance to Dictionary
"""

def api_home(request,*args,**kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data={}
    if model_data:
        data = model_to_dict(model_data,fields=['id','title','price'])
    return JsonResponse(data)
    #     data=dict(data)
    #     json_str_data = json.dumps(data)
    # return HttpResponse(json_str_data,headers={"content_type":"application/json"})
"""

"""
@api_view(["GET","POST"])
def api_home(request,*args,**kwargs):

    #DRF API View

    instance = Product.objects.all().order_by("?").first()
    data={}
    if instance:
        # data = model_to_dict(instance,fields=['id','title','price','sale_price'])
        data = ProductSerializer(instance).data
    return Response(data)
"""

@api_view(["POST"])
def api_home(request,*args,**kwargs):
    """ 
    DRF API View
    """
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save()
        # instance = forms.save()
        print(serializer.data) 
        return Response(serializer.data)
    else:
        return Response({"invalid":"not good data"},status=400)