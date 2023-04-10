from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User

# Create your views here.

def profile(request, username):
    user = User.objects.get(username=username)
    context = {'user':user}
    return render(request, 'profile/home.html', context)