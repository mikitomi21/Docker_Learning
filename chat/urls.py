from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('delete<int:pk>/', views.delete, name='delete'),
    path('edit<int:pk>/', views.edit, name='edit'),
    path('new_room<str:username>/', views.new_room, name='new_room')
]