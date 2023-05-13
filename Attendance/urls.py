from django.contrib import admin
from django.urls import path
from Attendance import views

urlpatterns = [
    path('', views.main , name='home'),
    path('another/', views.another , name='another'),
    path('save_attendance/', views.save_attendance, name='save_attendance'),
    path('add_New_Date/', views.save_attendance, name='add_New_Date'),
]
