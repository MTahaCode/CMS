from django.contrib import admin
from django.urls import path
from Attendance import views

urlpatterns = [
    path('', views.main , name='home'),
    path('another/', views.another , name='another'),
]
