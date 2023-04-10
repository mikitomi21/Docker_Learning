from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User


def home(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'main/home.html', context)