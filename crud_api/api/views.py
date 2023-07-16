from django.shortcuts import render
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
import io
# Create your views here.
# =============================================================================================================================

                              #     Function Based View  (FBV)
                              
# =============================================================================================================================

"""
@csrf_exempt
def student_api(request):
     if request.method == 'GET':
          json_data = request.body
          stream = io.BytesIO(json_data)
          python_data = JSONParser().parse(stream)
          id = python_data.get('id',None)
          print(id)
          if id is not None:
               student = Student.objects.get(id=id)
               serializer = StudentSerializer(student)
               json_data = JSONRenderer().render(serializer.data)
               return HttpResponse(json_data,content_type='application/json')
          student = Student.objects.all()
          serializer = StudentSerializer(student,many=True)
          json_data = JSONRenderer().render(serializer.data)
          return HttpResponse(json_data,content_type='application/json')
     
     if request.method == 'POST':
          json_data = request.body
          stream = io.BytesIO(json_data)
          python_data = JSONParser().parse(stream)
          serializer = StudentSerializer(data=python_data)
          if serializer.is_valid():
               serializer.save()
               res = {'msg':'Data Created'}
               json_data = JSONRenderer().render(res)
               return HttpResponse(json_data,content_type='application/json')
          json_data = JSONRenderer().render(serializer.errors)
          return HttpResponse(json_data,content_type='application/json')
     
     if request.method == 'PUT':
          json_data = request.body
          stream = io.BytesIO(json_data)
          python_data = JSONParser().parse(stream)
          id = python_data.get('id')
          student = Student.objects.get(id=id)
          serializer = StudentSerializer(student,data=python_data,partial=True)
          if serializer.is_valid():
               serializer.save()
               res = {'msg':'Data Updated !! '}
               json_data = JSONRenderer().render(res)
               return HttpResponse(json_data,content_type='application/json')
          json_data = JSONRenderer().render(serializer.errors)
          return HttpResponse(json_data,content_type='application/json')
     
     if request.method == 'DELETE':
          json_data = request.body
          stream = io.BytesIO(json_data)
          python_data = JSONParser().parse(stream)
          id = python_data.get('id')
          student = Student.objects.get(id=id)
          student.delete()
          res = {'msg':'Data Deleted !!'}
          # json_data = JSONRenderer().render(res)
          # return HttpResponse(json_data,content_type='application/json')
          return JsonResponse(res,safe=False) # We can use this instead of commented one
"""
          
# =============================================================================================================================

                              #     Class Based View  (CBV)
                              
# =============================================================================================================================

@method_decorator(csrf_exempt,name='dispatch')
class StudentAPI(View):
     def get(self,request,*args,**kwargs):
          json_data = request.body
          stream = io.BytesIO(json_data)
          python_data = JSONParser().parse(stream)
          id = python_data.get('id',None)
          print(id)
          if id is not None:
               student = Student.objects.get(id=id)
               serializer = StudentSerializer(student)
               json_data = JSONRenderer().render(serializer.data)
               return HttpResponse(json_data,content_type='application/json')
          student = Student.objects.all()
          serializer = StudentSerializer(student,many=True)
          json_data = JSONRenderer().render(serializer.data)
          return HttpResponse(json_data,content_type='application/json')
     
     def post(self,request,*args,**kwargs):
          json_data = request.body
          stream = io.BytesIO(json_data)
          python_data = JSONParser().parse(stream)
          serializer = StudentSerializer(data=python_data)
          if serializer.is_valid():
               serializer.save()
               res = {'msg':'Data Created'}
               json_data = JSONRenderer().render(res)
               return HttpResponse(json_data,content_type='application/json')
          json_data = JSONRenderer().render(serializer.errors)
          return HttpResponse(json_data,content_type='application/json')
     
     def put(self,request,*args,**kwargs):
          json_data = request.body
          stream = io.BytesIO(json_data)
          python_data = JSONParser().parse(stream)
          id = python_data.get('id')
          student = Student.objects.get(id=id)
          serializer = StudentSerializer(student,data=python_data,partial=True)
          if serializer.is_valid():
               serializer.save()
               res = {'msg':'Data Updated !! '}
               json_data = JSONRenderer().render(res)
               return HttpResponse(json_data,content_type='application/json')
          json_data = JSONRenderer().render(serializer.errors)
          return HttpResponse(json_data,content_type='application/json')
     
     def delete(self,request,*args,**kwargs):
          json_data = request.body
          stream = io.BytesIO(json_data)
          python_data = JSONParser().parse(stream)
          id = python_data.get('id')
          student = Student.objects.get(id=id)
          student.delete()
          res = {'msg':'Data Deleted !!'}
          # json_data = JSONRenderer().render(res)
          # return HttpResponse(json_data,content_type='application/json')
          return JsonResponse(res,safe=False) # =========================> # We can use this instead of commented one
     
     