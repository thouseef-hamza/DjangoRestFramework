from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.
# Function Based View =====================================================================================>
"""
@api_view(['GET','POST','PUT','PATCH','DELETE'])
def student_api(request,pk=None):
     if request.method == 'GET':
          id = pk
          if id is not None: 
               student = Student.objects.get(id=id)
               serializer = StudentSerializer(student)
               return Response(serializer.data)
          student = Student.objects.all()
          serializer = StudentSerializer(student,many=True,status=status.HTTP_200_OK)
          return Response(serializer.data,status=status.HTTP_200_OK )
     
     if request.method == 'POST': 
          serializer = StudentSerializer(data=request.data)
          if serializer.is_valid():
               serializer.save()
               return Response({'msg':'Data Created'},status=status.HTTP_201_CREATED)
          return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
     
     if request.method == 'PUT':
          id = pk
          student = Student.objects.get(pk=id)
          serializer = StudentSerializer(student,data=request.data)
          if serializer.is_valid():
               serializer.save()
               return Response({'msg':'Complete Data Updated'})
          return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
     
     if request.method == 'PATCH':
          id = pk
          student = Student.objects.get(pk=id)
          serializer = StudentSerializer(student,data=request.data,partial=True)
          if serializer.is_valid():
               serializer.save()
               return Response({'msg':'Partial Data Updated'})
          return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
     
     if request.method == 'DELETE':
          id = pk
          try:
               student = Student.objects.get(pk=id)
          except Student.DoesNotExist:
               return Response({'msg':'User Not Exist'})
          student.delete()
          return Response({'msg':'Data Deleted'})
"""
# Class Based View =================================================================================================>

class StudentAPI(APIView):
     def get(self,request,pk=None,format=None):
          id = pk
          if id is not None: 
               student = Student.objects.get(id=id)
               serializer = StudentSerializer(student)
               return Response(serializer.data)
          student = Student.objects.all()
          serializer = StudentSerializer(student,many=True)
          return Response(serializer.data,status=status.HTTP_200_OK)
     
     def post(self,request,format=None):
          serializer = StudentSerializer(data=request.data)
          if serializer.is_valid():
               serializer.save()
               return Response({'msg':'Data Created'},status=status.HTTP_201_CREATED)
          return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
     
     def put(self,request,pk=None,format=None):
          id = pk
          student = Student.objects.get(pk=id)
          serializer = StudentSerializer(student,data=request.data)
          if serializer.is_valid():
               serializer.save()
               return Response({'msg':'Complete Data Updated'})
          return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
     
     def patch(self,request,pk=None,format=None):
          id = pk
          student = Student.objects.get(pk=id)
          serializer = StudentSerializer(student,data=request.data,partial=True)
          if serializer.is_valid():
               serializer.save()
               return Response({'msg':'Partial Data Updated'})
          return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
          
     
     def delete(self,request,pk=None,format=None):
          id = pk
          try:
               student = Student.objects.get(pk=id)
          except Student.DoesNotExist:
               return Response({'msg':'User Not Exist'})
          student.delete()
          return Response({'msg':'Data Deleted'})