from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<str:username>/', views.profile, name='profile'),
    path('<str:username>/edit', views.edit, name='edit'),
]
