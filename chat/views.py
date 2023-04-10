from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import MessageForm
from .models import Message
from django.contrib.auth import get_user_model

# Create your views here.

def home(request):
    messages = Message.objects.all()
    print(messages)

    User = get_user_model()
    users = User.objects.all()

    form = MessageForm()
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid() and request.POST.get('description'):
            form.save()
            return redirect('chat:home')
        
    context = {'messages':messages,
               'users':users,
               'form':form}
    return render(request, 'chat/home.html', context)

def delete(request, pk):
    message = Message.objects.get(id=pk)

    if request.method == "POST":
        message.delete()
        return redirect('chat:home')

    context = {}
    return render(request, 'chat/delete.html', context)

def edit(request, pk):
    message = Message.objects.get(id=pk)
    form = MessageForm(instance=message)

    if request.method == "POST":
        form = MessageForm(request.POST, instance=message)
        if form.is_valid():
            message.save()
            return redirect('chat:home')

    context = {'form':form}
    return render(request, 'chat/edit.html', context)