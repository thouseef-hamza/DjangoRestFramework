from django.urls import path
from . import views

urlpatterns = [

    path('student_api/',views.StudentAPI.as_view(),name='student_api'),
    path('student_api/<int:pk>/',views.StudentAPI.as_view(),name='student_api'),
]

