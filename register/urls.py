from django.contrib import admin
from django.urls import path
from . import views

app_name = 'register'

urlpatterns = [
    path('login/', views.loginUser, name='login'),
    path('singup/', views.singUpUser, name='singup'),
    path('logout/', views.logoutUser, name='logout'),
]
