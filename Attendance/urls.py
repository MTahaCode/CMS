from django.contrib import admin
from django.urls import path
from Attendance import views

urlpatterns = [
    path('', views.main , name='home'),
    path('another/', views.another , name='another'),
    path('save_attendance/', views.save_attendance, name='save_attendance'),
    path('add_New_Date/', views.add_New_Date, name='add_New_Date'),
    path('add_New_Attendance/', views.add_New_Attendance, name='add_New_Attendance'),
    path('delete_attendance_of_one_date/', views.delete_attendance_of_one_date, name='delete_attendance_of_one_date'),
]
