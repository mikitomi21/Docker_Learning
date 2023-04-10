from django.shortcuts import render, HttpResponse, redirect
from .forms import UserLoginForm, UserSingUpForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

def loginUser(request):
    form = UserLoginForm()

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('main:home')
        else:
            messages.error(request, "User doesn't exist")

    context = {'form':form}
    return render(request, 'register/login.html', context)

@login_required
def logoutUser(request):
    logout(request)
    return redirect('main:home')

def singUpUser(request):
    form = UserSingUpForm()

    if request.method == "POST":
        form = UserSingUpForm(request.POST)
        if form.is_valid() and request.POST.get('username') and request.POST.get('password') and request.POST.get('email') :
            form.save()
            return redirect('main:home')

    context = {'form':form}
    return render(request, 'register/singup.html', context)