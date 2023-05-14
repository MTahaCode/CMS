"""
Home URLs
"""
from django.urls import path
from announcements import views

urlpatterns = [
    path('', views.index, name='announcements'),
    path('delete_announcement/', views.delete_announcement, name='delete_announcement/'),
    path('add_announcement/', views.add_announcement, name='add_announcement')
]
