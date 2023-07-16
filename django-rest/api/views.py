from django.shortcuts import render
from . models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse ,JsonResponse
from rest_framework.parsers import JSONParser
import io
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

# Model Object - Single Student Data

def student_detail(request):
  stu = Student.objects.all()
  print(stu,"=============================================>")
  serializer = StudentSerializer(stu,many=True )
  # print(serializer,"======================================>")
  # print(serializer.data,"=================================>")
  # json_data = JSONRenderer().render(serializer.data)
  # print(json_data,"=======================================>")
  # return HttpResponse(json_data,content_type='application/json')
  return JsonResponse(serializer.data,safe=False )

@csrf_exempt
def student_create(request):
  if request.method == 'POST':
    json_data = request.body 
    stream = io.BytesIO(json_data)
    python_data = JSONParser().parse(stream)
    serializer = StudentSerializer(data=python_data)
    if serializer.is_valid():
      serializer.save()
      res = {'msg':'Data Inserted'}
      json_data = JSONRenderer().render(res)
      return HttpResponse(json_data,content_type='application/json')
    json_data = JSONRenderer().render(serializer.errors)
    return HttpResponse(json_data,content_type='application/json')
