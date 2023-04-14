from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from .forms import EditForm

# Create your views here.

def profile(request, username):
    user = User.objects.get(username=username)
    user_url = f"/static/profile/media/{user.username}.jpg"

    context = {'user':user,
               'user_url':user_url}

    return render(request, 'profile/home.html', context)

def edit(request, username):
    user = User.objects.get(username=username)
    form = EditForm(instance=user)

    if request.method == "POST":
        form = EditForm(request.POST, instance=user)
        if form.is_valid():
            user.save()
            return redirect('profile:profile', username=user.username)

    context = {'user':user,
               'form':form}
    
    return render(request, 'profile/edit.html', context)