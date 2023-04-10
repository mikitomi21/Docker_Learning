from django.shortcuts import render, HttpResponse, redirect
from .forms import UserLoginForm, UserSingUpForm

# Create your views here.

def login(request):
    form = UserLoginForm()

    if request.method == "POST":
        if form.is_valid() and request.POST.get('username') and request.POST.get('password'):
            form.save()
            redirect('login')

    context = {}
    return render(request, 'register/home.html', context)

def singup(request):
    form = UserSingUpForm()
    context = {}
    return render(request, 'register/home.html', context)