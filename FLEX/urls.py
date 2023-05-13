from django.contrib import admin
from django.urls import path,include
from FLEX import views

urlpatterns = [
    path('', views.index , name='login'),
    path('find_UserName/', views.find_UserName , name='find_UserName'),
    path('spf/', views.spf , name='spf'),
]
