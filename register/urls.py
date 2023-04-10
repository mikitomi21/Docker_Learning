from django.contrib import admin
from django.urls import path
from . import views

app_name = 'register'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('singup/', views.singup, name='singup'),
]
