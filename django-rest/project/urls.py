from django.contrib import admin
from django.urls import path,include
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',views.student_detail),
    path('student_create/',views.student_create)
]
